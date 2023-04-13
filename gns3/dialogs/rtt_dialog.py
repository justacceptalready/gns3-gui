# -*- coding: utf-8 -*-
#
# Copyright (C) 2014 GNS3 Technologies Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from ..qt import QtWidgets
from ..version import __version__
from ..ui.rtt_dialog_ui import Ui_RTTDialog
from gns3.qt import QtCore, QtGui, QtWidgets
from gns3.dialogs.symbol_selection_dialog import SymbolSelectionDialog
from ..dialogs.node_properties_dialog import ConfigurationError
from gns3.controller import Controller
from gns3.node import Node


class RTTDialog(QtWidgets.QDialog, Ui_RTTDialog):

    """
    RTT dialog.
    """

    def __init__(self, parent):

        super().__init__(parent)
        self.setupUi(self)
        self._node = None
        self._ports = []
        self._interfaces = []
        self._connections = []

        # dynamically add the current version number
        text = self.uiRTTTextLabel.text()
        text = text.replace("%VERSION%", __version__)
        self.uiRTTTextLabel.setText(text)

        # connect  slots
        #self.uiComboBox.currentIndexChanged.connect(self._SelectedSlot)
        self.uiListWidget.itemSelectionChanged.connect(self._ChangedSlot)
        #self.uiAddPushButton.clicked.connect(self._AddSlot)
        #self.uiAddAllPushButton.clicked.connect(self._AddAllSlot)
        #self.uiRefreshPushButton.clicked.connect(self._RefreshSlot)
        self.uiDeletePushButton.clicked.connect(self._DeleteSlot)

        self.uiAddConnectionPushButton.clicked.connect(self._AddConnectionSlot)


    def _SelectedSlot(self, index):
            """
            Loads the selected  interface.

            :param index: ignored
            """

            #self.uiLineEdit.setText(self.uiComboBox.currentText())
    
    def _ChangedSlot(self):
        """
        Enables the use of the delete button.
        """

        item = self.uiListWidget.currentItem()
        if item:
            self.uiDeletePushButton.setEnabled(True)
            #self.uiLineEdit.setText(item.text())
        else:
            self.uiDeletePushButton.setEnabled(False)

    #def _AddSlot(self, interface=None):
    #    """
    #    Adds a new  interface.
    #    """
#
    #    if not interface:
    #        interface = self.uiLineEdit.text()
    #    if interface:
    #        for port in self._ports:
    #            if port["name"] == interface and port["type"] == "tap":
    #                return
    #        self.uiListWidget.addItem(interface)
    #        self._ports.append({"name": interface,
    #                            "port_number": len(self._ports),
    #                            "type": "tap",
    #                            "interface": interface})
    #        index = self.uiComboBox.findText(interface)
    #        if index != -1:
    #            self.uiComboBox.removeItem(index)
    #    print(self._ports)

    def _AddConnectionSlot(self, name1=None, name2=None, distance=None, speed=None):
        if not name1:
            name1 = self.uiNameLineEdit.text()
        if not name2:
            name2 = self.uiNameLine2Edit.text()
        if not distance:
            distance = self.uiDistanceLineEdit.text()
        if not speed:
            speed = self.uiSpeedLineEdit.text()

        if name1 and name2:
            for connection in self._connections:
                if connection["name 1"] == name1 and connection["name 2"] == name2:
                    return
                if connection["name 1"] == name2 and connection["name 2"] == name1:
                    return
                if connection["name 1"] == name1 or connection["name 1"] == name2:
                    return

        if name1 and name2 and distance and speed:
            self.uiListWidget.addItem(name1 + "\t" + name2 + "\t" + distance + "\t"  + speed)
            self._connections.append({"name 1": name1,
                                "name 2": name2,
                                "distance": distance,
                                "speed": speed})
        print(self._connections)




    #def _AddAllSlot(self):
    #    """
    #    Adds all  interfaces
    #    """
#
    #    for index in range(0, self.uiComboBox.count()):
    #        interface = self.uiComboBox.itemText(index)
    #        #self._AddSlot(interface)

    #def _RefreshSlot(self):
    #    """
    #    Refresh all  interfaces.
    #    """
#
    #    if self._node:
    #        self._node.update({}, force=True)
    #        self._node.updated_signal.connect(self._refreshInterfaces)

    def _DeleteSlot(self):
        """
        Deletes a  interface.
        """


        if self._node:
            for item in self.uiListWidget.selectedItems():
                interface = item.text()
                # check we can delete that interface
                for node_port in self._node.ports():
                    if node_port.name() == interface and not node_port.isFree():
                        QtWidgets.QMessageBox.critical(self, self._node.name(), "A link is connected to {}, please remove it first".format(interface))
                        return

        for item in self.uiListWidget.selectedItems():
            interface = item.text()
            for port in self._ports.copy():
                if port["name"] == interface:
                    self._ports.remove(port)
                    self.uiListWidget.takeItem(self.uiListWidget.row(item))
                    for interface in self._interfaces:
                        if interface["name"] == port["name"] and interface["type"] == "tap":
                            print()
                            #self.uiComboBox.addItem(interface["name"])
                    break

