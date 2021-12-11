import mysql.connector
from sqlconnection import connection
import sys 
from PyQt5 import QtWidgets
from information_qt import Ui_InfWindow

class InfSQL:

    connection = connection
    myCursor = connection.cursor()

class InfWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(InfWindow,self).__init__()

        self.ui = Ui_InfWindow()
        self.ui.setupUi(self)

        self.ui.inf_btn_search.clicked.connect(self.infSearch)
        self.ui.inf_btn_back.clicked.connect(self.infBack)

    def infSearch(self):
        sNo = self.ui.inf_txt_no.text()

        # sq = f"select SchoolNo from students"
        # InfSQL.myCursor.execute(sq)
        # nos = InfSQL.myCursor.fetchall()
        # nListe = []
        # for i in nos:
        #     nListe.append(i[0])
        # print(nListe)
        # if sNo not in nListe:
        #     self.ui.inf_lbl_inf.setText("no such record found \nBO'IL UF WO'A")
        try:
            sql = f"select * from students where SchoolNo = {sNo}"
            InfSQL.myCursor.execute(sql)  # Tum kolonlari secer.
            result = InfSQL.myCursor.fetchall()    # Tum satirlari secer.
            result = result[0]

            sql = f"select * from class where id = {result[6]}"
            InfSQL.myCursor.execute(sql)
            Class = InfSQL.myCursor.fetchall()
            Class = Class[0]
        
            self.ui.inf_lbl_inf.setText(f"No: {result[1]} \nName and Surname: {result[2]} {result[3]} \nClass: {Class[1]} \nGender: {result[4]} \nBirthday: {result[5]}")
        except IndexError:
            self.ui.inf_lbl_inf.setText("no such record found")

    def infBack(self):
        pass

def infApp():
    app = QtWidgets.QApplication(sys.argv)
    win = InfWindow()
    win.show()
    # sys.exit(app.exec_())

infApp()