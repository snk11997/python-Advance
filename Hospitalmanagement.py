a="HOSPITAL MANAGEMENT"
print(a.center(80,"*"))
print("1.Admin,2.Patient")
b=int(input("select any one"))
if b==1:
  c=int(input("1.sign up 2.login"))
  if c==1:
    print("enter your name")
    b=input()
    print("enter your password")
    c=input()
    x=len(c)
    if x>=8:
           if "1" in c or "2" in c or "3" in c or "4" in c or "5" in c or "6" in c or "7" in c or "8" in c or "9" in c or "0" in c:
                if "!" in c or "@" in c or "#" in c or "%"in c or "^" in c or "&" in c or "*" in c or "$" in c:
                                           
                    print(" account created  sucessfully")
                    print("1.uploaded details 2. Modifity details")
                    d=int(input("select any one"))
                    if d==1:
                        print("number of patients 3")
                        e=input(" patient name : ").upper()  
                        f=input(" patient ID : ")
                        g=input(" Disease name : ").upper()
                        h=input(" Admitted date: ")
                        i=input(" patient name : ").upper()
                        j=input(" patient ID : ")
                        k=input(" Disease name : ").upper()
                        l=input(" Admitted date: ")
                        m=input(" patient name : ").upper()
                        n=input(" patient ID : ")
                        o=input(" Disease name : ").upper()
                        p=input(" Admitted date: ")
                        print("uploaded sucessfully")
                        print("1.Admin 2.Patient")
                        op=int(input())

                        if op==2:
                              print("Enter the login details ")
                              m=input("enter username")
                              n=input("enter password")
                              if m==b and n==c:
                                     print("login sucessfully") 
                                     print("1.patient Name 2.Patient ID 3.Disease 4. Admit date")

                                     r=int(input("select any one "))
                                     if r==1  :
                                           q=input("enter a patient name")
                                           if q==e :
                                            print("e,f,g,h")
                                           if q==i :
                                            print("i,j,k,l")
                                           if q==m:  
                                             print("m,n,o,p")
                                           if not (q==e or q==i or q==m):
                                              print(" your input datails not availble in our database")

                                     if r==2:
                                         q=int(input("enter a patient ID"))
                                         v=int(input("enter a patient ID"))
                                         if  q>=10 and 100<=v:
                                             print("Arun,15,FEVER,15-01-2020")
                                         if q>=100 and 200<=v :
                                              print("kumar,115,cold,14-02-2009")
                                              print("mathan,155,FEVER,13-09-2023") 
                  
                                         if not((q>=100 and 200<=v) or (q>=10 and 100<=v)):
                                             print(" your input datails not availble in our database")

                                     if r==3:
                                         q=input("enter a disease")
                                         if q==g :
                                              print("Arun,15,FEVER,15-01-2020")
                                         if q==k :
                                               print("kumar,115,cold,14-02-2009")
                                         if q==o:  
                                               print("mathan,155,FEVER,13-09-2023")
                                         if not(q==g or q==k or q==o):
                                                print(" you input data not availble in our database")

                                     if r==4:
                                         q=input("enter Admit date")

                                         if q==h :     

                                             print("Arun,15,FEVER,15-01-2020")
                                         if q==l:
                                             print("kumar,115,cold,14-02-2009")
                                         if q==p:
                                              print("mathan,155,FEVER,13-09-2023")
                                         if not(q==h or q==l or q==p):
                                                print(" you input data not availble in our database")
                                     else:
                                          print("enter the correct option") 



                              else:
                                  print("invalid crendentials")
                
                    else:
                         print("min 1 special ")
           else:
               print("MIn 1 number")
    else:   
        print("min 8 character")

  else:
     print("You have to signup first")

else:
    print("Uploaded details first")








###int(q[6:])>2020 or (int(q[6:] ==2020 and int(q[3:5]>01 or (int(q[3:5]==01 and int(q[0:2])> 15 or (int(q[0:2])== 15))):

##elif b==2:
##    print("Enter login Details")
##    m=input("enter username")
##    n=input("enter password")
##    if m==b and n==c:
##         print("login sucessfully")
##         print("1.patient Name 2.Patient ID 3.Disease 4. Admit date")
##         r=input("select any one")
##         if r==1:
##             q=input("enter a patient name")
##             if q==e :
##                  print("Arun,15,FEVER,15-01-2020")
##             if q==i :
##                  print("kumar,115,cold,14-02-2009")
##             if q==m:  
##                  print("mathan,155,FEVER,13-09-2023")
##             else:
##                 print(" your input datails not availble in our database")
##
##         if r==2:
##            q=input("enter a patient ID")
##            v=input("enter a patient ID")
##            if  q>=10 and 100<=v:
##                  print("Arun,15,FEVER,15-01-2020")
##            if q>=100 and 200<=v :
##                  print("kumar,115,cold,14-02-2009")
##                  print("mathan,155,FEVER,13-09-2023") 
##                  
##            else:
##                 print(" your input datails not availble in our database")
##
##         if r==3:
##            q=input("enter a disease")
##            if q==g :
##                  print("Arun,15,FEVER,15-01-2020")
##            if q==k :
##                  print("kumar,115,cold,14-02-2009")
##            if q==o:  
##                  print("mathan,155,FEVER,13-09-2023")
##            if not(q==g or q==k or q==o):
##                 print(" you input data not availble in our database")
##
##         if r==4:
##            q=input("enter Admit date")
##
##            if q==h :     #int(q[6:])>2020 or (int(q[6:] ==2020 and int(q[3:5]>01 or (int(q[3:5]==01 and int(q[0:2])> 15 or (int(q[0:2])== 15))):
##
##                  print("Arun,15,FEVER,15-01-2020")
##            if q==l:
##                  print("kumar,115,cold,14-02-2009")
##            if q==p:
##                  print("mathan,155,FEVER,13-09-2023")
##            else:
##                  print(" you input data not availble in our database")
##
##
##
##    else:
##         print("invalid crendentials")
##    
##    
    


     



