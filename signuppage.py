#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup-page.ui'
#
# Created: Wed Nov 27 22:10:57 2013
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

class Ui_Dialog2(object):
    def setupUi(self, Dialog2):
        Dialog2.setObjectName(_fromUtf8("Dialog2"))
        Dialog2.resize(837, 574)
        Dialog2.setMouseTracking(False)
        self.textEdit = QtGui.QTextEdit(Dialog2)
        self.textEdit.setGeometry(QtCore.QRect(340, 100, 211, 31))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.radioButton = QtGui.QRadioButton(Dialog2)
        self.radioButton.setGeometry(QtCore.QRect(350, 160, 61, 17))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton_2 = QtGui.QRadioButton(Dialog2)
        self.radioButton_2.setGeometry(QtCore.QRect(430, 160, 82, 17))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.textEdit_2 = QtGui.QTextEdit(Dialog2)
        self.textEdit_2.setGeometry(QtCore.QRect(340, 200, 211, 31))
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.textEdit_3 = QtGui.QTextEdit(Dialog2)
        self.textEdit_3.setGeometry(QtCore.QRect(340, 260, 211, 31))
        self.textEdit_3.setObjectName(_fromUtf8("textEdit_3"))
        self.textEdit_4 = QtGui.QTextEdit(Dialog2)
        self.textEdit_4.setGeometry(QtCore.QRect(340, 310, 211, 31))
        self.textEdit_4.setObjectName(_fromUtf8("textEdit_4"))
        self.label = QtGui.QLabel(Dialog2)
        self.label.setGeometry(QtCore.QRect(270, 110, 46, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog2)
        self.label_2.setGeometry(QtCore.QRect(270, 160, 46, 13))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog2)
        self.label_3.setGeometry(QtCore.QRect(270, 210, 46, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Dialog2)
        self.label_4.setGeometry(QtCore.QRect(230, 270, 91, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Dialog2)
        self.label_5.setGeometry(QtCore.QRect(260, 320, 61, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.checkBox = QtGui.QCheckBox(Dialog2)
        self.checkBox.setGeometry(QtCore.QRect(170, 400, 191, 17))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.buttonBox = QtGui.QDialogButtonBox(Dialog2)
        self.buttonBox.setGeometry(QtCore.QRect(370, 460, 156, 23))
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label_6 = QtGui.QLabel(Dialog2)
        self.label_6.setGeometry(QtCore.QRect(380, 40, 81, 41))
        self.label_6.setObjectName(_fromUtf8("label_6"))

        self.retranslateUi(Dialog2)
        QtCore.QMetaObject.connectSlotsByName(Dialog2)

    def retranslateUi(self, Dialog2):
        Dialog2.setWindowTitle(_translate("Dialog2", "Dialog2", None))
        self.radioButton.setText(_translate("Dialog2", "Male", None))
        self.radioButton_2.setText(_translate("Dialog2", "Female", None))
        self.label.setText(_translate("Dialog2", "<html><head/><body><p><span style=\" font-size:10pt;\">Name</span></p></body></html>", None))
        self.label_2.setText(_translate("Dialog2", "<html><head/><body><p><span style=\" font-size:10pt;\">Gender</span></p></body></html>", None))
        self.label_3.setText(_translate("Dialog2", "<html><head/><body><p><span style=\" font-size:10pt;\">Country</span></p></body></html>", None))
        self.label_4.setText(_translate("Dialog2", "<html><head/><body><p><span style=\" font-size:10pt;\">New Username</span></p></body></html>", None))
        self.label_5.setText(_translate("Dialog2", "<html><head/><body><p><span style=\" font-size:10pt;\">Password</span></p></body></html>", None))
        self.checkBox.setText(_translate("Dialog2", "I agree the terms and conditions", None))
        self.label_6.setText(_translate("Dialog2", "<html><head/><body><p><span style=\" font-size:16pt;\">Signup</span></p></body></html>", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog2 = QtGui.QDialog()
    ui = Ui_Dialog2()
    ui.setupUi(Dialog2)
    Dialog2.show()
    sys.exit(app.exec_())

