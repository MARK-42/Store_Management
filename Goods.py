# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'updateInventory.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_goods(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(801, 428)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 20, 451, 81))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 130, 101, 41))
        self.label_2.setObjectName("label_2")
        self.itemComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.itemComboBox.setGeometry(QtCore.QRect(280, 130, 171, 41))
        self.itemComboBox.setObjectName("itemComboBox")
        self.itemComboBox.addItem("")
        self.itemComboBox.addItem("")
        self.editBtn = QtWidgets.QPushButton(self.centralwidget)
        self.editBtn.setGeometry(QtCore.QRect(540, 130, 121, 41))
        self.editBtn.setObjectName("editBtn")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 250, 91, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(420, 230, 55, 16))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(390, 240, 81, 41))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(570, 250, 81, 31))
        self.label_6.setObjectName("label_6")
        self.costTextBox = QtWidgets.QTextEdit(self.centralwidget)
        self.costTextBox.setGeometry(QtCore.QRect(440, 250, 121, 31))
        self.costTextBox.setObjectName("costTextBox")
        self.qtTextBox = QtWidgets.QTextEdit(self.centralwidget)
        self.qtTextBox.setGeometry(QtCore.QRect(650, 250, 131, 31))
        self.qtTextBox.setObjectName("qtTextBox")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(200, 230, 101, 61))
        self.label_8.setObjectName("label_8")
        self.nameTextBox = QtWidgets.QTextEdit(self.centralwidget)
        self.nameTextBox.setGeometry(QtCore.QRect(250, 250, 131, 31))
        self.nameTextBox.setObjectName("nameTextBox")
        self.addBtn = QtWidgets.QPushButton(self.centralwidget)
        self.addBtn.setGeometry(QtCore.QRect(350, 340, 93, 28))
        self.addBtn.setObjectName("addBtn")
        self.addBtn.clicked.connect(self.addItem)
        self.itemTextBox = QtWidgets.QTextEdit(self.centralwidget)
        self.itemTextBox.setGeometry(QtCore.QRect(70, 250, 111, 31))
        self.itemTextBox.setObjectName("itemTextBox")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 300, 191, 101))
        self.groupBox.setObjectName("groupBox")
        self.editRb = QtWidgets.QRadioButton(self.groupBox)
        self.editRb.setGeometry(QtCore.QRect(20, 20, 95, 20))
        self.editRb.setObjectName("editRb")
        self.addRb = QtWidgets.QRadioButton(self.groupBox)
        self.addRb.setGeometry(QtCore.QRect(20, 50, 95, 20))
        self.addRb.setObjectName("addRb")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def addItem(self):
        import cx_Oracle
        import os
        self.con = cx_Oracle.connect('shivansh', '1234', cx_Oracle.makedsn('localhost', 1521, 'DBMS1'))
        self.cur = self.con.cursor()
        output = self.cur.var(str)
        print(self.cur.callproc("management.insertStock", (self.itemTextBox.toPlainText(), self.nameTextBox.toPlainText(), 
            'test', self.qtTextBox.toPlainText(), self.costTextBox.toPlainText(), 10, output )))
        #insertStock(id tabProductStock.productId%type, prn tabProductStock.productName%type, cat tabProductStock.catagory%type,
        # quant tabProductStock.totalQuantity%type, pr tabProductStock.price%type, wei tabProductStock.weight%type, exitc OUT varchar2);
        print(output)


        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt;\">UPDATE INVENTORY</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">ITEM</span></p></body></html>"))
        self.itemComboBox.setItemText(0, _translate("MainWindow", "SOAP"))
        self.itemComboBox.setItemText(1, _translate("MainWindow", "SHAMPOO"))
        self.editBtn.setText(_translate("MainWindow", "EDIT"))
        self.label_3.setText(_translate("MainWindow", "ITEM ID"))
        self.label_5.setText(_translate("MainWindow", "COST"))
        self.label_6.setText(_translate("MainWindow", "QUANTITY"))
        self.costTextBox.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">21</p></body></html>"))
        self.qtTextBox.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">43</p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "NAME"))
        self.nameTextBox.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">WASHING POWDER</p></body></html>"))
        self.addBtn.setText(_translate("MainWindow", "ADD"))
        self.itemTextBox.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">A101</p></body></html>"))
        self.groupBox.setTitle(_translate("MainWindow", "CHOOSE "))
        self.editRb.setText(_translate("MainWindow", "EDIT"))
        self.addRb.setText(_translate("MainWindow", "ADD"))

if __name__ == '__main__':
    app = QtGui.QApplication([])
    gui = Ui_goods()
    gui.show()
    app.exec_()