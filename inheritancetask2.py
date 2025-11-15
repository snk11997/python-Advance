class bank:
    def bank_details(self):
        self.bank_name="SBI"
        self.IFSC_code=["114SB","115SB","116SB","117SB","118SB"]
        self.branch=["kodampakkam","annanagar","setpet","arumbakkam","avadi"]
        display=list(zip(self.IFSC_code,self.branch))
        print(self.bank_name,display)
        self.n=[]
        self.n2=[]
    def branch_data_modify(self):
        print(self.branch)
        print(self.IFSC_code)
        x1=input("enter the exiting branch name")
        for i in range(0,len(self.branch)):
            if x1==self.branch[i]: 
                self.branch[i]=input("enter the new branch name")
                print(self.branch)               
                self.IFSC_code[i]=input("enter the IFSC CODE")
                print(self.IFSC_code)            
class staff:   
    def new_staff(self):
         name=input("enter the name")
         print(self.branch)
         print("select any one")   
         branch=input("enter branch name")
         for i in range(0,len(self.branch)):
                if branch==self.branch[i]:                    
                     IFSC_code2=self.IFSC_code[i]
         phone=int(input("enter the phone number"))
         location=input("enter the location ")
         email=input("enter the email address")
         self.n.extend([name,branch,IFSC_code2,phone,location,email])
    def current_staff(self):
        print(" 1.Name ,2.Branch 3.All Details")   
        a1=int(input("selct ant one"))
        if a1==1:
            for i in range(0,len(self.n),6):
              print(self.n[i])  # Display all staff name        
        if a1==2:
            print(self.branch)
            b3=input("enter the branch name")
            for i in range(1,len(self.n),6):
              if b3==self.n[i]:   
                   print(self.n[i-1])   #Disply all branchs to you select any one branch view the staff name          
        if a1==3:
            print(self.n)  # ALL Details             
    def customer_details(self):
        print("1.branch 2.Name , 3.ID")
        a2=int(input("select ant one"))
        if a2==1:
            print(self.branch)
            b2=int(input("select any one branch"))
            for i in range(1,len(self.n2),7):
                 if self.n2[i]==b2:
                      print(self.n2[i-1])   # sow branches  next branch wise customer name          
        elif a2==2:
                print(self.n2)
                for i in range(0,len(self.n2),7):
                      print(self.n2[i])      # DIsply all customer name                    
        elif a2==3:
            a3=int(input("enetr the ID"))
            for i in range(3,len(self.n2),7):
                 if self.n2[i]==a3:             # get input & Display that customer details
                      print(self.n2[i-3])
                      print(self.n2[i-2])
                      print(self.n2[i-1])
                      print(self.n2[i+0])
                      print(self.n2[i+1])
                      print(self.n2[i+2])
                      print(self.n2[i+3])        
class customer(bank,staff):
    def __init__(self,idn=200):
         self.idn=idn
    def new_customer(self):
        total=int(input("how mony customer details , you will update"))        
        for i in range(total):
            name=input("enter the customer name")
            print(self.branch ,"\n select any one")
            branch=input("enter branch")
            for i in range(0,len(self.branch)):
                if self.branch[i]==branch:
                     IFSC_code2=self.IFSC_code[i]
                # IFSC code Automatic asigned
            self.idn=self.idn+1
            unique_ID=self.idn  # Automatic
            phone=int(input("enter the phone number"))
            location=input("enter the location ")
            email=input("enter the email address")
            self.n2.extend([name,branch,IFSC_code2,unique_ID,phone,location,email])
        print(self.n2)   
    def modify(self):
            print("1.name & Display all CUSTOMER name $ modify ")
            for i in range(0,len(self.n2),7):
                  print(self.n2[i])
            print("which user you are modifying, enter the name ")
            cusname=input("enter the customer name")
            print("1.branch modify, 2.phone number modify")
            a3=int(input("select any one"))
            if a3==1:
                    for j in range(0,len(self.n2),7):
                        if  cusname==self.n2[j]:
                            old=input("enter old branch name")
                            print(self.branch)
                            new1=input("enter new  branch name")
                            self.n2[j+1]=new1 
                            for k in range(0,len(self.branch)):
                                if self.branch[k]==new1 :
                                     #self.branch[k]=new1
                                     self.n2[j+2]=self.IFSC_code[k]
            elif a3==2:
                    for i in range(0,len(self.n2),7):
                        if cusname==self.n2[i]:
                            self.n2[i+4]=int(input("enter the mobile number"))
                            print(self.n2[i+4])
            print(self.n2)
obj=customer()
obj.bank_details()                                              
for i in range(20):
     print("1.branch_data_modify ,2.staff , 3.customer , 4.Exit")
     a=int(input("select any one"))
     if a==1:
          obj.branch_modify()
     elif a==2:
         print("1. New staff entry, 2.current staff checking , 3. current customer checking")
         b=int(input("select any one"))
         if b==1:
            obj.new_staff()
         elif b==2:
             obj.current_staff()                 #current staff name
         elif b==3:
             obj.customer_details()                      #Disply all customer name 
     elif a==3:
         print("1.new customer 2. customer details modify")
         x2=int(input("select any one"))
         if x2==1:
             obj.new_customer()
         if x2==2:
             obj.modify()              
     elif a==4:
            break 
     else:
          print("select correct option ") 
        




            
        






 

    
         

    
        












