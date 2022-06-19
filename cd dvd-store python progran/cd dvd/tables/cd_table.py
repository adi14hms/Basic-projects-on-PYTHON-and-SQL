import mysql.connector as sql
conn=sql.connect(host="localhost", user="root", passwd="1234",database="dvd")
if conn.is_connected():
    print("connected")
    
c1=conn.cursor()
c1.execute('create table cd_details(year_of_release  int, type_of_movie  varchar(65) , movie_name varchar(65), language varchar(56))')
print("table created")
