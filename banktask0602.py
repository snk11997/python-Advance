print("\t\t\tSTATE BANK OF INDIA")
print("\t\tEnter your card")
a=input("user name").lower()
b=int(input("Enter your password"))

if a=="naveen" and b==12345678:
    print("your balance 50000")
    e=50000 
    print("1.Deposit \n 2.Withdraw \n 3.Banking")
    print("select any one")
    c=int(input("write a num"))
    if c==1:
        print("enter your amount")
        d=int(input())
      
        if d>=10000 and d<=40000:
          print("amount credited to your account")
          x=d+e
          print("Total balance" , x)
        else:
          print("Range 10000 to 40000")

    elif c==2:
        print("your balance 50000")
        print("enter your withdraw amount")
        e=50000 
        f=int(input())
        if f>1000 and f<10000:
            print("amount debited")
            g=f-e
            print("total balance", g)
        else:
          print("range of 1000 to 10000")
    elif c==3:
        print("1.cheque book request 2.mobile change request")
        print("select any one")
        z=int(input())
        if z==1:
            print("request sumbmitted to branch")
            print("Chque book will sended to your postoffice")
        elif z==2:
             print("Message request sended to bank")
             print("bank will updated on your requsest")
        else:
             print("invalid data ")
            
    else:
        print("select correct option")
    


else:
    print("user data is wrong")
    


          
                
          
      
       
      
      

