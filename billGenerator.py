# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'billGenerator.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem
from customer import Ui_Customer


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

        


        self.quantitySpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.quantitySpinBox.setGeometry(QtCore.QRect(541, 161, 71, 31))
        self.quantitySpinBox.setObjectName("quantitySpinBox")

        self.itemComboBox.clear()
        self.itemComboBox.addItems(output.getvalue()[1:].split(';'))

        self.getDetailBtn = QtWidgets.QPushButton(self.centralwidget)
        self.getDetailBtn.setGeometry(QtCore.QRect(300, 160, 121, 31))
        self.getDetailBtn.setObjectName("getDetailBtn")
        self.getDetailBtn.clicked.connect(self.getDetails)

        self.AddItemBtn = QtWidgets.QPushButton(self.centralwidget)
        self.AddItemBtn.setGeometry(QtCore.QRect(640, 160, 121, 31))
        self.AddItemBtn.setObjectName("AddItemBtn")
        self.AddItemBtn.clicked.connect(self.addItem)


        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 230, 161, 31))
        self.label_3.setObjectName("label_3")
        self.itmNamelbl = QtWidgets.QLabel(self.centralwidget)
        self.itmNamelbl.setGeometry(QtCore.QRect(250, 230, 121 , 21))
        self.itmNamelbl.setObjectName("itmNamelbl")
        self.ItemPricelbl = QtWidgets.QLabel(self.centralwidget)
        self.ItemPricelbl.setGeometry(QtCore.QRect(390, 230, 111, 21))
        self.ItemPricelbl.setObjectName("ItemPricelbl")
        self.ItemQtLbl = QtWidgets.QLabel(self.centralwidget)
        self.ItemQtLbl.setGeometry(QtCore.QRect(530, 220, 111, 41))
        self.ItemQtLbl.setObjectName("ItemQtLbl")
        self.itemIdLbl = QtWidgets.QLabel(self.centralwidget)
        self.itemIdLbl.setGeometry(QtCore.QRect(170, 230, 55, 21))
        self.itemIdLbl.setObjectName("itemIdLbl")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(450, 160, 81, 31))
        self.label_8.setObjectName("label_8")
         


        

        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(20, 500, 131, 41))
        self.label_9.setObjectName("label_9")
        self.custIdTextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.custIdTextEdit.setGeometry(QtCore.QRect(120, 500, 161, 31))
        self.custIdTextEdit.setObjectName("custIdTextEdit")
        self.custRegLbl = QtWidgets.QLabel(self.centralwidget)
        self.custRegLbl.setGeometry(QtCore.QRect(20, 550, 191, 21))
        self.custRegLbl.setObjectName("custRegLbl")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(350, 500, 91, 41))
        self.label_11.setObjectName("label_11")
        self.totalAmtLbl = QtWidgets.QLabel(self.centralwidget)
        self.totalAmtLbl.setGeometry(QtCore.QRect(450, 500, 101, 41))
        self.totalAmtLbl.setObjectName("totalAmtLbl")
        self.GenBillBtn = QtWidgets.QPushButton(self.centralwidget)
        self.GenBillBtn.setGeometry(QtCore.QRect(610, 500, 121, 41))
        self.GenBillBtn.setObjectName("GenBillBtn")

        self.GenBillBtn.clicked.connect(self.genBill)

        self.regBtn = QtWidgets.QPushButton(self.centralwidget)
        self.regBtn.setGeometry(QtCore.QRect(110, 550, 81, 23))
        self.regBtn.setObjectName("regBtn")
        self.regBtn.clicked.connect(self.newCust)

        self.Bill = QtWidgets.QTableWidget(self.centralwidget)
        self.Bill.setGeometry(QtCore.QRect(170, 270, 511, 192))
        self.Bill.setColumnCount(5)
        self.Bill.setObjectName("Bill")
        self.Bill.setRowCount(0)
        self.Bill.setHorizontalHeaderLabels(['S.No', 'ID', 'NAME', 'COST', 'QTY.'])
        BILL.setCentralWidget(self.centralwidget)
        self.totalQty = 0
        self.billList = []
        self.retranslateUi(BILL)
        QtCore.QMetaObject.connectSlotsByName(BILL)

    def newCust(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Customer()
        self.ui.setupUi(self.window)
        self.window.show()        

    def setData(self): 
        horHeaders = []
        for n, key in enumerate(sorted(self.data.keys())):
            horHeaders.append(key)
            for m, item in enumerate(self.data[key]):
                newitem = QTableWidgetItem(item)
                self.Bill.setItem(m, n, newitem)
        self.Bill.setHorizontalHeaderLabels(horHeaders)

    def addItem(self):
        if (self.quantitySpinBox.value() > int(self.ItemQtLbl.text()[11:]))  :
            print('Not enough items in stock')
            return

        if ( self.quantitySpinBox.value() > 0 ) :
            
            self.Bill.insertRow(self.Bill.rowCount())

            newitem = QTableWidgetItem(str(self.Bill.rowCount()))
           
            self.Bill.setItem(self.Bill.rowCount()-1, 0, newitem)
            newitem = QTableWidgetItem(str(self.results[0]))
            
            self.Bill.setItem(self.Bill.rowCount()-1, 1, newitem)
            newitem = QTableWidgetItem(str(self.results[1]))

            self.Bill.setItem(self.Bill.rowCount()-1, 2, newitem)
            newitem = QTableWidgetItem(str(self.results[3]))
            
            self.Bill.setItem(self.Bill.rowCount()-1, 3, newitem)
            newitem = QTableWidgetItem(str(self.quantitySpinBox.value()))
            self.totalQty += self.quantitySpinBox.value()

            self.billList.append( [ str(self.results[0]).split(',')[0], self.quantitySpinBox.value(),self.results[3]  ] )

            self.Bill.setItem(self.Bill.rowCount()-1, 4, newitem)

            self.Bill.resizeRowsToContents()
            self.totalAmtLbl.setText(str(int(self.totalAmtLbl.text()) + int(self.results[3])*self.quantitySpinBox.value() ))


    def genBill(self):
        import cx_Oracle
        import os
        from datetime import datetime

        self.con = cx_Oracle.connect('shivansh', '1234', cx_Oracle.makedsn('localhost', 1521, 'DBMS1'))
        self.cur = self.con.cursor()
        output  = self.cur.var(str)
        result = self.cur.var(str)      
        print(self.cur.callproc("management.generateBill", (self.custIdTextEdit.toPlainText(), 1, int(self.totalAmtLbl.text()), self.totalQty, "Cash", 
            str(datetime.now()).split(' ')[1], str(datetime.now()).split(' ')[0], output, result)))  
        for i in self.billList:
            self.cur.callproc("management.insertRegister", (i[0], result, i[1], i[2], output ))
            print(output)
        if (output.getvalue() == 'Insert Success'):
            self.Bill.setRowCount(0);


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
        self.results = result.getvalue().split(',')
        self.itmNamelbl.setText('NAME : ' + self.results[1])
        self.ItemPricelbl.setText('RS. ' + self.results[3] + ' PER UNIT')
        self.ItemQtLbl.setText('QUANTITY : ' + self.results[4])
        self.itemIdLbl.setText('ID : ' + self.results[0])

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
        self.custRegLbl.setText(_translate("BILL", "New Customer?"))
        self.label_11.setText(_translate("BILL", "Total Amount"))
        self.totalAmtLbl.setText(_translate("BILL", "0"))
        self.GenBillBtn.setText(_translate("BILL", "Generate Bill"))
        self.regBtn.setText(_translate("BILL", "Register Here"))

if __name__ == '__main__':
    app = QtGui.QApplication([])
    gui = Ui_BILL()
    gui.show()
    app.exec_()