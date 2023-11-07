from PySide6.QtMultimedia import (QCamera, QCameraDevice, 
                                  QMediaCaptureSession, QMediaDevices,
                                  QVideoSink, QVideoFrame)
from PySide6.QtGui import QImage
from PySide6.QtCore import QObject, Signal, Slot

class CameraHandler(QObject):
    currentImageChanged = Signal(QImage)

    def __init__(self,
                 parent: QObject | None = ...,
                 device: QCameraDevice = QMediaDevices.defaultVideoInput()):
        super().__init__(parent)

        self.m_device = device
        self.m_camera = None
        self.m_captureSession = None

        self.m_videoSink = QVideoSink(self)

    @Slot()
    def startCamera(self):
        if self.isRunning():
            return

        self.m_camera = QCamera(self.m_device)
        
        self.m_captureSession = QMediaCaptureSession()
        self.m_captureSession.setCamera(self.m_camera)
        
        self.m_captureSession.setVideoSink(self.m_videoSink)
        self.m_videoSink.videoFrameChanged.connect(self.processFrame)

        self.m_camera.start()

    @Slot(QVideoFrame)
    def processFrame(self, frame : QVideoFrame):
        if frame.isValid():
            self.currentImageChanged.emit(frame.toImage())

    @Slot()
    def stopCamera(self):
        self.m_videoSink.videoFrameChanged.disconnect(self.processFrame)
        self.m_camera.stop()

        self.m_captureSession.deleteLater()
        self.m_captureSession = None
        self.m_camera.deleteLater()
        self.m_camera = None

    def changeCameraDevice(self, device: QCameraDevice):
        if (self.m_device == device):
            return
        
        self.m_device = device
        if self.m_camera:
          self.m_camera.setCameraDevice(device)

    def isRunning(self):
        return True if self.m_camera else False
