# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pose_match_windowMUkFmn.ui'
##
## Created by: Qt User Interface Compiler version 5.15.10
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_PoseMatchWindow(object):
    def setupUi(self, PoseMatchWindow):
        if not PoseMatchWindow.objectName():
            PoseMatchWindow.setObjectName(u"PoseMatchWindow")
        PoseMatchWindow.resize(1107, 783)
        font = QFont()
        font.setPointSize(14)
        PoseMatchWindow.setFont(font)
        self.centralwidget = QWidget(PoseMatchWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(Qt.Horizontal)
        self.verticalLayoutWidget = QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.cameralLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.cameralLayout.setObjectName(u"cameralLayout")
        self.cameralLayout.setContentsMargins(0, 0, 0, 0)
        self.cameraLabel = QLabel(self.verticalLayoutWidget)
        self.cameraLabel.setObjectName(u"cameraLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.cameraLabel.sizePolicy().hasHeightForWidth())
        self.cameraLabel.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(24)
        self.cameraLabel.setFont(font1)
        self.cameraLabel.setAlignment(Qt.AlignCenter)

        self.cameralLayout.addWidget(self.cameraLabel)

        self.cameraImageLabel = QLabel(self.verticalLayoutWidget)
        self.cameraImageLabel.setObjectName(u"cameraImageLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.cameraImageLabel.sizePolicy().hasHeightForWidth())
        self.cameraImageLabel.setSizePolicy(sizePolicy2)
        self.cameraImageLabel.setAlignment(Qt.AlignCenter)

        self.cameralLayout.addWidget(self.cameraImageLabel)

        self.splitter.addWidget(self.verticalLayoutWidget)
        self.verticalLayoutWidget_2 = QWidget(self.splitter)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.poseLayout = QVBoxLayout(self.verticalLayoutWidget_2)
        self.poseLayout.setObjectName(u"poseLayout")
        self.poseLayout.setContentsMargins(0, 0, 0, 0)
        self.poseLabel = QLabel(self.verticalLayoutWidget_2)
        self.poseLabel.setObjectName(u"poseLabel")
        sizePolicy1.setHeightForWidth(self.poseLabel.sizePolicy().hasHeightForWidth())
        self.poseLabel.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setPointSize(23)
        self.poseLabel.setFont(font2)
        self.poseLabel.setAlignment(Qt.AlignCenter)

        self.poseLayout.addWidget(self.poseLabel)

        self.poseImageLabel = QLabel(self.verticalLayoutWidget_2)
        self.poseImageLabel.setObjectName(u"poseImageLabel")
        sizePolicy.setHeightForWidth(self.poseImageLabel.sizePolicy().hasHeightForWidth())
        self.poseImageLabel.setSizePolicy(sizePolicy)
        self.poseImageLabel.setAlignment(Qt.AlignCenter)

        self.poseLayout.addWidget(self.poseImageLabel)

        self.splitter.addWidget(self.verticalLayoutWidget_2)

        self.verticalLayout_4.addWidget(self.splitter)

        self.stageWidget = QWidget(self.centralwidget)
        self.stageWidget.setObjectName(u"stageWidget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.stageWidget.sizePolicy().hasHeightForWidth())
        self.stageWidget.setSizePolicy(sizePolicy3)

        self.verticalLayout_4.addWidget(self.stageWidget)

        self.startButton = QPushButton(self.centralwidget)
        self.startButton.setObjectName(u"startButton")
        self.startButton.setFont(font)

        self.verticalLayout_4.addWidget(self.startButton)

        PoseMatchWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(PoseMatchWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1107, 39))
        self.settingMenu = QMenu(self.menubar)
        self.settingMenu.setObjectName(u"settingMenu")
        font3 = QFont()
        font3.setPointSize(10)
        self.settingMenu.setFont(font3)
        PoseMatchWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(PoseMatchWindow)
        self.statusbar.setObjectName(u"statusbar")
        PoseMatchWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.settingMenu.menuAction())

        self.retranslateUi(PoseMatchWindow)

        QMetaObject.connectSlotsByName(PoseMatchWindow)
    # setupUi

    def retranslateUi(self, PoseMatchWindow):
        PoseMatchWindow.setWindowTitle(QCoreApplication.translate("PoseMatchWindow", u"\u0421\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u0435 \u043f\u043e\u0437", None))
        self.cameraLabel.setText(QCoreApplication.translate("PoseMatchWindow", u"\u041a\u0430\u043c\u0435\u0440\u0430", None))
        self.cameraImageLabel.setText("")
        self.poseLabel.setText(QCoreApplication.translate("PoseMatchWindow", u"\u041f\u043e\u0437\u0430 \u0434\u043b\u044f \u0441\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u044f", None))
        self.poseImageLabel.setText("")
        self.startButton.setText(QCoreApplication.translate("PoseMatchWindow", u"\u0417\u0430\u043f\u0443\u0441\u043a", None))
        self.settingMenu.setTitle(QCoreApplication.translate("PoseMatchWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438...", None))
    # retranslateUi

