#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'phonenum.ui'
#
# Created: Thu Nov 28 19:32:36 2013
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog6(object):
    def setupUi(self, Dialog6):
        Dialog6.setObjectName("Dialog6")
        Dialog6.resize(835, 569)
        self.label = QtGui.QLabel(Dialog6)
        self.label.setGeometry(QtCore.QRect(70, 10, 121, 31))
        self.label.setObjectName("label")
        self.pushButton = QtGui.QPushButton(Dialog6)
        self.pushButton.setGeometry(QtCore.QRect(740, 10, 91, 31))
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtGui.QTextEdit(Dialog6)
        self.textEdit.setGeometry(QtCore.QRect(410, 240, 291, 41))
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtGui.QLabel(Dialog6)
        self.label_2.setGeometry(QtCore.QRect(450, 180, 211, 41))
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtGui.QPushButton(Dialog6)
        self.pushButton_2.setGeometry(QtCore.QRect(520, 310, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtGui.QLabel(Dialog6)
        self.label_3.setGeometry(QtCore.QRect(100, 130, 201, 281))
        self.label_3.setObjectName("label_3")
        self.pushButton_3 = QtGui.QPushButton(Dialog6)
        self.pushButton_3.setGeometry(QtCore.QRect(480, 410, 151, 27))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Dialog6)
        QtCore.QMetaObject.connectSlotsByName(Dialog6)

    def retranslateUi(self, Dialog6):
        Dialog6.setWindowTitle(QtGui.QApplication.translate("Dialog6", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog6", "<html><head/><body><p><span style=\" font-size:16pt; font-style:italic;\">Hello Staff</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Dialog6", "Log out", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog6", "<html><head/><body><p><span style=\" font-size:14pt;\">Enter Phone Number</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("Dialog6", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog6", "<html><head/><body><p><img src=\":/resources/Coffeeimage/images-3.jpg\"/></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("Dialog6", "New Customer", None, QtGui.QApplication.UnicodeUTF8))

import logo_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog6 = QtGui.QDialog()
    ui = Ui_Dialog6()
    ui.setupUi(Dialog6)
    Dialog6.show()
    sys.exit(app.exec_())

