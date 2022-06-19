import mysql.connector as sql
conn=sql.connect(host="localhost", user="root", passwd="2099",database="dvd")
if conn.is_connected():
    print("HELLO")
    
c1=conn.cursor()
c1.execute('use dvd')
c1=conn.cursor()
print("WELCOME TO  CD STORE")
print(' ')
print(' ')
from time import gmtime,strftime
a=strftime("%A | %B %d,%Y",gmtime())
print(a)
print(' ')
print(' ')
name=input("enter your name:")
n=name.capitalize()
print(' ')
print(' ')
print('OUR HEARTY WELCOMES TO',n)
print(' ')
print(' ')
print("1.login")
print("2.To create account")
print("3.exit")
print('')
print('')
choice=int(input("enter your choice:"))
print(' ')
print(' ')
if choice==1:
    user_id=int(input('Enter your User ID :'))
    print(' ')
    passwd=int(input('Enter your Passphrase :'))
    print(' ')
    c1=conn.cursor()
    c1.execute('select * from login')
    data=c1.fetchall()
    count=c1.rowcount
    for row in data:
     if (user_id in row) and (passwd in row):
      print(' ')
     print(' ')
     conn.cursor()
     conn.commit()
     print(' ')
     print('For Online Order, press                 :1')
     print(' ')
     print(' ')
     print('For details on CD, press                :2')
     print(' ')
     print(' ')
     print('For details enquiry of DVD, press       :3')
     print(' ')
     print(' ')
     choice2=int(input("enter your choice to see cd and dvd(5 or 6) and for online order(4):"))
     if choice2==2:
        v_year_of_release=int(input("enter the year:"))
        v_language=input("enter ur language:")
        print("1.horror")
        print("2.comedy")
        print("3.action")
        print("4.inspiration")
        print("5.sentimental")
        v_type_of_movie=input("type of movie u want:")
        v_movie_name=input("enter movie name:")
        print("details uploaded")
        V_SQL_INSERT1="insert into cd_details values("+str(v_year_of_release)+",'"+v_type_of_movie+"','"+v_movie_name+"','"+v_language+"')"
        c1.execute(V_SQL_INSERT1)
        print("movie added to your cart")
        conn.commit()
     if choice2==3:
        v_dvd_model=input("enter dvd model:")
        v_dvd_name=input("enter dvd company:")
        v_version=int(input("enter the version you need:"))
        v_range_of_amt=int(input("the amt of product u expect:"))
        if v_range_of_amt>=5000:
            print("best products awaits you")
        else:
            print("we can provide the best if there is offers")
        V_SQL_INSERT2="insert into dvd_detail values('"+v_dvd_model+"','"+v_dvd_name+"',"+str(v_version)+","+str(v_range_of_amt)+")"
        c1.execute(V_SQL_INSERT2)
        print("dvd added to your cart !!!")
        conn.commit()
     if choice2==1:
        v_customer_name=input("enter name:")
        print("welcome",v_customer_name,"to our shop")
        v_age=int(input("enter ur age:"))
        v_mobile_number=int(input("enter ur phno:"))
        v_cd_or_dvd=input("enter what you want(cd or dvd):")
        if v_cd_or_dvd=="cd":
            v_year_of_release=int(input("enter the year:"))
            v_language=input("enter ur language:")
            print("1.horror")
            print("2.comedy")
            print("3.action")
            print("4.inspiration")
            print("5.sentimental")
            v_type_of_movie=input("type of movie u want:")
            v_movie_name=input("enter movie name:")
            print("details uploaded")
            V_SQL_INSERT1="insert into cd_details values("+str(v_year_of_release)+",'"+v_type_of_movie+"','"+v_movie_name+"','"+v_language+"')"
            c1.execute(V_SQL_INSERT1)
            print("movie added to your cart")
            conn.commit()
        elif v_cd_or_dvd=="dvd":
            v_dvd_model=input("enter dvd model:")
            v_dvd_name=input("enter dvd name:")
            v_version=int(input("enter the version you need:"))
            v_range_of_amt=int(input("the amt of product u expect:"))
            if v_range_of_amt>=10000:
                print("best products awaits you")
            else:
                print("we can provide the best if there is offers")
                V_SQL_INSERT2="insert into dvd_detail values('"+v_dvd_model+"','"+v_dvd_name+"',"+str(v_version)+","+str(v_range_of_amt)+")"
                c1.execute(V_SQL_INSERT2)
                print("dvd added to your cart !!!")
                conn.commit()
        else:
            print("sorry we didn't get u")
            v_rating=int(input("rate us if u like:"))
            V_SQL_INSERT1="insert into online values('"+v_customer_name+"',"+str(v_age)+","+str(v_mobile_number)+",'"+v_cd_or_dvd+"',"+str(v_rating)+")"
            c1.execute(V_SQL_INSERT1)
            conn.commit()
            print("your order will accpected once u detail ur material")
            
        
if choice==2:
    print('to create your account please enter your user id and password')
    c1=conn.cursor()
    #c1=conn.cursor("('create table login_id(user_id varchar(100) primary key,passwd varchar(100),name varchar(100))')
    user_id=int(input("Choose your User id (in integer):"))
    print('')
    passwd=int(input("Enter your Password (in integer):"))
    print('')
    name=input("Enter your Full name:")
    print('')
    c1=conn.cursor()
    update="insert into login values("+ str(user_id) +","+ str(passwd) +",'"+ name +"')"
    c1.execute(update)
    conn.commit()
    print("account created")
    

if choice==3:
    print("THANK YOU",n)
    print("VISIT AGAIN")



               
