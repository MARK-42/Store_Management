from owner import Ui_ownerPage
from billGenerator import Ui_BILL
from login import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5 import QtCore, QtGui

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
