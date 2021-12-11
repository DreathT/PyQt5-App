import sys 
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from rm import RmWindow
from choose_btn_qt import Ui_ChoWindow
from add import AddWindow
from edit import EditWindow
from inf import InfWindow

class ChooseWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ChooseWindow,self).__init__()

        self.ui = Ui_ChoWindow()
        self.ui.setupUi(self)

        self.ui.btn_add.clicked.connect(self.addPage)
        self.ui.btn_edit.clicked.connect(self.editPage)
        self.ui.btn_inf.clicked.connect(self.infPage)
        self.ui.btn_remove.clicked.connect(self.removePage)
        self.ui.btn_exit.clicked.connect(self.exit)

    # @pyqtSlot
    def addPage(self):
        self.addWin = AddWindow()
        self.addWin.show()
        self.close()
    # @pyqtSlot
    def editPage(self):
        self.editWin = EditWindow()
        self.editWin.show()
        self.close()
    # @pyqtSlot
    def infPage(self):
        self.infWin = InfWindow()
        self.infWin.show()
        self.close()
    # @pyqtSlot
    def removePage(self):
        self.rmWin = RmWindow()
        self.rmWin.show()
        self.close()
    # @pyqtSlot
    def exit(self):
        QtWidgets.qApp.quit()

def chooseApp():
    app = QtWidgets.QApplication(sys.argv)
    win = ChooseWindow()
    win.show()
    # sys.exit(app.exec_())

chooseApp()