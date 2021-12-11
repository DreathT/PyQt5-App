import sys 
from PyQt5 import QtWidgets
from fp_qt import Ui_MainWindow
from choose_btn import ChooseWindow

class FpWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(FpWindow,self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_start.clicked.connect(self.choosePage)

    def choosePage(self):
        self.win = ChooseWindow()
        self.win.show()
        self.close()


def fpApp():
    app = QtWidgets.QApplication(sys.argv)
    win = FpWindow()
    win.show()
    sys.exit(app.exec_())

fpApp()