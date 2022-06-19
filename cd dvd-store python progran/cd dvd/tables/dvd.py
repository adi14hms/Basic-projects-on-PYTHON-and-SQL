import mysql.connector as sql
conn=sql.connect(host="localhost", user="root", passwd="1234",database="dvd")
if conn.is_connected():
    print("connected")
    
c1=conn.cursor()
c1.execute('create table dvd_detail(dvd_model varchar(65),dvd_name varchar(56),version int,range_of_amt int)')
print('created')
           
