import mysql.connector as MyConn

My_db=MyConn.connect(host="localhost", user="root", password="Sahil786@",database="Sahil")

db_cursor=My_db.cursor()

db_deleteData="delete from Emp where Ename=%s"
db_value=("null",) # 1 row Delete and select name  

db_cursor.execute(db_deleteData,db_value)
My_db.commit()
print("Delete successfully")