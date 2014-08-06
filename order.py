#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'order.ui'
#
# Created: Thu Nov 28 21:43:39 2013
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog8(object):
    def setupUi(self, Dialog8):
        Dialog8.setObjectName("Dialog8")
        Dialog8.resize(366, 153)
        self.label = QtGui.QLabel(Dialog8)
        self.label.setGeometry(QtCore.QRect(110, 40, 151, 20))
        self.label.setObjectName("label")
        self.pushButton = QtGui.QPushButton(Dialog8)
        self.pushButton.setGeometry(QtCore.QRect(80, 90, 93, 27))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtGui.QPushButton(Dialog8)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 90, 93, 27))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog8)
        QtCore.QMetaObject.connectSlotsByName(Dialog8)

    def retranslateUi(self, Dialog8):
        Dialog8.setWindowTitle(QtGui.QApplication.translate("Dialog8", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog8", "Order has been placed", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Dialog8", "Print", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("Dialog8", "Close", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog8 = QtGui.QDialog()
    ui = Ui_Dialog8()
    ui.setupUi(Dialog8)
    Dialog8.show()
    sys.exit(app.exec_())

