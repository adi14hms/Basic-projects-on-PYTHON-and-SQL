import mysql.connector as sql
conn=sql.connect(host="localhost", user="root", passwd="manager",database="dvd")
if conn.is_connected():
    print("connected")
    
c1=conn.cursor()
c1.execute('create table online(customer_name varchar(100),age int,mobile_number int,cd_or_dvd varchar(65),rating int)')
print("table created")
