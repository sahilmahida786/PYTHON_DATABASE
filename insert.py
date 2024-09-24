import mysql.connector as MyConn

My_db=MyConn.connect(host="localhost", user="root", password="Sahil786@", database="sahil")
db_cursor=My_db.cursor()
db_insert="insert into Emp(Roll,Ename) values(%s,%s)"
db_list=[(5,"mayank"),(6,"rehan"),(7,"sahil"),(8,"null")]
db_cursor.executemany(db_insert,db_list)
My_db.commit()
print(db_cursor.rowcount,"Record inserted")
