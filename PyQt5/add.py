import mysql.connector
from mysql.connector import errors
from mysql.connector.errors import get_exception
from sqlconnection import connection
import sys 
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from add_qt import Ui_AWindow
# from choose_btn import ChooseWindow

class MySQL:

    connection = connection
    myCursor = connection.cursor()

class AddWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(AddWindow,self).__init__()

        self.ui = Ui_AWindow()
        self.ui.setupUi(self)

        self.loadClass()

        self.ui.btn_save.clicked.connect(self.addSave)
        self.ui.btn_back.clicked.connect(self.addBack)

    def loadClass(self):
        sql = "select className from class"
        MySQL.myCursor.execute(sql)  # Tum kolonlari secer.
        result = MySQL.myCursor.fetchall()    # Tum satirlari secer.
        
        cListe = []
        index = 0
         
        for stu in result:
            cListe.insert(index, stu[0]) 
            index += 1

        self.ui.cb_class.addItems(cListe)


    def addSave(self):
        no = self.ui.txt_no.text()
        name = self.ui.txt_name.text()
        surName = self.ui.txt_surname.text()
        gender = self.ui.txt_gender.text()
        choose = self.ui.cb_class.currentText()
        birthdate = self.ui.dt_birthday.date().toString(Qt.ISODate)


        def control():
            try:
                MySQL.connection.commit()
                self.ui.add_lbl_result.setText("Registration successful")
                print(f"{MySQL.myCursor.rowcount} tane kayit yapildi.")
            except mysql.connector.Error as err:
                print("Problem: ", err)
            finally:
                MySQL.connection.close()
                print("Kayit isleminiz gerceklesti")

        
        
        if no and name and surName and gender is not None:
            try:
                if choose == "XX":
                    sql = "INSERT INTO students(SchoolNo,name,surName,Birthdate,gender,ClassId) VALUES (%s,%s,%s,%s,%s,%s)"
                    value = (no,name,surName,birthdate,gender,1)
                    MySQL.myCursor.execute(sql,value)
                    control()
                elif choose == "XY":
                    sql = "INSERT INTO students(SchoolNo,name,surName,Birthdate,gender,ClassId) VALUES (%s,%s,%s,%s,%s,%s)"
                    value = (no,name,surName,birthdate,gender,2)
                    MySQL.myCursor.execute(sql,value)
                    control()
                elif choose == "YY":
                    sql = "INSERT INTO students(SchoolNo,name,surName,Birthdate,gender,ClassId) VALUES (%s,%s,%s,%s,%s,%s)"
                    value = (no,name,surName,birthdate,gender,3)
                    MySQL.myCursor.execute(sql,value)
                    control()
                elif choose == "ZY":
                    sql = "INSERT INTO students(SchoolNo,name,surName,Birthdate,gender,ClassId) VALUES (%s,%s,%s,%s,%s,%s)"
                    value = (no,name,surName,birthdate,gender,4)
                    MySQL.myCursor.execute(sql,value)
                    control()
                elif choose == "ZZ":
                    sql = "INSERT INTO students(SchoolNo,name,surName,Birthdate,gender,ClassId) VALUES (%s,%s,%s,%s,%s,%s)"
                    value = (no,name,surName,birthdate,gender,5)
                    MySQL.myCursor.execute(sql,value)
                    control()
            except Exception:
                self.ui.add_lbl_result.setText("This record already exists")
        else:
            QMessageBox.warning(self,"Error","Registration failed. Try again.")
            


    def addBack(self):
        pass


def AddApp():
    app = QtWidgets.QApplication(sys.argv)
    win = AddWindow()
    win.show()
    # sys.exit(app.exec_())

AddApp()

