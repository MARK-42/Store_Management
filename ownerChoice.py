# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ownerChoice.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ownerChoiceWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.sellBtn = QtWidgets.QPushButton(self.centralwidget)
        self.sellBtn.setGeometry(QtCore.QRect(30, 410, 171, 61))
        self.sellBtn.setObjectName("sellBtn")
        self.updateBtn = QtWidgets.QPushButton(self.centralwidget)
        self.updateBtn.setGeometry(QtCore.QRect(282, 410, 171, 61))
        self.updateBtn.setObjectName("updateBtn")
        self.registerBtn = QtWidgets.QPushButton(self.centralwidget)
        self.registerBtn.setGeometry(QtCore.QRect(552, 407, 171, 61))
        self.registerBtn.setObjectName("registerBtn")
        self.OwnerNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.OwnerNameLabel.setGeometry(QtCore.QRect(200, 150, 341, 51))
        self.OwnerNameLabel.setObjectName("OwnerNameLabel")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.sellBtn.setText(_translate("MainWindow", "SELL"))
        self.updateBtn.setText(_translate("MainWindow", "UPDATE INVENTORY"))
        self.registerBtn.setText(_translate("MainWindow", "REGISTER NEW STAFF"))
        self.OwnerNameLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">Welcome , Owner</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_ownerChoiceWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

