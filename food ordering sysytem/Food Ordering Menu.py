import mysql.connector as sql
conn=sql.connect(host="localhost", user="root", passwd="2099", database="foodmenu-db")
if conn.is_connected():
    print("Conection With Database Establised Successfully")
else:
    print("Conection With Database Failed XXX")
print("Welcome to Food Ordering Menu")

c1=conn.cursor()
choice = 0
while choice != 3:
    print("1.CREATE YOUR ACCOUNT")
    print("2.LOG IN")
    print("3.EXIT")
    choice=int(input("ENTER YOUR CHOICE:"))
    if choice ==1:
     v_cust_name=input("Enter your name :")
     v_account_no=int(input("enter your User ID :"))
     v_password=int(input("Enter your Passpharse :"))
     v_SQL_insert="insert into log_in values('"+v_cust_name+"',"+str(v_account_no)+", "+str (v_password)+")"
     c1.execute(v_SQL_insert)
     conn.commit()
     print("ACCOUNT CREATED")

    if choice==2:
     print('')
     print('Enter your Credentials')
     cust_name=input('Enter your name : ')
     print('')
     v_account_no=int(input('Enter your User ID : '))
     print(' ')
     v_password=int(input('Enter your Passpharse : '))
     print(' ')
     c1=conn.cursor()
     c1.execute('select * from log_in')
     data=c1.fetchall()
     count=c1.rowcount
     for row in data:
        if (cust_name in row) and (v_account_no in row):
            print(' ')
            print(' ')
            print("WELCOME TO FOOD ORDERING SERVICE")
            print(' ')
            print(' ')
            print('TO SEE EMPLOYEES DETAILS PRESS :1')
            print(' ')
            print('TO UPDATE DETAILS PRESS        :2')
            print(' ')
            print('TO EXIT PRESS                  :3')
            print(' ')
            print('TO ORDER FOOD                  :4')
            print(' ')
            print('TO SEE ORDERED FOOD            :5')
            print(' ')
            print('WANT TO RATE US ?              :6')
            print(' ')
            c2=int(input('enter your choice : '))
            if (c2==1):
                c1=conn.cursor()
                c1.execute('select * from log_in')
                data=c1.fetchall()
                count=c1.rowcount
                print('Details of all employees is',count)
                print("Details of all employees are arranged as Name/User ID/Passpharse")
                for row in data:
                    print(row)
                print("VISIT AGAIN")
            elif (c2==2):
                print('')
                print('TO UPDATE FILL THIS')
                print('')
                empName = input("Enter name")
                update = input("Enter new name")
                sqlFormula = "UPDATE log_in SET v_cust_name=%s WHERE v_cust_name = %s"
                c1.execute(sqlFormula,(update,empName))
                conn.commit()

                print('YOUR DETAILS ARE SUCESSFULLY UPDATED')
            elif (c2==3):
                print('THANK YOU FOR VISITING')
            elif(c2==4):
                 v_f_name=input("enter the name of food:")
                 v_price=int(input("enter the cost of your food:"))
                 v_address=input("enter your delivery address:")
                 v_cust_name=input("enter Customer Name:")
                 v_phone_no=int(input("Enter Customer phone no:"))
                 v_SQL_insert="insert into menu values("+"'"+ v_f_name+"'"+","+"'"+str(v_price)+"'"+","+"'"+v_address+"'"+","+"'"+v_cust_name+"'"+","+str(v_phone_no)+")"
                 c1.execute(v_SQL_insert)
                 conn.commit()
                 print("SUCESSFULLY ORDERED")
                 print("Your Food will be served within 15 minutes")
            elif(c2==5):
                  c1=conn.cursor()
                  c1.execute('select * from sales1')
                  data=c1.fetchall()
                  count=c1.rowcount
                  print('total order food  is',count)
                  for row in data:
                     print(row)
                  print("VISIT AGAIN")
            elif (c2==6):
                print('RATE US FOR SERVICE')
                rating=int(input("On the Scale of 10 how would you like to rate us:"))
                print('THANK FOR RATING')
            else:
                print("ERROR,ERROR...........")

        
     if choice==3:
      print("THANK YOU FOR VISITING")
      cl.close
               
                 
            
