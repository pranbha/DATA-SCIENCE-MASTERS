import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Goodmorning@1"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE if not exists test1")
mydb.close()