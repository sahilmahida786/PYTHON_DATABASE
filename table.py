import mysql.connector as MyConn

My_db=MyConn.connect(host="localhost", user="root", password="Sahil786@", database="Sahil")
db_cursor=My_db.cursor()
db_cursor.execute("show table")
for i in db_cursor:
    print(i)