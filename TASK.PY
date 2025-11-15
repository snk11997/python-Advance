class bank:
        def bank_details(self):
            print("bank name:SBI , IFSC CODE: SBI0084 , LOCATION: CHENNAI")  
                     
class staff:
    n=[]
    def new_staff(self):
         for i in range(20):
            try :
                name=input("enter the name")
                phone=int(input("enter the phone number"))
                location=input("enter the location ")
                email=input("enter the email address")
            except ValueError:
                print("give the  value")
            else:
                self.n.extend([name,phone,location,email])
                break
    def current_staff(self):
        for i in range(0,len(self.n),5):
            print(self.n[i])                 
    def customer(self):
        for i in range(0,len(self.n2),6):
              print(self.n2[i])                   
class customer(bank,staff):
    n2=[] 
    def new_customer(self):         
         name=input("enter the name")
         branch=input("enter the branch")
         acc_no=int(input("enter the acc no"))
         phone=int(input("enter the phone number"))
         location=input("enter the location ")
         email=input("enter the email address")
         self.n2.extend([name,branch,acc_no,phone,location,email])   

obj=customer()
obj.bank_details()                                              

for i in range(20):
     print("1.staff , 2.customer , 3.Exit")
     a=int(input("select any one"))
     if a==1:
         print("1. New staff entry, 2.current staff checking , 3. current customer checking")
         b=int(input("select any one"))
         if b==1:
            obj.new_staff()
         elif b==2:
             obj.current_staff()                 #current staff name
         elif b==3:
             obj.customer_details()                      #Disply all customer name 
     elif a==2:
         print("1.new customer ")
         x2=int(input("select any one"))
         if x2==1:
             obj.new_customer()
               
     elif a==3:
            break 
     else:
          print("select correct option ") 
        



    





