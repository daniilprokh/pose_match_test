# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'setting_dialogARAOdm.ui'
##
## Created by: Qt User Interface Compiler version 5.15.10
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_SettingDialog(object):
    def setupUi(self, SettingDialog):
        if not SettingDialog.objectName():
            SettingDialog.setObjectName(u"SettingDialog")
        SettingDialog.resize(451, 336)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SettingDialog.sizePolicy().hasHeightForWidth())
        SettingDialog.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(SettingDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.settingLayout = QFormLayout()
        self.settingLayout.setObjectName(u"settingLayout")
        self.cameraLabel = QLabel(SettingDialog)
        self.cameraLabel.setObjectName(u"cameraLabel")

        self.settingLayout.setWidget(0, QFormLayout.LabelRole, self.cameraLabel)

        self.cameraComboBox = QComboBox(SettingDialog)
        self.cameraComboBox.setObjectName(u"cameraComboBox")

        self.settingLayout.setWidget(0, QFormLayout.FieldRole, self.cameraComboBox)

        self.bodyPartLabel = QLabel(SettingDialog)
        self.bodyPartLabel.setObjectName(u"bodyPartLabel")

        self.settingLayout.setWidget(1, QFormLayout.LabelRole, self.bodyPartLabel)

        self.bodyPartWidget = QWidget(SettingDialog)
        self.bodyPartWidget.setObjectName(u"bodyPartWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.bodyPartWidget.sizePolicy().hasHeightForWidth())
        self.bodyPartWidget.setSizePolicy(sizePolicy1)
        self.verticalLayout_2 = QVBoxLayout(self.bodyPartWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.headCheckBox = QCheckBox(self.bodyPartWidget)
        self.headCheckBox.setObjectName(u"headCheckBox")
        self.headCheckBox.setChecked(True)

        self.verticalLayout_2.addWidget(self.headCheckBox)

        self.bodyCheckBox = QCheckBox(self.bodyPartWidget)
        self.bodyCheckBox.setObjectName(u"bodyCheckBox")
        self.bodyCheckBox.setChecked(True)

        self.verticalLayout_2.addWidget(self.bodyCheckBox)

        self.armGroupBox = QGroupBox(self.bodyPartWidget)
        self.armGroupBox.setObjectName(u"armGroupBox")
        sizePolicy.setHeightForWidth(self.armGroupBox.sizePolicy().hasHeightForWidth())
        self.armGroupBox.setSizePolicy(sizePolicy)
        self.armGroupBox.setCheckable(True)
        self.armGroupBox.setChecked(True)
        self.horizontalLayout_2 = QHBoxLayout(self.armGroupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.leftArmCheckBox = QCheckBox(self.armGroupBox)
        self.leftArmCheckBox.setObjectName(u"leftArmCheckBox")
        self.leftArmCheckBox.setChecked(True)

        self.horizontalLayout_2.addWidget(self.leftArmCheckBox)

        self.rightArmCheckBox = QCheckBox(self.armGroupBox)
        self.rightArmCheckBox.setObjectName(u"rightArmCheckBox")
        self.rightArmCheckBox.setChecked(True)

        self.horizontalLayout_2.addWidget(self.rightArmCheckBox)


        self.verticalLayout_2.addWidget(self.armGroupBox)

        self.legGroupBox = QGroupBox(self.bodyPartWidget)
        self.legGroupBox.setObjectName(u"legGroupBox")
        sizePolicy.setHeightForWidth(self.legGroupBox.sizePolicy().hasHeightForWidth())
        self.legGroupBox.setSizePolicy(sizePolicy)
        self.legGroupBox.setCheckable(True)
        self.legGroupBox.setChecked(True)
        self.horizontalLayout_3 = QHBoxLayout(self.legGroupBox)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.leftLegCheckBox = QCheckBox(self.legGroupBox)
        self.leftLegCheckBox.setObjectName(u"leftLegCheckBox")
        self.leftLegCheckBox.setChecked(True)

        self.horizontalLayout_3.addWidget(self.leftLegCheckBox)

        self.rightLegCheckBox = QCheckBox(self.legGroupBox)
        self.rightLegCheckBox.setObjectName(u"rightLegCheckBox")
        self.rightLegCheckBox.setChecked(True)

        self.horizontalLayout_3.addWidget(self.rightLegCheckBox)


        self.verticalLayout_2.addWidget(self.legGroupBox)


        self.settingLayout.setWidget(1, QFormLayout.FieldRole, self.bodyPartWidget)


        self.verticalLayout.addLayout(self.settingLayout)

        self.buttonBox = QDialogButtonBox(SettingDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(SettingDialog)
        self.buttonBox.accepted.connect(SettingDialog.accept)
        self.buttonBox.rejected.connect(SettingDialog.reject)

        QMetaObject.connectSlotsByName(SettingDialog)
    # setupUi

    def retranslateUi(self, SettingDialog):
        SettingDialog.setWindowTitle(QCoreApplication.translate("SettingDialog", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.cameraLabel.setText(QCoreApplication.translate("SettingDialog", u"\u041a\u0430\u043c\u0435\u0440\u0430:", None))
        self.bodyPartLabel.setText(QCoreApplication.translate("SettingDialog", u"\u0427\u0430\u0441\u0442\u0438 \u0442\u0435\u043b\u0430:", None))
        self.headCheckBox.setText(QCoreApplication.translate("SettingDialog", u"\u0413\u043e\u043b\u043e\u0432\u0430", None))
        self.bodyCheckBox.setText(QCoreApplication.translate("SettingDialog", u"\u0422\u0443\u043b\u043e\u0432\u0438\u0449\u0435", None))
        self.armGroupBox.setTitle(QCoreApplication.translate("SettingDialog", u"\u0420\u0443\u043a\u0438", None))
        self.leftArmCheckBox.setText(QCoreApplication.translate("SettingDialog", u"\u041b\u0435\u0432\u0430\u044f \u0440\u0443\u043a\u0430", None))
        self.rightArmCheckBox.setText(QCoreApplication.translate("SettingDialog", u"\u041f\u0440\u0430\u0432\u0430\u044f \u0440\u0443\u043a\u0430", None))
        self.legGroupBox.setTitle(QCoreApplication.translate("SettingDialog", u"\u041d\u043e\u0433\u0438", None))
        self.leftLegCheckBox.setText(QCoreApplication.translate("SettingDialog", u"\u041b\u0435\u0432\u0430\u044f \u043d\u043e\u0433\u0430", None))
        self.rightLegCheckBox.setText(QCoreApplication.translate("SettingDialog", u"\u041f\u0440\u0430\u0432\u0430\u044f \u043d\u043e\u0433\u0430", None))
    # retranslateUi
