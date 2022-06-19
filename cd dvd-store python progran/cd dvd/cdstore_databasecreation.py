import mysql.connector as sql
conn = sql.connect(
  host="localhost",
  user="root",
  password="2099"
)

if conn.is_connected():
    print("sucessfully connected")

conn.cursor().execute("CREATE DATABASE DVD7")
print("Database Successfully Created")
conn.cursor().execute("USE DVD7")
conn.cursor().execute('create table cd_details(year_of_release  int, type_of_movie  varchar(65) , movie_name varchar(65), language varchar(56))')
print("CD_table created")
conn.cursor().execute('create table dvd_detail(dvd_model varchar(65),dvd_name varchar(56),version int,range_of_amt int)')
print("DVD_table created")
conn.cursor().execute('create table online(customer_name varchar(100),age int,mobile_number bigint,cd_or_dvd varchar(65),rating int)')
print("Online_ order table created")
conn.cursor().execute('CREATE TABLE login(v_user_id int, v_passwd int, v_name varchar(30))')
print("table created")

v_user_id=int(input("Enter id:"))
v_passwd=int(input("Enter password:"))
v_name=input("Enter your name")

V_SQL_INSERT="insert into login values("+str(v_user_id)+","+str(v_passwd)+",'"+v_name+"')"
conn.cursor().execute(V_SQL_INSERT)
conn.commit()
print("LOGIN DONE")


