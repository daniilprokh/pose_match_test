from typing import Optional
from enum import Enum

from PySide6.QtWidgets import QMainWindow, QWidget
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import Qt, Slot, Signal, QTimer, QSize

from mediapipe.python.solutions.pose import Pose, PoseLandmark
from mediapipe.framework.formats.landmark_pb2 import NormalizedLandmarkList

import qimage2ndarray

import numpy as np

from camera_handler import CameraHandler
from setting_dialog import SettingDialog
from ui_pose_match_window import Ui_PoseMatchWindow

class PoseMatchStage(Enum):
    DETERMINATION = 0,
    MATCH = 1

class PoseMatchWindow(QMainWindow):
    def __init__(self,
                 parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)

        self.m_ui = Ui_PoseMatchWindow()
        self.m_ui.setupUi(self)

        self.m_ui.settingMenu.aboutToShow.connect(self.openSettings)

        self.m_cameraHandler = CameraHandler(self)
        self.m_cameraHandler.currentImageChanged.connect(
                self.updateCameraImage)
        self.m_ui.startButton.clicked.connect(self.startPoseMatch)

        self.m_pose = None
        self.m_poseMatchStage = None
        self.m_poseLandmarks = [
            PoseLandmark.NOSE,
            PoseLandmark.LEFT_EYE_INNER,
            PoseLandmark.LEFT_EYE,
            PoseLandmark.LEFT_EYE_OUTER,
            PoseLandmark.RIGHT_EYE_INNER,
            PoseLandmark.RIGHT_EYE,
            PoseLandmark.RIGHT_EYE_OUTER,
            PoseLandmark.LEFT_EAR,
            PoseLandmark.RIGHT_EAR,
            PoseLandmark.MOUTH_LEFT,
            PoseLandmark.MOUTH_RIGHT,
            PoseLandmark.LEFT_SHOULDER,
            PoseLandmark.RIGHT_SHOULDER,
            PoseLandmark.LEFT_ELBOW,
            PoseLandmark.RIGHT_ELBOW,
            PoseLandmark.LEFT_WRIST,
            PoseLandmark.RIGHT_WRIST,
            PoseLandmark.LEFT_HIP,
            PoseLandmark.RIGHT_HIP,
            PoseLandmark.LEFT_KNEE,
            PoseLandmark.RIGHT_KNEE,
            PoseLandmark.LEFT_ANKLE,
            PoseLandmark.RIGHT_ANKLE
        ]
        self.m_poseNormIndexSlice = np.zeros(2 * len(self.m_poseLandmarks))

        #self.m_determinationPoseLayout = None

        self.m_determinationTimer = QTimer(self)
        self.m_determinationTimer.setSingleShot(True)
        self.m_determinationTimer.timeout.connect(self.startMatchStage)

    @Slot()
    def openSettings(self):
        setting_dialog = SettingDialog(self)
        if setting_dialog.exec():
            self.m_cameraHandler.changeCameraDevice(
                    setting_dialog.getCurrentCameraDevice())
            self.m_poseLandmarks = setting_dialog.getPoseLandmarks()
            
    @Slot(QImage)
    def updateCameraImage(self, image: QImage):
        scaled_image = image.scaled(self.m_ui.cameraImageLabel.size(),
                                    Qt.KeepAspectRatio,
                                    Qt.SmoothTransformation)
        pixmap = QPixmap.fromImage(scaled_image)
        self.m_ui.cameraImageLabel.setPixmap(pixmap)

    @Slot()
    def startPoseMatch(self):
        if not self.m_poseMatchStage:
            self.m_pose = Pose(min_detection_confidence=0.5,
                               min_tracking_confidence=0.5)
            self.m_cameraHandler.currentImageChanged.connect(
                    self.determinePose)
            self.m_poseMatchStage == PoseMatchStage.DETERMINATION
            self.m_cameraHandler.startCamera()
        elif self.m_poseMatchStage == PoseMatchStage.MATCH:
            self.m_cameraHandler.currentImageChanged.disconnect(
                    self.matchPose)
            self.m_cameraHandler.currentImageChanged.connect(
                    self.determinePose)
            self.m_poseMatchStage == PoseMatchStage.DETERMINATION        

    @Slot(QImage)
    def determinePose(self, image: QImage):
        rgb_view = qimage2ndarray.rgb_view(image)
        results = self.m_pose.process(rgb_view)
        if not results.pose_landmarks:
            self.m_determinationTimer.stop()
            return
        
        pose_index_slice = self.poseNormIndexSlice(
                results.pose_landmarks.landmark)
        is_same_pose = self.comparePose(self.m_poseNormIndexSlice,
                                        pose_index_slice)
        self.m_poseNormIndexSlice = pose_index_slice
        if not (is_same_pose and self.m_determinationTimer.isActive()):
            self.m_determinationTimer.start(5000)

    @Slot()
    def startMatchStage(self):
        pixmap = self.m_ui.cameraImageLabel.pixmap()
        pixmap.scaled(self.m_ui.poseImageLabel.size(),
                                    Qt.KeepAspectRatio,
                                    Qt.SmoothTransformation)
        self.m_ui.poseImageLabel.setPixmap(pixmap)

        self.m_cameraHandler.currentImageChanged.disconnect(
                    self.determinePose)
        self.m_cameraHandler.currentImageChanged.connect(
                    self.matchPose)
        self.m_poseMatchStage = PoseMatchStage.MATCH

    @Slot(QImage)
    def matchPose(self, image: QImage):
        rgb_view = qimage2ndarray.rgb_view(image)
        results = self.m_pose.process(rgb_view)
        if not results.pose_landmarks:
            return
        
        pose_index_slice = self.poseNormIndexSlice(
                results.pose_landmarks.landmark)
        is_same = self.comparePose(self.m_poseNormIndexSlice,
                                        pose_index_slice, 5e-4)
        if is_same:
            self.m_ui.poseImageLabel.setStyleSheet("QLabel { background-color : green; }")
        else:
            self.m_ui.poseImageLabel.setStyleSheet("QLabel { background-color : red; }")

    def comparePose(self, lhs: np.ndarray, rhs: np.ndarray, eps: float = 5e-6) -> bool:
        div = np.linalg.norm(lhs) * np.linalg.norm(rhs)
        if not div:
            return False 
        
        cos_sim = np.dot(lhs, rhs) / div
        return 1.0 - cos_sim < eps
    
    def comparePoseL(self, lhs: np.ndarray, rhs: np.ndarray) -> float:
        div = np.linalg.norm(lhs) * np.linalg.norm(rhs)
        if not div:
            return 0.0
        
        cos_sim = np.dot(lhs, rhs) / div
        return cos_sim

    def poseNormIndexSlice(self, landmark_list: NormalizedLandmarkList) -> np.ndarray:
        slice = np.zeros(2 * len(self.m_poseLandmarks))
        for index, pose_landmark in enumerate(self.m_poseLandmarks):
             slice[2 * index] = landmark_list[pose_landmark].x
             slice[2 * index + 1] = landmark_list[pose_landmark].y
        return slice
