import mysql.connector as sql
conn=sql.connect(host="localhost", user="root", passwd="1234",database="dvd")
if conn.is_connected():
    print("connected")
    
conn.cursor().execute('CREATE TABLE login(v_user_id int, v_passwd int, v_name varchar(30))')
print("table created")

v_user_id=int(input("Enter id:"))
v_passwd=int(input("Enter password:"))
v_name=input("Enter your name")

V_SQL_INSERT="insert into login values("+str(v_user_id)+","+str(v_passwd)+",'"+v_name+"')"
conn.cursor().execute(V_SQL_INSERT)
conn.commit()
print("LOGIN DONE")

