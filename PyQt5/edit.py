import mysql.connector
from mysql.connector.errors import OperationalError
from sqlconnection import connection
import sys 
from PyQt5 import QtWidgets
from edit_qt import Ui_EWindow
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox
# from choose_btn import ChooseWindow

class EditSQL:

    connection = connection
    myCursor = connection.cursor()

class EditWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(EditWindow,self).__init__()

        self.ui = Ui_EWindow()
        self.ui.setupUi(self)

        self.editLoadClass()

        self.ui.edit_btn_find.clicked.connect(self.editSearch)
        self.ui.edit_btn_save.clicked.connect(self.editSave)

    def editLoadClass(self):
        sql = "select className from class"
        EditSQL.myCursor.execute(sql)  # Tum kolonlari secer.
        result = EditSQL.myCursor.fetchall()    # Tum satirlari secer.
        
        cListe = []
        index = 0
         
        for stu in result:
            cListe.insert(index, stu[0]) 
            index += 1

        self.ui.edit_cb_class.addItems(cListe)

    def editSearch(self):

        sNo = self.ui.edit_search_txt_no.text()
        
        try:
            sql = f"select * from students where SchoolNo = {sNo}"
            EditSQL.myCursor.execute(sql)  # Tum kolonlari secer.
            result = EditSQL.myCursor.fetchall()    # Tum satirlari secer.
            result = result[0]

            sql = f"select * from class where id = {result[6]}"
            EditSQL.myCursor.execute(sql)
            Class = EditSQL.myCursor.fetchall()
            Class = Class[0]
        
            self.ui.edit_lbl_before.setText(f"No: {result[1]} \nName and Surname: {result[2]} {result[3]} \nClass: {Class[1]} \nGender: {result[4]} \nBirthday: {result[5]}")
        except IndexError:
            self.ui.edit_lbl_before.setText("no such record found")


    def editSave(self):
        sNo = self.ui.edit_search_txt_no.text()
        name = self.ui.edit_txt_name.text()
        surname = self.ui.edit_txt_surname.text()
        gender = self.ui.edit_txt_gender.text()
        cbClass = self.ui.edit_cb_class.currentText()
        birthdate = self.ui.edit_dt_birthday.date().toString(Qt.ISODate)

        def editControl():
            try:
                EditSQL.connection.commit()
                print(f"{EditSQL.myCursor.rowcount} tane guncelleme yapildi.")
            except mysql.connector.Error as err:
                print("Problem: ", err)
            finally:
                EditSQL.connection.close()
                print("Guncelleme isleminiz gerceklesti")
        
        if sNo and name and surname and gender is not None:
            
            if cbClass == "XX":
                sql = f"Update Students Set Name='{name}',Surname='{surname}',Gender='{gender}',Birthdate='{birthdate}',ClassId=1 Where SchoolNo={sNo}"
                # sql = f"Update Students Set Name=%s,Surname=%s,Gender=%s,Birthdate=%s,ClassId=%s Where SchoolNo=%s"
                # values = (name,surname,gender,birthdate,1,sNo)
                EditSQL.myCursor.execute(sql)
                editControl()
            elif cbClass == "XY":
                sql = f"Update Students Set Name=%s,Surname=%s,Gender=%s,Birthdate=%s,ClassId=%s Where SchoolNo=%s"
                values = (name,surname,gender,birthdate,2,sNo)
                EditSQL.myCursor.execute(sql,values)
                editControl()
            elif cbClass == "YY":
                sql = f"Update Students Set Name=%s,Surname=%s,Gender=%s,Birthdate=%s,ClassId=%s Where SchoolNo=%s"
                values = (name,surname,gender,birthdate,3,sNo)
                EditSQL.myCursor.execute(sql,values)
                editControl()
            elif cbClass == "ZY":
                sql = f"Update Students Set Name=%s,Surname=%s,Gender=%s,Birthdate=%s,ClassId=%s Where SchoolNo=%s"
                values = (name,surname,gender,birthdate,4,sNo)
                EditSQL.myCursor.execute(sql,values)
                editControl()
            elif cbClass == "ZZ":
                sql = f"Update Students Set Name=%s,Surname=%s,Gender=%s,Birthdate=%s,ClassId=%s Where SchoolNo=%s"
                values = (name,surname,gender,birthdate,5,sNo)
                EditSQL.myCursor.execute(sql,values)
                editControl()
                
                sql = f"select * from students where SchoolNo = {sNo}"
                EditSQL.myCursor.execute(sql)  # Tum kolonlari secer.
                result = EditSQL.myCursor.fetchall()    # Tum satirlari secer.
                result = result[0]

                sql = f"select * from class where id = {result[6]}"
                EditSQL.myCursor.execute(sql)
                Class = EditSQL.myCursor.fetchall()
                Class = Class[0]
        
                self.ui.edit_lbl_after.setText(f"No: {result[1]} \nName and Surname: {result[2]} {result[3]} \nClass: {Class[1]} \nGender: {result[4]} \nBirthday: {result[5]}")
        else:
            QMessageBox.warning(self,"Error","Update failed. Try again.")
        
        


def editApp():
    app = QtWidgets.QApplication(sys.argv)
    win = EditWindow()
    win.show()
    # sys.exit(app.exec_())

editApp()