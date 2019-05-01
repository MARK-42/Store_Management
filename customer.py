# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'customer.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Customer(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(643, 475)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.FName = QtWidgets.QLabel(self.centralwidget)
        self.FName.setGeometry(QtCore.QRect(216, 110, 61, 20))
        self.FName.setObjectName("FName")
        self.LName = QtWidgets.QLabel(self.centralwidget)
        self.LName.setGeometry(QtCore.QRect(216, 170, 61, 20))
        self.LName.setObjectName("LName")
        self.Addr = QtWidgets.QLabel(self.centralwidget)
        self.Addr.setGeometry(QtCore.QRect(216, 230, 61, 20))
        self.Addr.setObjectName("Addr")
        self.FNameTxt = QtWidgets.QLineEdit(self.centralwidget)
        self.FNameTxt.setGeometry(QtCore.QRect(330, 110, 113, 20))
        self.FNameTxt.setObjectName("FNameTxt")
        self.LNameTxt = QtWidgets.QLineEdit(self.centralwidget)
        self.LNameTxt.setGeometry(QtCore.QRect(330, 170, 113, 20))
        self.LNameTxt.setObjectName("LNameTxt")
        self.AddrTxt = QtWidgets.QLineEdit(self.centralwidget)
        self.AddrTxt.setGeometry(QtCore.QRect(330, 230, 113, 20))
        self.AddrTxt.setObjectName("AddrTxt")
        self.EmailTxt = QtWidgets.QLineEdit(self.centralwidget)
        self.EmailTxt.setGeometry(QtCore.QRect(330, 290, 113, 20))
        self.EmailTxt.setObjectName("EmailTxt")
        self.Email = QtWidgets.QLabel(self.centralwidget)
        self.Email.setGeometry(QtCore.QRect(216, 290, 61, 20))
        self.Email.setObjectName("Email")
        self.PhoneTxt = QtWidgets.QLineEdit(self.centralwidget)
        self.PhoneTxt.setGeometry(QtCore.QRect(330, 350, 113, 20))
        self.PhoneTxt.setObjectName("PhoneTxt")
        self.Phone = QtWidgets.QLabel(self.centralwidget)
        self.Phone.setGeometry(QtCore.QRect(216, 350, 61, 20))
        self.Phone.setObjectName("Phone")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(240, 30, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(22)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(300, 400, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.regCust)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 643, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def regCust(self):

        import cx_Oracle
        import os
        self.con = cx_Oracle.connect('shivansh', '1234', cx_Oracle.makedsn('localhost', 1521, 'DBMS1'))
        self.cur = self.con.cursor()
        output = self.cur.var(str)
        print(self.cur.callproc("management.insertCustomer", (self.FNameTxt.text(), self.LNameTxt.text(), 
            self.PhoneTxt.text(), self.AddrTxt.text(), self.EmailTxt.text() ,0, output )))
        print(output)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.FName.setText(_translate("MainWindow", "First Name"))
        self.LName.setText(_translate("MainWindow", "Last Name"))
        self.Addr.setText(_translate("MainWindow", "Address"))
        self.Email.setText(_translate("MainWindow", "Email"))
        self.Phone.setText(_translate("MainWindow", "Phone"))
        self.label_6.setText(_translate("MainWindow", "New Customer"))
        self.pushButton.setText(_translate("MainWindow", "Register"))

