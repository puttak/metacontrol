# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Felipe\PycharmProjects\metacontrol\gui\views\ui_files\choleskydialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(900, 364)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setMinimumSize(QtCore.QSize(300, 0))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.modifyLabel = QtWidgets.QLabel(self.groupBox_2)
        self.modifyLabel.setText("")
        self.modifyLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.modifyLabel.setObjectName("modifyLabel")
        self.gridLayout_3.addWidget(self.modifyLabel, 1, 0, 1, 1)
        self.setPushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.setPushButton.setObjectName("setPushButton")
        self.gridLayout_3.addWidget(self.setPushButton, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 2, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.originalMatrixTableView = QtWidgets.QTableView(self.groupBox)
        self.originalMatrixTableView.setObjectName("originalMatrixTableView")
        self.gridLayout_2.addWidget(self.originalMatrixTableView, 1, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.groupBox)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 0, 1, 2, 1)
        self.modifiedMatrixTableView = QtWidgets.QTableView(self.groupBox)
        self.modifiedMatrixTableView.setObjectName("modifiedMatrixTableView")
        self.gridLayout_2.addWidget(self.modifiedMatrixTableView, 1, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 4, 1, 1)
        self.errorMatrixTableView = QtWidgets.QTableView(self.groupBox)
        self.errorMatrixTableView.setObjectName("errorMatrixTableView")
        self.errorMatrixTableView.verticalHeader().setMinimumSectionSize(39)
        self.gridLayout_2.addWidget(self.errorMatrixTableView, 1, 4, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.groupBox)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_2.addWidget(self.line_2, 0, 3, 2, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.setPushButton.setText(_translate("Dialog", "Use the modified matrix"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p>Modified J<span style=\" vertical-align:sub;\">uu</span></p></body></html>"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p>Original J<span style=\" vertical-align:sub;\">uu</span></p></body></html>"))
        self.label_5.setText(_translate("Dialog", "Error"))

