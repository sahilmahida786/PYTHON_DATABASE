import mysql.connector as MyConn

My_db=MyConn.connect(host="localhost", user="root", password="Sahil786@")

db_cursor=My_db.cursor()
db_Updatedate="update Sahil.emp set Roll=%s where Ename=%s"
db_value=(8,"null")
db_cursor.execute(db_Updatedate,db_value)

My_db.commit()
print(db_cursor.rowcount,"Data Updated! ")