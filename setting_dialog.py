from typing import Optional
from PySide6.QtMultimedia import QMediaDevices, QCameraDevice
from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import QDialog, QWidget

from mediapipe.python.solutions.pose import PoseLandmark

from ui_setting_dialog import Ui_SettingDialog

class SettingDialog(QDialog):
    def __init__(
            self,
            parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)

        self.m_ui = Ui_SettingDialog()
        self.m_ui.setupUi(self)

        self.m_devices = QMediaDevices()
        self.m_currentDevice = QMediaDevices.defaultVideoInput()
        self.m_ui.cameraComboBox.currentIndexChanged.connect(
                self.changeCameraDevice)
        self.updateCameras()
        self.m_devices.videoInputsChanged.connect(self.updateCameras)

        self.m_headLandmarks = {
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
            PoseLandmark.MOUTH_RIGHT
        }
        self.m_leftArmLandmarks = {
            PoseLandmark.LEFT_SHOULDER,
            PoseLandmark.LEFT_ELBOW,
            PoseLandmark.LEFT_WRIST
        }
        self.m_rightArmLandmarks = {
            PoseLandmark.RIGHT_SHOULDER,
            PoseLandmark.RIGHT_ELBOW,
            PoseLandmark.RIGHT_WRIST
        }
        self.m_leftLegLandmarks = {
            PoseLandmark.LEFT_HIP,
            PoseLandmark.LEFT_KNEE,
            PoseLandmark.LEFT_ANKLE
        }
        self.m_rightLegLandmarks = {
            PoseLandmark.RIGHT_HIP,
            PoseLandmark.RIGHT_KNEE,
            PoseLandmark.RIGHT_ANKLE
        }
        self.m_bodyLandmarks = {
            PoseLandmark.LEFT_SHOULDER,
            PoseLandmark.RIGHT_SHOULDER,
            PoseLandmark.LEFT_HIP,
            PoseLandmark.RIGHT_HIP
        }
        self.m_poseLandmarks = (
            self.m_headLandmarks | 
            self.m_leftArmLandmarks |
            self.m_rightArmLandmarks |
            self.m_leftLegLandmarks |
            self.m_rightLegLandmarks
        )

        self.m_ui.headCheckBox.stateChanged.connect(
                self.changeHeadLandmarksPresence)
        self.m_ui.bodyCheckBox.stateChanged.connect(
                self.changeBodyLandmarksPresence)
        self.m_ui.armGroupBox.clicked.connect(
                self.changeArmLandmarksPresence
        )
        self.m_ui.leftArmCheckBox.stateChanged.connect(
                self.changeLeftArmLandmarksPresence
        )
        self.m_ui.rightArmCheckBox.stateChanged.connect(
                self.changeRightArmLandmarksPresence
        )
        self.m_ui.legGroupBox.clicked.connect(
                self.changeLegLandmarksPresence
        )
        self.m_ui.leftLegCheckBox.stateChanged.connect(
                self.changeLeftLegLandmarksPresence
        )
        self.m_ui.rightLegCheckBox.stateChanged.connect(
                self.changeRightLegLandmarksPresence
        )
            
    @Slot()
    def updateCameras(self):
        self.m_ui.cameraComboBox.clear()

        for camera_device in QMediaDevices.videoInputs():
            description = camera_device.description()
            self.m_ui.cameraComboBox.addItem(
                    description,
                    camera_device)
          
        if self.m_ui.cameraComboBox.count() == 0:
            return

        description = QMediaDevices.defaultVideoInput().description()
        self.m_ui.cameraComboBox.setCurrentText(description)

    @Slot(int)
    def changeCameraDevice(self, index : int):
        self.m_currentDevice = self.m_ui.cameraComboBox.itemData(index)

    @Slot(int)
    def changeHeadLandmarksPresence(self, state: int) -> None:
        if state:
            self.m_poseLandmarks &= self.m_leftArmLandmarks
        else:
            self.m_poseLandmarks |= self.m_leftArmLandmarks

    @Slot(int)
    def changeLeftArmLandmarksPresence(self, state: int) -> None:
        if state:
            self.m_poseLandmarks &= self.m_leftArmLandmarks
        else:
            self.m_poseLandmarks |= self.m_leftArmLandmarks

    @Slot(int)
    def changeRightArmLandmarksPresence(self, state: int) -> None:
        if state:
            self.m_poseLandmarks &= self.m_rightArmLandmarks
        else:
            self.m_poseLandmarks |= self.m_rightArmLandmarks
            
    @Slot(bool)
    def changeArmLandmarksPresence(self, cheked: bool) -> None:
        if cheked:
            self.changeLeftArmLandmarksPresence(
                    self.m_ui.leftArmCheckBox.checkState())
            self.changeRightArmLandmarksPresence(
                    self.m_ui.rightArmCheckBox.checkState())
        else:
            self.m_poseLandmarks &= self.m_bodyLandmarks
            self.m_poseLandmarks &= self.m_bodyLandmarks

    @Slot(int)
    def changeLeftLegLandmarksPresence(self, state: int) -> None:
        if state:
            self.m_poseLandmarks &= self.m_leftArmLandmarks
        else:
            self.m_poseLandmarks |= self.m_leftArmLandmarks

    @Slot(int)
    def changeRightLegLandmarksPresence(self, state: int) -> None:
        if state:
            self.m_poseLandmarks &= self.m_rightArmLandmarks
        else:
            self.m_poseLandmarks |= self.m_rightArmLandmarks
            
    @Slot(bool)
    def changeLegLandmarksPresence(self, cheked: bool) -> None:
        if cheked:
            self.changeLeftLegLandmarksPresence(
                    self.m_ui.leftLegCheckBox.checkState())
            self.changeRightLegLandmarksPresence(
                    self.m_ui.rightLegCheckBox.checkState())
        else:
            self.m_poseLandmarks &= self.m_leftLegLandmarks
            self.m_poseLandmarks &= self.m_rightLegLandmarks

    @Slot(int)
    def changeBodyLandmarksPresence(self, state: int) -> None:
        if state:
            self.m_poseLandmarks &= self.m_bodyLandmarks
        else:
            self.m_poseLandmarks |= self.m_bodyLandmarks

    def getPoseLandmarks(self) -> list[PoseLandmark]:
        return list(self.m_poseLandmarks)
    
    def getCurrentCameraDevice(self) -> QCameraDevice:
        return self.m_currentDevice
