import mysql.connector 
con=mysql.connector.connect(host="localhost",user='root',passwd='2099')
c = con.cursor()
sql1 = "create database auto2"
c.execute(sql1)
sql2 = "use auto2"
c.execute(sql2)
sql3 = "create table customer_details((sno int primary key, cname varchar(25),cdetails varchar(30),caddress varchar(30),cpincode int,cpuramt int,cdisc float)"
c.execute(sql3)
con.commit()
