# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'owner.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ownerPage(object):
    def setupUi(self, ownerPage):
        ownerPage.setObjectName("ownerPage")
        ownerPage.resize(493, 333)
        self.centralwidget = QtWidgets.QWidget(ownerPage)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 50, 47, 20))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(210, 120, 91, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 170, 91, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(210, 220, 91, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        ownerPage.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ownerPage)
        self.statusbar.setObjectName("statusbar")
        ownerPage.setStatusBar(self.statusbar)

        self.retranslateUi(ownerPage)
        QtCore.QMetaObject.connectSlotsByName(ownerPage)

    def retranslateUi(self, ownerPage):
        _translate = QtCore.QCoreApplication.translate
        ownerPage.setWindowTitle(_translate("ownerPage", "MainWindow"))
        self.label.setText(_translate("ownerPage", "ACTION"))
        self.pushButton.setText(_translate("ownerPage", "Update Goods"))
        self.pushButton_2.setText(_translate("ownerPage", "Billing"))
        self.pushButton_3.setText(_translate("ownerPage", "Add Employee"))

