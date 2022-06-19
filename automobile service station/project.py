import mysql.connector as sql 
conn=sql.connect(host='localhost',user='root',passwd='2099',database='auto')
if conn.is_connected():
    print("Successfully Connected")
else:
    print("Conection With Database Failed XXX")
print("welcome automobile service station")

c1=conn.cursor()
print("Automobile")
print("1. service station")
print("2. source")
print("3. selling")
print("4. Exit")
choice=int(input("Enter the Choice - "))
if choice==1:
    v_sno=int(input("Enter the serial Number: "))
    v_cname=input("Enter the customer name : ")
    v_cdetails=input("Enter the customer details: ")
    v_caddress=input("Enter the customer address: ")
    v_cpincode=int(input("Enter the pincode: "))
    v_cpuramt=int(input("Enter the pur amt: "))
    v_cdisc=int(input("Enter the discount: "))
    V_SQL_Insert = "insert into customer_details values (" + str( v_sno) + ","+"'" + v_cname + "'"+","+"'"+ v_cdetails + "'"+","+"'"+ v_caddress+"',"+","+str(v_cpincode )+","+ str(v_cpuramt )+" ," +str(v_cdisc)+" )"
    c1.execute(V_SQL_Insert)
    conn.commit()
print("CUSTOMER Created Congrats!!!")
   
if choice == 2:
    username=input('USERNAME:')
    password=input('PASSWORD:')
    c1.execute("select * from user where username = '' and passwd = ''".format(username , password))
    data = c1.fetchall()
    if any(data) :
        import main
    else:
        print('''try again''')

