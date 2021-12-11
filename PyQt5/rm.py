import mysql.connector
from sqlconnection import connection
import sys 
from PyQt5 import QtWidgets
from rm_qt import Ui_RmWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
# from choose_btn import ChooseWindow

class RmSQL:

    connection = connection
    myCursor = connection.cursor()

class RmWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(RmWindow,self).__init__()

        self.ui = Ui_RmWindow()
        self.ui.setupUi(self)


        self.ui.rm_btn_search.clicked.connect(self.rmSearch)
        self.ui.rm_btn_delete.clicked.connect(self.rmDelete)
        self.ui.rm_btn_back.clicked.connect(self.rmBack)

    def rmSearch(self):
        sNo = self.ui.rm_txt_no.text()
        if sNo is not None:
            try:
                sql = f"select * from students where SchoolNo = {sNo}"
                RmSQL.myCursor.execute(sql)  # Tum kolonlari secer.
                result = RmSQL.myCursor.fetchall()    # Tum satirlari secer.
                result = result[0]

                sql = f"select * from class where id = {result[6]}"
                RmSQL.myCursor.execute(sql)
                Class = RmSQL.myCursor.fetchall()
                Class = Class[0]
            
                self.ui.rm_lbl_inf.setText(f"No: {result[1]} \nName and Surname: {result[2]} {result[3]} \nClass: {Class[1]} \nGender: {result[4]} \nBirthday: {result[5]}")
            except IndexError:
                self.ui.rm_lbl_inf.setText("no such record found")
        else:
            QMessageBox.warning(self,"Error","Failed. Try again.")

    def rmDelete(self):
        sNo = self.ui.rm_txt_no.text()

        def rmControl():
            try:
                RmSQL.connection.commit()
                print(f"{RmSQL.myCursor.rowcount} tane kayit silindi.")
            except mysql.connector.Error as err:
                print("Problem: ", err)
            finally:
                RmSQL.connection.close()
                print("Kayit silme isleminiz gerceklesti.")

        mess = QMessageBox.question(self, "Remove Student","Are you sure?",QMessageBox.Ok | QMessageBox.Cancel,QMessageBox.Cancel)
        if mess == QMessageBox.Ok:
            sql = f"delete from students where SchoolNo = {sNo}"
            RmSQL.myCursor.execute(sql)
            self.ui.rm_lbl_result.setText("Record deleted")
            rmControl()
        else:
            pass

        
    def rmBack(self):
        # self.choWin = ChooseWindow()
        # self.choWin.show()
        # self.close()
        pass


def rmApp():
    app = QtWidgets.QApplication(sys.argv)
    win = RmWindow()
    win.show()
    # sys.exit(app.exec_())

rmApp()