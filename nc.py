#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newconstumer.ui'
#
# Created: Thu Nov 28 18:51:25 2013
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog4(object):
    def setupUi(self, Dialog4):
        Dialog4.setObjectName("Dialog4")
        Dialog4.resize(834, 580)
        self.label = QtGui.QLabel(Dialog4)
        self.label.setGeometry(QtCore.QRect(340, 60, 181, 21))
        self.label.setObjectName("label")
        self.textEdit = QtGui.QTextEdit(Dialog4)
        self.textEdit.setGeometry(QtCore.QRect(340, 130, 201, 41))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtGui.QTextEdit(Dialog4)
        self.textEdit_2.setGeometry(QtCore.QRect(340, 200, 201, 41))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtGui.QTextEdit(Dialog4)
        self.textEdit_3.setGeometry(QtCore.QRect(340, 270, 201, 41))
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_2 = QtGui.QLabel(Dialog4)
        self.label_2.setGeometry(QtCore.QRect(240, 140, 91, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(Dialog4)
        self.label_3.setGeometry(QtCore.QRect(280, 210, 41, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtGui.QLabel(Dialog4)
        self.label_4.setGeometry(QtCore.QRect(270, 280, 61, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtGui.QLabel(Dialog4)
        self.label_5.setGeometry(QtCore.QRect(270, 340, 62, 17))
        self.label_5.setObjectName("label_5")
        self.textEdit_4 = QtGui.QTextEdit(Dialog4)
        self.textEdit_4.setGeometry(QtCore.QRect(340, 330, 201, 41))
        self.textEdit_4.setObjectName("textEdit_4")
        self.label_6 = QtGui.QLabel(Dialog4)
        self.label_6.setGeometry(QtCore.QRect(270, 410, 62, 17))
        self.label_6.setObjectName("label_6")
        self.textEdit_5 = QtGui.QTextEdit(Dialog4)
        self.textEdit_5.setGeometry(QtCore.QRect(340, 400, 201, 41))
        self.textEdit_5.setObjectName("textEdit_5")
        self.pushButton = QtGui.QPushButton(Dialog4)
        self.pushButton.setGeometry(QtCore.QRect(330, 490, 93, 27))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtGui.QPushButton(Dialog4)
        self.pushButton_2.setGeometry(QtCore.QRect(460, 490, 93, 27))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog4)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.textEdit_5.clear)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.textEdit_4.clear)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.textEdit_3.clear)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.textEdit_2.clear)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.textEdit.clear)
        QtCore.QMetaObject.connectSlotsByName(Dialog4)

    def retranslateUi(self, Dialog4):
        Dialog4.setWindowTitle(QtGui.QApplication.translate("Dialog4", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog4", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">New Constumer</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog4", "<html><head/><body><p><span style=\" font-size:9pt;\">Phone Number</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog4", "<html><head/><body><p><span style=\" font-size:9pt;\">Name</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Address1</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog4", "Address2", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Dialog4", "Address3", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Dialog4", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("Dialog4", "OK", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog4 = QtGui.QDialog()
    ui = Ui_Dialog4()
    ui.setupUi(Dialog4)
    Dialog4.show()
    sys.exit(app.exec_())

