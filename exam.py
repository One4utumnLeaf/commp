def output():
    print("Welcome to Student Fund Management Sysytem")
    print("What operation do you want to perform")
    while True:
            ch=int(input("1-Input data\n 2-Update data\n 3-Delete data\n4-Analyse data\n5-Exit"))
            if ch==1:
                ip()
            elif ch==2:
                update()
            elif ch==3:
                delete()
            elif ch==4:
                analyse()
            elif ch==5:
                print("Exiting program")
                break
            else:
                print("Wrong choice entered")
                print("Enter correct choice")

def update():
    c=int(input("Enter the code of the student whose payment details are to be changed"))
    l=[]
    with open("fund_database.csv","r",newline="") as a:
        b=csv.reader(a)
        for i in b:
            l.append(i)
    with open ("fund_database.csv","w",newline="") as a:
        b=csv.writer(a)
        for i in l:
            if i[0]==c:
                print("Student name : ",i[1])
                print("Reason for payment : ",i[2])
                print("Payment method : ",i[3])
                print("Amount payed : Rs.",i[4])
                print("What would you like to update")
                while True:
                    ch=int(input("1-Students name \n2-Reason for payment \n3-Payment method \n4-Amount payed\n5-Done with updation"))
                    if ch==1:
                        n=input("Enter new name")
                        i[1]=n
                    elif ch==2:
                        r=input("Enter new reason")
                        i[2]=r
                    elif ch==3:
                        m=input("Enter new payment method")
                        i[3]=r
                    elif ch==4:
                        a=int(input("Enter new amount payed"))
                        i[4]=a
                    elif ch==5:
                        break
                    else :
                        print("Wrong choice entered")
                        print("Please enter correct choice")
                b.writerows(l)
                print("Data updated successfully")
                break
            else:
                print("Code not found")
        
        
            
    
        
    
