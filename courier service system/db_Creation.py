import mysql.connector as sql
conn = sql.connect(
  host="localhost",
  user="root",
  password="2099"
)

if conn.is_connected():
    print("sucessfully connected")

conn.cursor().execute("CREATE DATABASE Courier")
print("Database Successfully Created")
conn.cursor().execute("USE Courier")
conn.cursor().execute('create table log_in(cust_name  varchar(65), account_no  int, password int)')
print("Log_in_table created")
conn.cursor().execute('create table address(cust_name varchar(65),cust_address varchar(65),bill varchar(10),sender_name varchar(65), phone_no bigint)')
print("Customer_table created")
conn.commit()
print("DONE")

