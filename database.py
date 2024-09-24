import mysql.connector as MyConn

My_db=MyConn.connect(host="localhost", user="root", password="Sahil786@")

db_cursor=My_db.cursor()

db_cursor.execute("create database sahilmahida")

print ("Database created")