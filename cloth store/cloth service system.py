import mysql.connector as sql
conn=sql.connect(host="localhost", user="root", passwd="2099", database="cloth_db")
mycursor=conn.cursor()
if conn.is_connected():
    print("Conection With Database Establised Successfully")
else:
    print("Conection With Database Failed XXX")


print("Welcome to Aditya cloth store")

c1=conn.cursor()
choice = 0
while choice != 3:
    print("1.CREATE YOUR ACCOUNT")
    print("2.LOG IN")
    print("3.EXIT")
    choice=int(input("ENTER YOUR CHOICE:"))
    if choice ==1:
     v_cust_name=input("Enter the customer name :")
     v_account_no=int(input("enter your User ID "))
     v_password=int(input("Enter your Passkey :"))
     v_SQL_insert="insert into log_in values('"+v_cust_name+"',"+str(v_account_no)+","+str (v_password)+")"
     c1.execute(v_SQL_insert)
     conn.commit()
     print("ACCOUNT CREATED")

    if choice==2:
     print('')
     print('Enter your Credentials')
     cust_name=input('Enter your name : ')
     print('')
     v_account_no=int(input('Enter your User ID  '))
     print(' ')
     v_password=int(input('Enter your Passkey : '))
     print(' ')
     c1=conn.cursor()
     c1.execute('select * from log_in')
     data=c1.fetchall()
     count=c1.rowcount
     for row in data:
        if (cust_name in row) and (v_account_no in row):
            print(' ')
            print(' ')
            print("WELCOME TO Aditya cloth store")
            print(' ')
            print(' ')
            print('TO SEE  DETAILS of Customer PRESS   :1')
            print(' ')
            print('TO UPDATE DETAILS PRESS             :2')
            print(' ')
            print('TO EXIT PRESS                       :3')
            print(' ')
            print('TO pay the bill  of the shopping    :4')
            print(' ')
            print('TO SEE your Details                 :5')
            print(' ')
            print('WANT TO RATE US ?                   :6')
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
                sqlFormula = "UPDATE log_in SET v_cust_name=%s WHERE v_cust_name = %s"
                c1.execute(sqlFormula,(update,empName))
                conn.commit()

                print('YOUR DETAILS ARE SUCESSFULLY UPDATED')
            elif (c2==3):
                print('THANK YOU FOR VISITING')
            elif(c2==4):
                 v_employ_name=input("enter the employ name")
                 v_item =input("enter the item name:")
                 v_bill=int(input("enter the item's price"))
                 v_cust_name=input("enter costumer Name:")
                 v_phone_no=int(input("Enter costumer phone no:"))
                 v_SQL_insert="insert into sales_cloth values("+"'"+ v_employ_name+"'"+","+"'"+v_item+"'"+","+"'"+str(v_bill)+"'"+","+"'"+v_cust_name+"'"+","+"'"+str(v_phone_no)+"'"+")"
                 c1.execute(v_SQL_insert)
                 conn.commit()
                 print("payment Successfull")
            elif(c2==5):
                  c1=conn.cursor()
                  c1.execute('select * from sales_cloth ')
                  data=c1.fetchall()
                  count=c1.rowcount
                  print('total bill of this shopping  is',count)
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
               
                 
            
