#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'phonenum.ui'
#
# Created: Thu Nov 28 00:06:36 2013
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog5(object):
    def setupUi(self, Dialog5):
        Dialog5.setObjectName(_fromUtf8("Dialog5"))
        Dialog5.resize(835, 569)
        self.pushButton = QtGui.QPushButton(Dialog5)
        self.pushButton.setGeometry(QtCore.QRect(740, 10, 91, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.textEdit = QtGui.QTextEdit(Dialog5)
        self.textEdit.setGeometry(QtCore.QRect(270, 160, 291, 41))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.label_2 = QtGui.QLabel(Dialog5)
        self.label_2.setGeometry(QtCore.QRect(320, 110, 211, 41))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton_2 = QtGui.QPushButton(Dialog5)
        self.pushButton_2.setGeometry(QtCore.QRect(370, 220, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

        self.retranslateUi(Dialog5)
        QtCore.QMetaObject.connectSlotsByName(Dialog5)

    def retranslateUi(self, Dialog5):
        Dialog5.setWindowTitle(_translate("Dialog5", "Dialog", None))
        self.pushButton.setText(_translate("Dialog5", "Log out", None))
        self.label_2.setText(_translate("Dialog5", "<html><head/><body><p><span style=\" font-size:14pt;\">Enter Phone Number</span></p></body></html>", None))
        self.pushButton_2.setText(_translate("Dialog5", "OK", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog5 = QtGui.QDialog()
    ui = Ui_Dialog5()
    ui.setupUi(Dialog5)
    Dialog5.show()
    sys.exit(app.exec_())

