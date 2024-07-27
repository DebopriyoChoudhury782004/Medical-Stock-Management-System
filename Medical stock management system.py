import mysql.connector as sqltor
def input_purchase_details():
    mycon=sqltor.connect(host="localhost",user="root",passwd="root",database="MSMS")
    if mycon.is_connected()==False:
        print('Error connecting to MySQL database')
    else:
        c=int(input("Enter the code of the medicine:- "))
        m=input("Enter the name of the medicine:- ")
        p=float(input("Enter the cost price of the medicine:- "))
        q=int(input("Enter the quantity of the medicine:- "))
        md=input("Enter manufacturing date:- ")
        ed=input("Enter expiry date:- ")
        n=input("Enter the name of the supplier:- ")
        cursor=mycon.cursor()   
        st="insert into purchase_details values({},'{}',{},{},'{}','{}','{}')".format(c,m,p,q,md,ed,n)
        cursor.execute(st)
        mycon.commit()
        print("Purchase details added successfully...")
        st="insert into stock_details values({},'{}',{},{},{},'{}','{}')".format(c,m,p,p+p*20/100,q,md,ed)
        cursor.execute(st)
        mycon.commit()
        print("Stock details added successfully...")
        mycon.close()
def display_purchase_details():
    mycon=sqltor.connect(host="localhost",user="root",passwd="root",database="MSMS")
    if mycon.is_connected()==False:
        print('Error connecting to MySQL database')
    else:
        cursor=mycon.cursor()   
        st="select * from purchase_details"
        cursor.execute(st)
        data=cursor.fetchall()
        count=cursor.rowcount
        if count>=1:
            for c in range(count):
                t1=data[c]
                print("\nDETAILS OF MEDICINE",c+1)
                print("CODE:",t1[0])
                print("NAME:",t1[1])
                print("COST PRICE:",t1[2])
                print("QUANTITY:",t1[3])
                print("MANUFACTURING DATE:",t1[4])
                print("EXPIRY DATE:",t1[5])
                print("NAME OF THE SUPPLIER:",t1[6])
        else:
            print("NO RECORDS FOUND")
    mycon.close()
def display_stock_details():
    mycon=sqltor.connect(host="localhost",user="root",passwd="root",database="MSMS")
    if mycon.is_connected()==False:
        print('Error connecting to MySQL database')
    else:
        cursor=mycon.cursor()   
        st="select * from stock_details"
        cursor.execute(st)
        data=cursor.fetchall()
        count=cursor.rowcount
        if count>=1:
            for c in range(count):
                t1=data[c]
                print("\nDETAILS OF MEDICINE",c+1)
                print("CODE:",t1[0])
                print("NAME:",t1[1])
                print("COST PRICE:",t1[2])
                print("SELLING PRICE:",t1[3])
                print("QUANTITY:",t1[4])
                print("MANUFACTURING DATE:",t1[5])
                print("EXPIRY DATE:",t1[6])
        else:
            print("NO RECORDS FOUND")
    mycon.close()
def input_sales_details():
    mycon=sqltor.connect(host="localhost",user="root",passwd="root",database="MSMS")
    if mycon.is_connected()==False:
        print('Error connecting to MySQL database')
    else:
        s=int(input("Enter the Sales id:- "))       
        n=input("Enter the name of the customer:- ")
        p=input("Enter the phone number of the customer:- ")
        cursor=mycon.cursor()   
        st="insert into Sales_cust_details values({},'{}','{}')".format(s,n,p)
        cursor.execute(st)
        mycon.commit()
        amt=0
        while True:
            c=int(input("Enter the code of the medicine:- "))
            q=int(input("Enter the quantity of the medicine:- "))
            st3="select mqty,msp from stock_details where mcode={}".format(c)
            cursor.execute(st3)
            data=cursor.fetchall()
            count=cursor.rowcount
            if count>=1:                
                qty=data[0][0]
                sp=data[0][1]
                if qty<q:
                    print("ONLY",qty,"ARE STRIPS ARE AVAILABLE")
                else:
                    st="insert into Sales_medi_details values({},{},{})".format(c,q,s)
                    cursor.execute(st)
                    st2="update stock_details set mqty={} where mcode={}".format(qty-q,c)
                    cursor.execute(st2)
                    mycon.commit()
                    amt=amt+sp*q
                    ch=input("Do you want to add more medicine(y/n)?")
                    if ch.lower()=='n':
                        print("Amount Payable:-",amt)
                        print("Sales details added successfully...")
                        print("Stock details updated successfully...")                        
                        break
                    
            else:
                print("NO MEDICINE FOUND WITH MEDICINE CODE:-",c)
        mycon.close()           
def display_all_sales_details():
    mycon=sqltor.connect(host="localhost",user="root",passwd="root",database="MSMS")
    if mycon.is_connected()==False:
        print('Error connecting to MySQL database')
    else:
        cursor=mycon.cursor()   
        st="select * from sales_cust_details c,sales_medi_details m where c.Sales_id=m.sales_id"
        cursor.execute(st)
        data=cursor.fetchall()
        count=cursor.rowcount
        if count>=1:
            print("-----SALES DETAILS-----")
            for c in range(count):
                t1=data[c]
                print("SALES ID:",t1[0])
                print("CUSTOMER NAME:",t1[1])
                print("CUSTOMER PHONE NUMBER:",t1[2])
                print("MEDICINE CODE",t1[3])
                print("MEDICINE QUANTITY",t1[4])
        else:
            print("NO RECORDS FOUND")
    mycon.close()
ch='y'
while ch=='y':
    print("\n----------MENU----------")
    print("1.Input purchase details")
    print("2.Display purchase details")
    print("3.Display stock details")
    print("4.Input sales details")
    print("5.Display all sales details")
    i=int(input("Enter your choice(1/2/3/4/5): "))
    if i==1:
        input_purchase_details()
    elif i==2:
        display_purchase_details()
    elif i==3:
        display_stock_details()
    elif i==4:
        input_sales_details()
    elif i==5:
        display_all_sales_details()
    else:
        print("Please enter a valid option...")
    ch=input("Do you want to continue(y/n)? ")
print("Thank you...")
