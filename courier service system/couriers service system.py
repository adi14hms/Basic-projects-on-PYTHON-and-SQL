import mysql.connector as sql
conn=sql.connect(host="localhost", user="root", passwd="2099", database="courier")
mycursor=conn.cursor()
if conn.is_connected():
    print("Conection With Database Establised Successfully")
else:
    print("Conection With Database Failed XXX")

print("Welcome to ZARONE COURIER SERVICE")

c1=conn.cursor()
choice = 0
while choice != 3:
    print("1.CREATE YOUR ACCOUNT")
    print("2.LOG IN")
    print("3.EXIT")
    choice=int(input("ENTER YOUR CHOICE:"))
    if choice ==1:
     cust_name=input("Enter the customer name :")
     account_no=int(input("enter your User ID "))
     password=int(input("Enter your Passkey :"))
     v_SQL_insert="insert into log_in values('"+cust_name+"',"+str(account_no)+","+str (password)+")"
     c1.execute(v_SQL_insert)
     conn.commit()
     print("ACCOUNT CREATED")

    if choice==2:
     print('')
     print('Enter your Credentials')
     cust_name=input('Enter your name :')
     print('')
     account_no=int(input('Enter your User ID :'))
     print(' ')
     password=int(input('Enter your Password :'))
     print(' ')
     c1=conn.cursor()
     c1.execute('select * from log_in')
     data=c1.fetchall()
     count=c1.rowcount
     for row in data:
        if (cust_name in row) and (account_no in row):
            print(' ')
            print(' ')
            print("******************WELCOME TO ZARONE COURIER SYSTEM******************")
            print(' ')
            print(' ')
            print('TO SEE  DETAILS of all Customers,press         :1')
            print(' ')
            print('TO UPDATE details,press                        :2')
            print(' ')
            print('TO pay the bill,press                          :3')
            print(' ')
            print('TO SEE details of all the package              :4')
            print(' ') 
            print('TO EXIT,press                                  :5')
            print(' ')
            print('WANT TO RATE US, press                         :6')
            print(' ')
            c2=int(input('enter your choice : '))
            if (c2==1):
                c1=conn.cursor()
                c1.execute('select * from log_in')
                data=c1.fetchall()
                count=c1.rowcount
                print('Details of all Customer is',count)
                print("Details of all Customer are arranged as User Name/ID/Passkey")
                for row in data:
                    print(row)
                print("VISIT AGAIN")
            elif (c2==2):
                print('')
                print('TO UPDATE FILL THIS')
                print('')
                empName = input("Enter name")
                update = input("Enter new name")
                sqlFormula = "UPDATE log_in SET cust_name=%s WHERE cust_name = %s"
                c1.execute(sqlFormula,(update,empName))
                conn.commit()

                print('YOUR DETAILS ARE SUCESSFULLY UPDATED')
            elif (c2==5):
                print('THANK YOU FOR VISITING')
            elif(c2==3):
                 cust_name=input("enter the Reciever's name : ")
                 cust_address=input("enter the Address with zipcode : ")
                 bill=input("enter the bill cost : ")
                 sender_name=input("enter Sender's Name : ")
                 phone_no=int(input("Enter Sender's phone no : "))
                 SQL_insert="insert into address values("+"'"+ cust_name+"'"+","+"'"+cust_address+"'"+","+"'"+bill+"'"+","+"'"+sender_name+"'"+","+str(phone_no)+")"
                 c1.execute(SQL_insert)
                 conn.commit()
                 print("BILL Generated")
            elif(c2==4):
                  c1=conn.cursor()
                  c1.execute('select * from address')
                  data=c1.fetchall()
                  count=c1.rowcount
                  print('Total package for this month  is',count)
                  for row in data:
                     print(row)
                  print("VISIT AGAIN")
            elif (c2==6):
                print('RATE US FOR SERVICE')
                rating=int(input("On the Scale of 10 how would you like to rate us:"))
                print('THANK FOR RATING')
            else:
                print("Oops,Something went Wrong...........")

        
     if choice==3:
      print("THANK YOU FOR VISITING")
      cl.close
               
                 
            
