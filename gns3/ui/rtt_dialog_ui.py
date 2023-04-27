# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/grossmj/PycharmProjects/gns3-gui/gns3/ui/RTT_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RTTDialog(object):
    def setupUi(self, RTTDialog):
        RTTDialog.setObjectName("RTTDialog")
        RTTDialog.setWindowModality(QtCore.Qt.WindowModal)
        RTTDialog.resize(465, 272)
        self.gridLayout_2 = QtWidgets.QGridLayout(RTTDialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(RTTDialog)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")

        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.uiCalculatePushButton = QtWidgets.QPushButton(self.tab)
        self.uiCalculatePushButton.setObjectName("uiCalculatePushButton")
        self.gridLayout.addWidget(self.uiCalculatePushButton, 1, 4, 1, 1)
        #self.uiDeletePushButton = QtWidgets.QPushButton(self.tab)
        #self.uiDeletePushButton.setEnabled(False)
        #self.uiDeletePushButton.setObjectName("uiDeletePushButton")
        #self.gridLayout.addWidget(self.uiDeletePushButton, 1, 5, 1, 1)
        self.uiListWidget = QtWidgets.QListWidget(self.tab)
        self.uiListWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.uiListWidget.setObjectName("uiListWidget")
        self.gridLayout.addWidget(self.uiListWidget, 2, 0, 1, 6)

        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")
        self.gridLayout3 = QtWidgets.QGridLayout(self.tab2)
        self.gridLayout3.setContentsMargins(10, 10, 10, 10)
        self.gridLayout3.setObjectName("gridLayout3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.uiNameLabel = QtWidgets.QLabel(self.tab2)
        self.uiNameLabel.setObjectName("uiNameLabel")
        self.gridLayout3.addWidget(self.uiNameLabel, 0, 0, 1, 1)
        self.uiNameLineEdit = QtWidgets.QLineEdit(self.tab2)
        self.uiNameLineEdit.setObjectName("uiNameLineEdit")
        self.gridLayout3.addWidget(self.uiNameLineEdit, 0, 2, 1, 1)
        self.uiNameLineEdit.raise_()

        self.uiName2Label = QtWidgets.QLabel(self.tab2)
        self.uiName2Label.setObjectName("uiName2Label")
        self.gridLayout3.addWidget(self.uiName2Label, 0, 0, 2, 1)
        self.uiNameLine2Edit = QtWidgets.QLineEdit(self.tab2)
        self.uiNameLine2Edit.setObjectName("uiNameLine2Edit")
        self.gridLayout3.addWidget(self.uiNameLine2Edit, 0, 2, 2, 1)
        self.uiNameLine2Edit.raise_()

        self.uiDistanceLabel = QtWidgets.QLabel(self.tab2)
        self.uiDistanceLabel.setObjectName("uiDistanceLabel")
        self.gridLayout3.addWidget(self.uiDistanceLabel, 0, 0, 3, 1)
        self.uiDistanceLineEdit = QtWidgets.QLineEdit(self.tab2)
        self.uiDistanceLineEdit.setObjectName("uiDistanceLineEdit")
        self.gridLayout3.addWidget(self.uiDistanceLineEdit, 0, 2, 3, 1)
        self.uiDistanceLineEdit.raise_()

        self.uiSpeedLabel = QtWidgets.QLabel(self.tab2)
        self.uiSpeedLabel.setObjectName("uiSpeedLabel")
        self.gridLayout3.addWidget(self.uiSpeedLabel, 0, 0, 4, 1)
        self.uiSpeedLineEdit = QtWidgets.QLineEdit(self.tab2)
        self.uiSpeedLineEdit.setObjectName("uiSpeedLineEdit")
        self.gridLayout3.addWidget(self.uiSpeedLineEdit, 0, 2, 4, 1)
        self.uiSpeedLineEdit.raise_()

        self.uiAddConnectionPushButton = QtWidgets.QPushButton(self.tab)
        self.uiAddConnectionPushButton.setObjectName("uiAddConnectionPushButton")
        self.gridLayout3.addWidget(self.uiAddConnectionPushButton, 0, 2, 5, 1)
    
        self.uiRTTTextLabel = QtWidgets.QLabel(self.tab)
        self.uiRTTTextLabel.setOpenExternalLinks(True)
        self.uiRTTTextLabel.setObjectName("uiRTTTextLabel")
        self.horizontalLayout.addWidget(self.uiRTTTextLabel)
        
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tabWidget.addTab(self.tab2, "")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(RTTDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_2.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(RTTDialog)
        self.tabWidget.setCurrentIndex(0)
        self.buttonBox.accepted.connect(RTTDialog.accept)
        self.buttonBox.rejected.connect(RTTDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(RTTDialog)

    def retranslateUi(self, RTTDialog):
        _translate = QtCore.QCoreApplication.translate
        RTTDialog.setWindowTitle(_translate("RTTDialog", "Calculate"))
        self.uiRTTTextLabel.setText(_translate("RTTDialog", "Node 1\tNode 2\tDistance (m)\tSpeed (ms)"))  
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("RTTDialog", "Round Trip Time"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), _translate("RTTDialog", "Add Connection"))


        self.uiCalculatePushButton.setText(_translate("RTTDialog", "&Calculate"))
        #self.uiDeletePushButton.setText(_translate("RTTDialog", "&Delete"))
        self.uiListWidget.setSortingEnabled(True)

        self.uiNameLabel.setText(_translate("RTTDialog", "Node 1 Name:"))
        self.uiName2Label.setText(_translate("RTTDialog", "Node 2 Name:"))
        self.uiDistanceLabel.setText(_translate("RTTDialog", "Distance:"))
        self.uiSpeedLabel.setText(_translate("RTTDialog", "Speed:"))
        self.uiAddConnectionPushButton.setText(_translate("RTTDialog", "&Add"))

from . import resources_rc
