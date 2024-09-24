import mysql.connector as MyConn

My_db=MyConn.connect(host="localhost", user="root", password="Sahil786@")

db_cursor=My_db.cursor()

db_cursor.execute("Select * from sahil.Emp")
for db_data in db_cursor.fetchall():
    print(db_data)