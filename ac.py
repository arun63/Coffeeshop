#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'alert_constumer.ui'
#
# Created: Thu Nov 28 20:23:58 2013
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog7(object):
    def setupUi(self, Dialog7):
        Dialog7.setObjectName("Dialog7")
        Dialog7.resize(366, 182)
        self.label = QtGui.QLabel(Dialog7)
        self.label.setGeometry(QtCore.QRect(80, 40, 211, 20))
        self.label.setObjectName("label")
        self.pushButton = QtGui.QPushButton(Dialog7)
        self.pushButton.setGeometry(QtCore.QRect(120, 80, 141, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog7)
        QtCore.QMetaObject.connectSlotsByName(Dialog7)

    def retranslateUi(self, Dialog7):
        Dialog7.setWindowTitle(QtGui.QApplication.translate("Dialog7", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog7", "<html><head/><body><p><span style=\" font-size:10pt;\">Sorry , There is no such constumer.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Dialog7", "OK", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog7 = QtGui.QDialog()
    ui = Ui_Dialog7()
    ui.setupUi(Dialog7)
    Dialog7.show()
    sys.exit(app.exec_())

