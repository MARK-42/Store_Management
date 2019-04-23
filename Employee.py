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
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 160, 91, 41))
        self.label_2.setObjectName("label_2")
        self.staffIdTbox = QtWidgets.QTextEdit(self.centralwidget)
        self.staffIdTbox.setGeometry(QtCore.QRect(340, 160, 141, 41))
        self.staffIdTbox.setObjectName("staffIdTbox")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(220, 240, 81, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(210, 290, 91, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(210, 350, 81, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(210, 410, 81, 16))
        self.label_6.setObjectName("label_6")
        self.staffNameTb = QtWidgets.QTextEdit(self.centralwidget)
        self.staffNameTb.setGeometry(QtCore.QRect(340, 220, 141, 41))
        self.staffNameTb.setObjectName("staffNameTb")
        self.staffDesgTb = QtWidgets.QTextEdit(self.centralwidget)
        self.staffDesgTb.setGeometry(QtCore.QRect(340, 280, 141, 41))
        self.staffDesgTb.setObjectName("staffDesgTb")
        self.staffUsernameTb = QtWidgets.QTextEdit(self.centralwidget)
        self.staffUsernameTb.setGeometry(QtCore.QRect(340, 340, 141, 41))
        self.staffUsernameTb.setObjectName("staffUsernameTb")
        self.staffPassTb = QtWidgets.QTextEdit(self.centralwidget)
        self.staffPassTb.setGeometry(QtCore.QRect(340, 400, 141, 41))
        self.staffPassTb.setObjectName("staffPassTb")
        self.regBtn = QtWidgets.QPushButton(self.centralwidget)
        self.regBtn.setGeometry(QtCore.QRect(300, 510, 93, 28))
        self.regBtn.setObjectName("regBtn")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">STAFF REGISTRATION </span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "STAFF ID"))
        self.label_3.setText(_translate("MainWindow", "NAME"))
        self.label_4.setText(_translate("MainWindow", "DESIGNATION"))
        self.label_5.setText(_translate("MainWindow", "USERNAME"))
        self.label_6.setText(_translate("MainWindow", "PASSWORD"))
        self.regBtn.setText(_translate("MainWindow", "REGISTER"))

if __name__ == '__main__':
    app = QtGui.QApplication([])
    gui = Ui_employee()
    gui.show()
    app.exec_()