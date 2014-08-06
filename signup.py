#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup.ui'
#
# Created: Thu Nov 28 20:21:35 2013
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog1(object):
    def setupUi(self, Dialog1):
        Dialog1.setObjectName("Dialog1")
        Dialog1.resize(837, 570)
        self.textEdit = QtGui.QTextEdit(Dialog1)
        self.textEdit.setGeometry(QtCore.QRect(370, 260, 201, 31))
        self.textEdit.setObjectName("textEdit")
        self.label = QtGui.QLabel(Dialog1)
        self.label.setGeometry(QtCore.QRect(280, 260, 81, 21))
        self.label.setObjectName("label")
        self.textEdit_2 = QtGui.QTextEdit(Dialog1)
        self.textEdit_2.setGeometry(QtCore.QRect(370, 330, 191, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_2 = QtGui.QLabel(Dialog1)
        self.label_2.setGeometry(QtCore.QRect(280, 340, 71, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(Dialog1)
        self.label_3.setGeometry(QtCore.QRect(270, 40, 321, 151))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtGui.QPushButton(Dialog1)
        self.pushButton.setGeometry(QtCore.QRect(390, 390, 161, 31))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog1)
        QtCore.QMetaObject.connectSlotsByName(Dialog1)

    def retranslateUi(self, Dialog1):
        Dialog1.setWindowTitle(QtGui.QApplication.translate("Dialog1", "Dialog1", None, QtGui.QApplication.UnicodeUTF8))
        self.textEdit.setHtml(QtGui.QApplication.translate("Dialog1", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\"><br /></span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog1", "<html><head/><body><p><span style=\" font-weight:600;\">Username</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog1", "<html><head/><body><p><span style=\" font-weight:600;\">Password</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog1", "<html><head/><body><p><img src=\":/resources/Coffeeimage/images.jpg\"/></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Dialog1", "Login", None, QtGui.QApplication.UnicodeUTF8))

import Photos_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog1 = QtGui.QDialog()
    ui = Ui_Dialog1()
    ui.setupUi(Dialog1)
    Dialog1.show()
    sys.exit(app.exec_())

