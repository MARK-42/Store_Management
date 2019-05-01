# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'staffRegistration.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_employee(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 40, 441, 71))
        self.label.setObjectName("label")
        self.staffEmailTbox = QtWidgets.QTextEdit(self.centralwidget)
        self.staffEmailTbox.setGeometry(QtCore.QRect(340, 220, 141, 41))
        self.staffEmailTbox.setObjectName("staffEmailTbox")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(210, 170, 81, 16))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(210, 350, 81, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(210, 410, 81, 16))
        self.label_6.setObjectName("label_6")
        self.staffNameTb = QtWidgets.QTextEdit(self.centralwidget)
        self.staffNameTb.setGeometry(QtCore.QRect(340, 160, 141, 41))
        self.staffNameTb.setObjectName("staffNameTb")
        self.staffPhoneTb = QtWidgets.QTextEdit(self.centralwidget)
        self.staffPhoneTb.setGeometry(QtCore.QRect(340, 280, 141, 41))
        self.staffPhoneTb.setObjectName("staffPhoneTb")
        self.staffUsernameTb = QtWidgets.QTextEdit(self.centralwidget)
        self.staffUsernameTb.setGeometry(QtCore.QRect(340, 340, 141, 41))
        self.staffUsernameTb.setObjectName("staffUsernameTb")
        self.staffPassTb = QtWidgets.QTextEdit(self.centralwidget)
        self.staffPassTb.setGeometry(QtCore.QRect(340, 400, 141, 41))
        self.staffPassTb.setObjectName("staffPassTb")
        self.regBtn = QtWidgets.QPushButton(self.centralwidget)
        self.regBtn.setGeometry(QtCore.QRect(300, 510, 93, 28))
        self.regBtn.setObjectName("regBtn")
        self.regBtn.clicked.connect(self.register)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(210, 240, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(210, 290, 47, 13))
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def register(self):
        import cx_Oracle
        import os
        self.con = cx_Oracle.connect('shivansh', '1234', cx_Oracle.makedsn('localhost', 1521, 'DBMS1'))
        self.cur = self.con.cursor()
        output = self.cur.var(str)
        print(self.cur.callproc("management.insertEmployee", (self.staffNameTb.toPlainText().split(' ')[0], self.staffNameTb.toPlainText().split(' ')[-1], 
            self.staffUsernameTb.toPlainText(), self.staffPassTb.toPlainText(), int(self.staffPhoneTb.toPlainText()),'addr', self.staffEmailTbox.toPlainText(),
            500,'n', output )))
        print(output)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">STAFF REGISTRATION </span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "NAME"))
        self.label_5.setText(_translate("MainWindow", "USERNAME"))
        self.label_6.setText(_translate("MainWindow", "PASSWORD"))
        self.regBtn.setText(_translate("MainWindow", "REGISTER"))
        self.label_2.setText(_translate("MainWindow", "EMAIL"))
        self.label_4.setText(_translate("MainWindow", "PHONE"))

if __name__ == '__main__':
    app = QtGui.QApplication([])
    gui = Ui_employee()
    gui.show()
    app.exec_()