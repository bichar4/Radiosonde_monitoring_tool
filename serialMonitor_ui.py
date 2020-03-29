# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'serialMonitor.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Serial(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(502, 547)
        self.SendButton = QtWidgets.QPushButton(Dialog)
        self.SendButton.setGeometry(QtCore.QRect(400, 20, 89, 25))
        self.SendButton.setObjectName("SendButton")
        self.lineInput = QtWidgets.QLineEdit(Dialog)
        self.lineInput.setGeometry(QtCore.QRect(20, 20, 351, 25))
        self.lineInput.setObjectName("lineInput")
        self.SerialOutput = QtWidgets.QTextEdit(Dialog)
        self.SerialOutput.setGeometry(QtCore.QRect(20, 70, 351, 401))
        self.SerialOutput.setObjectName("SerialOutput")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.SendButton.setText(_translate("Dialog", "Send"))
