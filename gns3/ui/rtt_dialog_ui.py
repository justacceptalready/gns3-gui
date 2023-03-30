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
    
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.uiRTTTextLabel = QtWidgets.QLabel(self.tab)
        self.uiRTTTextLabel.setOpenExternalLinks(True)
        self.uiRTTTextLabel.setObjectName("uiRTTTextLabel")
        self.horizontalLayout.addWidget(self.uiRTTTextLabel)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
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
        self.uiRTTTextLabel.setText(_translate("RTTDialog", "Menu Work In Progress."))  
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("RTTDialog", "Round Trip Time"))
    
from . import resources_rc
