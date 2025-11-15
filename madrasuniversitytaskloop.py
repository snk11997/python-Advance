x="Madras university"
print(x.center(80,"*"))
for i in range(100):
    print("1.Admin 2. Student")
    y=int(input("select any one"))
    if y==1:
        break
    if y==2:
        print("doesnot have account so plesase sigin first")
for i in range(100):
    print("1.sigin 2. uploaded details 3. Exit") 
    c=int(input("select any one"))
    if c==1:
            a=input("enter usernmae") 
            for i in range(100):
                b=input("enter password")
                if len(b)>8:
                    if "1" in b or "2" in b or "3" in b or "4" in b or "5" in b or "6" in b or "7" in b or "8" in b or "9" in b or "0" in  b:
                          if "@" in b or "!" in b or "#" in b or "$" in b or "%" in b or "&" in b or "*" in b:
                                    print("registerd sucessfully")
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
    if c==2:
            
                       print(" number of students 3")
                       s1=input("enter  student name")
                       s2=int(input("enter a tamil mark"))
                       s3=int(input("enter english mark"))
                       s4=int(input("enter maths mark"))
                       s5=int(input("enter science mark"))
                       s6=int(input("enter social mark"))                     
                       s7=input("enter  student name")
                       s8=int(input("enter a tamil mark"))
                       s9=int(input("enter english mark"))
                       s10=int(input("enter maths mark"))
                       s11=int(input("enter science mark"))
                       s12=int(input("enter social mark"))                      
                       s13=input("enter  student name")
                       s14=int(input("enter a tamil mark"))
                       s15=int(input("enter english mark"))
                       s16=int(input("enter maths mark"))
                       s17=int(input("enter science mark"))
                       s18=int(input("enter social mark"))                      
                       print("Uploaded sucessfully")                   
    if c==3:
        
            break
print("1.Admin 2.Student")
f=int(input("select any one"))
if f==2:
 for i in range(100):
     print("Enter the login details")
     g=input("enter a user name")
     h=input("enter password") 
     if g==a and h==b:
             for i in range(100):
                print("enter the name to view result")
                j=input("enter student name")
                if  s1==j:
                    if s2>35 and s3>35 and s4>35 and s5>35 and s6>35:
                           print("PASS")
                           print("1.View again  2.exit")
                           k=int(input("select any one"))
                           if k==1:
                             continue
                           else:
                             print("program ended")
                    else:
                          print("FAIL")
                          print("1.View again  2.exit")
                          k=int(input("select any one"))                                                    
                          if k==1:
                                 continue
                          else:
                                 print("program ended")
                elif s7==j:
                        if s8>35 and s9>35 and s10>35 and s11>35 and s12>35:
                                     print("PASS")
                                     print("1.View again  2.exit")
                                     k=int(input("select any one"))
                                     if k==1:
                                        continue
                                     else:
                                        print("program ended")
                        else:
                          print("FAIL")
                          print("View again  2.exit")
                          k=int(input("select any one"))                                                    
                          if k==1:
                                 continue
                          else:
                                  print("program ended")
                elif s13==j:
                        if s14>35 and s15>35 and s16>35 and s17>35 and s18>35:
                                        print("PASS")
                                        print("View again  2.exit")
                                        k=int(input("select any one"))
                                        if k==1:
                                            continue
                                        else:
                                            print("program ended")

                        else:
                          print("FAIL")
                          print("View again  2.exit")
                          k=int(input("select any one"))
                                                    
                          if k==1:
                                 continue
                          else:
                                  print("program ended")
                else:
                    print("enter a valid name")
                    continue
     else:
       print("enter a correct password")
       continue
                                        
                                        
                                        
                                    
                            
                             
                         

                
                        
                        
                       
                       
                       
                     
                     
                 
                 
                 
                 
                 
                    


            
    

