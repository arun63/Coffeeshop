#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'homedelivery.ui'
#
# Created: Thu Nov 28 21:27:34 2013
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog3(object):
    def setupUi(self, Dialog3):
        Dialog3.setObjectName("Dialog3")
        Dialog3.resize(834, 569)
        self.commandLinkButton = QtGui.QCommandLinkButton(Dialog3)
        self.commandLinkButton.setGeometry(QtCore.QRect(0, 0, 185, 41))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.label = QtGui.QLabel(Dialog3)
        self.label.setGeometry(QtCore.QRect(50, 70, 251, 31))
        self.label.setAutoFillBackground(False)
        self.label.setObjectName("label")
        self.textEdit = QtGui.QTextEdit(Dialog3)
        self.textEdit.setGeometry(QtCore.QRect(250, 330, 181, 51))
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtGui.QLabel(Dialog3)
        self.label_2.setGeometry(QtCore.QRect(60, 340, 171, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(Dialog3)
        self.label_3.setGeometry(QtCore.QRect(120, 380, 61, 16))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtGui.QPushButton(Dialog3)
        self.pushButton.setGeometry(QtCore.QRect(110, 460, 101, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtGui.QPushButton(Dialog3)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 470, 101, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.comboBox = QtGui.QComboBox(Dialog3)
        self.comboBox.setGeometry(QtCore.QRect(510, 60, 181, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.tableWidget = QtGui.QTableWidget(Dialog3)
        self.tableWidget.setGeometry(QtCore.QRect(40, 120, 421, 181))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(5)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        self.comboBox_3 = QtGui.QComboBox(Dialog3)
        self.comboBox_3.setGeometry(QtCore.QRect(510, 140, 181, 31))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_4 = QtGui.QComboBox(Dialog3)
        self.comboBox_4.setGeometry(QtCore.QRect(510, 210, 181, 31))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_5 = QtGui.QComboBox(Dialog3)
        self.comboBox_5.setGeometry(QtCore.QRect(510, 290, 181, 31))
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_6 = QtGui.QComboBox(Dialog3)
        self.comboBox_6.setGeometry(QtCore.QRect(510, 370, 181, 31))
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_7 = QtGui.QComboBox(Dialog3)
        self.comboBox_7.setGeometry(QtCore.QRect(510, 450, 181, 31))
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_8 = QtGui.QComboBox(Dialog3)
        self.comboBox_8.setGeometry(QtCore.QRect(720, 60, 91, 31))
        self.comboBox_8.setObjectName("comboBox_8")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.label_4 = QtGui.QLabel(Dialog3)
        self.label_4.setGeometry(QtCore.QRect(720, 40, 62, 17))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtGui.QLabel(Dialog3)
        self.label_5.setGeometry(QtCore.QRect(510, 40, 62, 17))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtGui.QLabel(Dialog3)
        self.label_6.setGeometry(QtCore.QRect(510, 120, 81, 17))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtGui.QLabel(Dialog3)
        self.label_7.setGeometry(QtCore.QRect(510, 190, 81, 17))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtGui.QLabel(Dialog3)
        self.label_8.setGeometry(QtCore.QRect(510, 270, 62, 17))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtGui.QLabel(Dialog3)
        self.label_9.setGeometry(QtCore.QRect(510, 350, 62, 17))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtGui.QLabel(Dialog3)
        self.label_10.setGeometry(QtCore.QRect(510, 430, 101, 17))
        self.label_10.setObjectName("label_10")
        self.comboBox_2 = QtGui.QComboBox(Dialog3)
        self.comboBox_2.setGeometry(QtCore.QRect(720, 140, 89, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_9 = QtGui.QComboBox(Dialog3)
        self.comboBox_9.setGeometry(QtCore.QRect(720, 210, 89, 31))
        self.comboBox_9.setObjectName("comboBox_9")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_10 = QtGui.QComboBox(Dialog3)
        self.comboBox_10.setGeometry(QtCore.QRect(720, 290, 89, 31))
        self.comboBox_10.setObjectName("comboBox_10")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_11 = QtGui.QComboBox(Dialog3)
        self.comboBox_11.setGeometry(QtCore.QRect(720, 370, 89, 31))
        self.comboBox_11.setObjectName("comboBox_11")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_12 = QtGui.QComboBox(Dialog3)
        self.comboBox_12.setGeometry(QtCore.QRect(720, 450, 89, 31))
        self.comboBox_12.setObjectName("comboBox_12")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")

        self.retranslateUi(Dialog3)
        QtCore.QMetaObject.connectSlotsByName(Dialog3)

    def retranslateUi(self, Dialog3):
        Dialog3.setWindowTitle(QtGui.QApplication.translate("Dialog3", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.commandLinkButton.setText(QtGui.QApplication.translate("Dialog3", "Home", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog3", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; font-style:italic; text-decoration: underline;\">Home Delivery Orders</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog3", "<html><head/><body><p><span style=\" font-size:18pt;\">Total Amount</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog3", "<html><head/><body><p>(Rupees)</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Dialog3", "Order Now", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("Dialog3", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(0, QtGui.QApplication.translate("Dialog3", "Chicken_65_Sandwich", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(1, QtGui.QApplication.translate("Dialog3", "Tandoori_Paneer_Sandwich", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(2, QtGui.QApplication.translate("Dialog3", "Tandoori_Chicken_Sandwich", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(3, QtGui.QApplication.translate("Dialog3", "Cheesy_Veg_Croissant", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(4, QtGui.QApplication.translate("Dialog3", "Smoked_Chicken_Sandwich", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(5, QtGui.QApplication.translate("Dialog3", "Spinach_N_Corn_Chesse_Sandwich", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(6, QtGui.QApplication.translate("Dialog3", "Tex_Mex_Veg_Cheese_Sandwich", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.verticalHeaderItem(0).setText(QtGui.QApplication.translate("Dialog3", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.verticalHeaderItem(1).setText(QtGui.QApplication.translate("Dialog3", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.verticalHeaderItem(2).setText(QtGui.QApplication.translate("Dialog3", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.verticalHeaderItem(3).setText(QtGui.QApplication.translate("Dialog3", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.verticalHeaderItem(4).setText(QtGui.QApplication.translate("Dialog3", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("Dialog3", "Item Name", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("Dialog3", "Each Cost", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("Dialog3", "Quantity", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(3).setText(QtGui.QApplication.translate("Dialog3", "Total cost", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.comboBox_3.setItemText(0, QtGui.QApplication.translate("Dialog3", "Hot_N_Spicy_Veg_Puff", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_3.setItemText(1, QtGui.QApplication.translate("Dialog3", "Hot_N_Spicy_Chicken_Puff", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_3.setItemText(2, QtGui.QApplication.translate("Dialog3", "Chilli_Cheese_Toastizza", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_3.setItemText(3, QtGui.QApplication.translate("Dialog3", "Cookie", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_3.setItemText(4, QtGui.QApplication.translate("Dialog3", "Veg_Samosa", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_4.setItemText(0, QtGui.QApplication.translate("Dialog3", "Chocolate_Fantasy_Cake", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_5.setItemText(0, QtGui.QApplication.translate("Dialog3", "ColdBeverage_VegSamosa", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_5.setItemText(1, QtGui.QApplication.translate("Dialog3", "ColdBeverage_ChilliChesseToastizza", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_5.setItemText(2, QtGui.QApplication.translate("Dialog3", "ColdBeverage_VegSandwich", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_5.setItemText(3, QtGui.QApplication.translate("Dialog3", "ColdBeverage_Non-VegSandwich", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_6.setItemText(0, QtGui.QApplication.translate("Dialog3", "Sizzle_Dazzle_Brownie", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_6.setItemText(1, QtGui.QApplication.translate("Dialog3", "Fruity_Blizz", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_6.setItemText(2, QtGui.QApplication.translate("Dialog3", "Choco-Hola", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_6.setItemText(3, QtGui.QApplication.translate("Dialog3", "Dark_Passion", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_6.setItemText(4, QtGui.QApplication.translate("Dialog3", "Vanilla_Icecream", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_6.setItemText(5, QtGui.QApplication.translate("Dialog3", "Chocolate_Icecream", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_7.setItemText(0, QtGui.QApplication.translate("Dialog3", "Black_Forest_Cup", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_7.setItemText(1, QtGui.QApplication.translate("Dialog3", "Nutty_Fudge_Brownie", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_7.setItemText(2, QtGui.QApplication.translate("Dialog3", "Chocolate_Fantasy", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_7.setItemText(3, QtGui.QApplication.translate("Dialog3", "Cafe_Coffee_Day_Indulgence", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_8.setItemText(0, QtGui.QApplication.translate("Dialog3", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_8.setItemText(1, QtGui.QApplication.translate("Dialog3", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_8.setItemText(2, QtGui.QApplication.translate("Dialog3", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_8.setItemText(3, QtGui.QApplication.translate("Dialog3", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_8.setItemText(4, QtGui.QApplication.translate("Dialog3", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog3", "Quantity", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog3", "Big_eats", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Dialog3", "Small_eats", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Dialog3", "Cakeaway", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Dialog3", "Combo", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("Dialog3", "Sundaes", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("Dialog3", "Sweet_Treats", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_2.setItemText(0, QtGui.QApplication.translate("Dialog3", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_2.setItemText(1, QtGui.QApplication.translate("Dialog3", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_2.setItemText(2, QtGui.QApplication.translate("Dialog3", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_2.setItemText(3, QtGui.QApplication.translate("Dialog3", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_2.setItemText(4, QtGui.QApplication.translate("Dialog3", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_9.setItemText(0, QtGui.QApplication.translate("Dialog3", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_9.setItemText(1, QtGui.QApplication.translate("Dialog3", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_9.setItemText(2, QtGui.QApplication.translate("Dialog3", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_9.setItemText(3, QtGui.QApplication.translate("Dialog3", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_9.setItemText(4, QtGui.QApplication.translate("Dialog3", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_10.setItemText(0, QtGui.QApplication.translate("Dialog3", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_10.setItemText(1, QtGui.QApplication.translate("Dialog3", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_10.setItemText(2, QtGui.QApplication.translate("Dialog3", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_10.setItemText(3, QtGui.QApplication.translate("Dialog3", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_10.setItemText(4, QtGui.QApplication.translate("Dialog3", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_11.setItemText(0, QtGui.QApplication.translate("Dialog3", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_11.setItemText(1, QtGui.QApplication.translate("Dialog3", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_11.setItemText(2, QtGui.QApplication.translate("Dialog3", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_11.setItemText(3, QtGui.QApplication.translate("Dialog3", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_11.setItemText(4, QtGui.QApplication.translate("Dialog3", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_12.setItemText(0, QtGui.QApplication.translate("Dialog3", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_12.setItemText(1, QtGui.QApplication.translate("Dialog3", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_12.setItemText(2, QtGui.QApplication.translate("Dialog3", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_12.setItemText(3, QtGui.QApplication.translate("Dialog3", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_12.setItemText(4, QtGui.QApplication.translate("Dialog3", "5", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog3 = QtGui.QDialog()
    ui = Ui_Dialog3()
    ui.setupUi(Dialog3)
    Dialog3.show()
    sys.exit(app.exec_())

