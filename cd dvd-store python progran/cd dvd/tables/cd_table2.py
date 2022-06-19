import mysql.connector as sql
conn=sql.connect(host="localhost", user="root", passwd="1234",database="dvd")
if conn.is_connected():
    print("connected")
    
c1=conn.cursor()
c1.execute('create table  login_id( user_id  int(11) primary key,passwd int(11),name varchar(65))')
print("table created")
