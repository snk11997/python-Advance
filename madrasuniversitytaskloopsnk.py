def stdd():
       s01=input("enter  student name")
       s1=int(input("enter register number"))
       s2=int(input("enter a tamil mark"))
       s3=int(input("enter english mark"))
       s4=int(input("enter maths mark"))
       s5=int(input("enter science mark"))
       s6=int(input("enter social mark"))                      
       print("Uploaded sucessfully")
       v.extend([s01,s1,s2,s3,s4,s5,s6])
def fun1():
        print("enter the name to view result")
        j=input("enter student name")       
        for n2 in range(0,len(v),7):          
          if  v[n2]==j:
             if v[n2+2]>35 and v[n2+3]>35 and v[n2+4]>35 and v[n2+5]>35 and v[n2+6]>35:
                  print("PASS")                    
             else:
                  print("FAIL")                                                              
             print("1.View again  2.exit")
             k=int(input("select any one")) 
             if k==1:
                   fun1()
             elif k==2:
                   print("program ended")                   
                   break                                                               
          else:
                print("enter a valid name") 
x="Madras university"
print(x.center(80,"*"))
v,v3=[],[]
n=1
for i in range(100):
    print("1.Admin 2. user  3.Exit")
    y=int(input("select any one"))
    if y==3:
       break
    if y==1:
        for i22 in range(100):    
           print("1.upload ,2.back")
           v2=int(input("seelct any one"))
           if v2==2:
                 break        
           if v2==1:                                                    
              stdd()
    if y==2:
       for i in range(200):
            print("1.sigin 2. log in , 3. Exit") 
            c=int(input("select any one"))
            if c==1:
              a=input("enter usernmae")
              for i8 in range(100):
                b=input("enter password")
                if len(b)>8:
                    if "1" in b or "2" in b or "3" in b or "4" in b or "5" in b or "6" in b or "7" in b or "8" in b or "9" in b or "0" in  b:
                          if "@" in b or "!" in b or "#" in b or "$" in b or "%" in b or "&" in b or "*" in b:
                                    print("registerd sucessfully")                                   
                                    v3.extend([a,b])
                                    break
                          else:
                                print("minimum one character")
                                continue
                    else:
                          print("minimum one number")
                          continue
                else:
                       print("Minimum 8 character")
                       continue   
            elif c==3:        
                break                
            elif c==2:
              for i6 in range(3): 
                 print("Enter the login details")
                 g=input("enter a user name")
                 h=input("enter password")
                 
                 if g in v3 and h in v3:
                    print("Log in sucessfully")  
                    for i in  range(20):  
                      fun1()
                    if n==1:
                        break                             
                 else:
                   print("enter a correct password and user name ")
                









                             
                                        
                                    
                            
                             
                         

                
                        
                        
                       
                       
                       
                     
                     
                 
                 
                 
                 
                 
                    


            
    

