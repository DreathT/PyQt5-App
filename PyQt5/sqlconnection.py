import mysql.connector 

connection = mysql.connector.connect(
    host = "localhost", # 192.23.45.56
    user = "root",
    password = "*****",
    database = "app"
)

myCursor = connection.cursor()



