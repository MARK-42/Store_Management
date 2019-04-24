# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'billGenerator.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BILL(object):
    def setupUi(self, BILL):
        import cx_Oracle
        import os
        self.con = cx_Oracle.connect('shivansh', '1234', cx_Oracle.makedsn('localhost', 1521, 'DBMS1'))
        self.cur = self.con.cursor()
        output = self.cur.var(str)
        print(self.cur.callproc("management.getAllProducts", [ output ]  ))
        BILL.setObjectName("BILL")
        BILL.resize(809, 580)
        self.centralwidget = QtWidgets.QWidget(BILL)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 30, 441, 91))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 150, 31, 51))
        self.label_2.setObjectName("label_2")
        self.itemComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.itemComboBox.setGeometry(QtCore.QRect(80, 160, 201, 31))
        self.itemComboBox.setObjectName("itemComboBox")

        self.itemComboBox.clear()
        self.itemComboBox.addItems(output.getvalue()[1:].split(';'))
        
        self.getDetailBtn = QtWidgets.QPushButton(self.centralwidget)
        self.getDetailBtn.setGeometry(QtCore.QRect(300, 160, 121, 31))
        self.getDetailBtn.setObjectName("getDetailBtn")
        self.getDetailBtn.clicked.connect(self.getDetails)

        self.AddItemBtn = QtWidgets.QPushButton(self.centralwidget)
        self.AddItemBtn.setGeometry(QtCore.QRect(640, 160, 121, 31))
        self.AddItemBtn.setObjectName("AddItemBtn")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 230, 161, 31))
        self.label_3.setObjectName("label_3")
        self.itmNamelbl = QtWidgets.QLabel(self.centralwidget)
        self.itmNamelbl.setGeometry(QtCore.QRect(230, 300, 91, 21))
        self.itmNamelbl.setObjectName("itmNamelbl")
        self.ItemPricelbl = QtWidgets.QLabel(self.centralwidget)
        self.ItemPricelbl.setGeometry(QtCore.QRect(390, 300, 111, 21))
        self.ItemPricelbl.setObjectName("ItemPricelbl")
        self.ItemQtLbl = QtWidgets.QLabel(self.centralwidget)
        self.ItemQtLbl.setGeometry(QtCore.QRect(580, 290, 111, 41))
        self.ItemQtLbl.setObjectName("ItemQtLbl")
        self.itemIdLbl = QtWidgets.QLabel(self.centralwidget)
        self.itemIdLbl.setGeometry(QtCore.QRect(100, 300, 55, 21))
        self.itemIdLbl.setObjectName("itemIdLbl")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(450, 160, 81, 31))
        self.label_8.setObjectName("label_8")
        self.quantitySpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.quantitySpinBox.setGeometry(QtCore.QRect(541, 161, 71, 31))
        self.quantitySpinBox.setObjectName("quantitySpinBox")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(30, 360, 131, 41))
        self.label_9.setObjectName("label_9")
        self.custIdTextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.custIdTextEdit.setGeometry(QtCore.QRect(180, 360, 161, 41))
        self.custIdTextEdit.setObjectName("custIdTextEdit")
        self.custRegLbl = QtWidgets.QLabel(self.centralwidget)
        self.custRegLbl.setGeometry(QtCore.QRect(580, 350, 191, 51))
        self.custRegLbl.setObjectName("custRegLbl")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(300, 470, 91, 41))
        self.label_11.setObjectName("label_11")
        self.totalAmtLbl = QtWidgets.QLabel(self.centralwidget)
        self.totalAmtLbl.setGeometry(QtCore.QRect(410, 470, 101, 41))
        self.totalAmtLbl.setObjectName("totalAmtLbl")
        self.GenBillBtn = QtWidgets.QPushButton(self.centralwidget)
        self.GenBillBtn.setGeometry(QtCore.QRect(402, 357, 121, 41))
        self.GenBillBtn.setObjectName("GenBillBtn")
        BILL.setCentralWidget(self.centralwidget)

        self.retranslateUi(BILL)
        QtCore.QMetaObject.connectSlotsByName(BILL)

    def getDetails(self):
        import cx_Oracle
        import os
        self.con = cx_Oracle.connect('shivansh', '1234', cx_Oracle.makedsn('localhost', 1521, 'DBMS1'))
        self.cur = self.con.cursor()
        output  = self.cur.var(str)
        result = self.cur.var(str,100)
        print(self.itemComboBox.currentText().split(',')[1], 
            self.itemComboBox.currentText().split(',')[2])
        print(self.cur.callproc("management.searchProductID", (self.itemComboBox.currentText().split(',')[1], 
            self.itemComboBox.currentText().split(',')[2], output, result )))
        print(output)
        print(result)
        results = result.split(',')

    def retranslateUi(self, BILL):
        _translate = QtCore.QCoreApplication.translate
        BILL.setWindowTitle(_translate("BILL", "MainWindow"))
        self.label.setText(_translate("BILL", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">BILLER</span></p></body></html>"))
        self.label_2.setText(_translate("BILL", "Item "))
        self.getDetailBtn.setText(_translate("BILL", "Get Details"))
        self.AddItemBtn.setText(_translate("BILL", "Add"))
        self.label_3.setText(_translate("BILL", "<html><head/><body><p><span style=\" font-size:14pt;\">ITEM DETAIL</span></p></body></html>"))
        self.itmNamelbl.setText(_translate("BILL", "NAME : SOAP"))
        self.ItemPricelbl.setText(_translate("BILL", " RS.20 PER UNIT"))
        self.ItemQtLbl.setText(_translate("BILL", "QUANTITY : 320"))
        self.itemIdLbl.setText(_translate("BILL", "ID : A101"))
        self.label_8.setText(_translate("BILL", "QUANTITY"))
        self.label_9.setText(_translate("BILL", "CUSTOMER ID"))
        self.custRegLbl.setText(_translate("BILL", "New Customer ? Register Here !!"))
        self.label_11.setText(_translate("BILL", "Total Amount"))
        self.totalAmtLbl.setText(_translate("BILL", "Rs. 2400"))
        self.GenBillBtn.setText(_translate("BILL", "Generate Bill"))

if __name__ == '__main__':
    app = QtGui.QApplication([])
    gui = Ui_BILL()
    gui.show()
    app.exec_()