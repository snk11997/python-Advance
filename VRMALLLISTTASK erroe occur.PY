a="VR MALL"
print(a.center(120,"*"))
print("1.Admin 2.user")
t1,t2,t3,t4,t5,t6,t7,t8,t9=[],[],[],[],[],[],[],[],[]
tm,tm2,tm3=[],[],[]
q,q1,q2,q3,q4,q5,q6,q7,q8,=0,0,0,0,0,0,0,0,0
x=0

b=int(input("select any one"))
if b==2:
      for i in range(100):
            print("1.sig in , 2 .log in ")
            c=int(input("select any one"))
            if c==1:
                d=input("enter the user name")
                for i in range(100):
                   e=input("enter the password")
                   if len(e)>8 :
                      if "1" in e or "2" in e or "3" in e or "4" in e or "5" in e or "6" in e or "7" in e or "8" in e or "9" in e or "0" in  e:
                          if "@" in e or "!" in e or "#" in e or "$" in e or "%" in e or "&" in e or "*" in e:
                                  print("sign in sucessfully")
                                  break
            
                          else:
                              print("minimu one special charcter")

                      else:
                          print("minimum one number")
      
                   else:
                        print("minimum 8 character")
         
            if c==2:
               for a1 in range(100):
                  f=input("enter the user name")
                  g=input("enter the password")
                  if d==f and e==g:
                       print("log in sucessfully")
                       for a2 in range(100):
                  
                           mv=["siram",4,["10.00AM","12.00PM","4.00PM","7.00PM"],"leo",3,["12.00PM ","5.00PM","10.00PM"],"joe",2,["4.00PM","7.00PM"]]  
                           print(mv)                                                             
                           for i in range(2,len(mv),3):                                 
                                
                                       if mv.index(mv[i])==2:
                                           for j in mv[i]:
                                              tm.append(j)
                                       if mv.index(mv[i])==5:
                                             for j in mv[i]:
                                                 tm2.append(j)
                                       if mv.index(mv[i])==8:
                                             for j in mv[i]:
                                                  tm3.append(j)
                                                  
                                       
                                                  
                           print(tm , tm2 ,tm3 )
                           
                           h1=input("select any one movie")
                           for a3 in range(0,len(mv),3):                          
                               if  mv[a3]==h1 :
                                   print("no of shows" ,mv[a3+1])
                                   print("Timings" ,mv[a3+2])                                                                                                                                       
                                   k=input("select the time")
                                   for a4 in tm:                           
                                      if a4==k:                              
                                          print("number of tickets available")
                                          if q==0:
                                               for i in range(1,101,10):
                                                    for j in range(i,i+10):
                                                         print(j , end=" ")
                                               
                                                    print()
                                          if q>=1:
                                               for i in range(1,101,10):
                                                     for j in range(i,i+10):                                
                                                          if j in t1:
                                                              print("X", end=" ")
                                                     else:                                                   
                                                           print(j , end=" ")

                                                     print()

                                      
                                          m=int(input("enter the number of ticket"))
                                          for a5 in range(m):
                                                l=int(input("select seat number"))
                                                t1.append(l)
                                          print(" you ticket has been  booked sucessfully")
                                          print( " your booking is" ,t1)                                  
                                          print("Availble tickets")
                                          for i in range(1,100,10):
                                               for j in range(i,i+10):
                                                   if j in t1 :
                                                       print("X", end=" ")

                                                   else:
                                                       print(j ,end=" ")
                                               print()
                                          q=q+1
                                          print("thanks for purchasing")
                                          
                                      if a4==k:
                                            print("number of tickets available")
                                            if q1==0:
                                                 for i in range(1,101,10):
                                                       for j in range(i,i+10):
                                                           print(j , end=" ")
                                                 print()
                                               
                                            if q1>=1:
                                                for i in range(1,101,10):
                                                     for j in range(i,i+10):                                
                                                         if j in t2:
                                                             print("X", end=" ")
                                                         else:                                                   
                                                             print(j , end=" ")

                                                     print()           
                                  

                                      
                                            m2=int(input("enter the number of ticket"))
                                            for i in range(m2):

                                                l2=int(input("select seat number"))
                                                t2.append(l2)
                                            print(" you ticket has been  booked sucessfully")
                                            print( " your booking is" ,t2)                                  
                                            print("Availble tickets")
                                            for i in range(1,100,10):
                                                   for j in range(i,i+10):
                                                        if j in t2 :
                                                           print("X", end=" ")

                                                        else:
                                                             print(j ,end=" ")
                                                   print()
                                            print("thanks for purchasing")
                                            print("1.book again 2.LOG OUT")
                                            a1=int(input("select any one"))
                                            q1=q1+1
                                            if a1==2:
                                              break
                                      if a4==k:
                                             print("number of tickets available")
                                             if q2==0:
                                                 for i in range(1,101,10):
                                                     for j in range(i,i+10):
                                                          print(j , end=" ")
                                         
                                                     print()
                                             if q2>=1:
                                                   for i in range(1,101,10):
                                                        for j in range(i,i+10):                                
                                                                if j in t3:
                                                                    print("X", end=" ")
                                                                else:              
                                                                    print(j , end=" ")
                                                        print()
                                

                                
                                             m3=int(input("enter the number of ticket"))
                                             for i in range(m3):
                                                     l3=int(input("select seat number"))
                                                     t3.append(l3)
                                             print(" you ticket has been  booked sucessfully")
                                             print( " your booking is" ,t3)                                  
                                             print("Availble tickets")
                                             for i in range(1,100,10):
                                                           for j in range(i,i+10):
                                                                  if j in t3 :
                                                                          print("X", end=" ")

                                                                  else:
                                                                             print(j ,end=" ")

                                                           print()


                                             print("thanks for purchasing")
                                             print("1.book again 2.LOG OUT")
                                             a1=int(input("select any one"))
                                             q2=q2+1
                                             if a1==2:
                                                break                                   
                                      if a4==k:
                                              print("number of tickets available")
                                              if q3==0:
                                                  for i in range(1,101,10):
                                                        for j in range(i,i+10):
                                                              print(j , end=" ")
                                         
                                                        print()
                                              if q3>=1:
                                                        for i in range(1,101,10):
                                                             for j in range(i,i+10):                                
                                                                  if j in t4:
                                                                      print("X", end=" ")
                                                                  else:                                                   
                                                                        print(j , end=" ")

                                                             print()                                      
                                              m4=int(input("enter the number of ticket"))
                                              for i in range(m4):
                                                     l4=int(input("select seat number"))
                                                     t4.append(l4)
                                              print(" you ticket has been  booked sucessfully")
                                              print( " your booking is" ,t4)                                  
                                              print("Availble tickets")
                                              for i in range(1,100,10):
                                                          for j in range(i,i+10):
                                                             if j in t4 :
                                                                 print("X", end=" ")

                                                             else:
                                                                print(j ,end=" ")
                                                          print()
                                              print("thanks for purchasing")
                                              print("1.book again 2.LOG OUT")
                                              a1=int(input("select any one"))
                                              q3=q3+1
                                              


                                      print("1.book again 2.LOG OUT")
                                      a1=int(input("select any one"))                                         
                                      if a1==1:
                                           break 

                                    
                               elif mv[a3]==h1:
                                  print("no of shows 3")
                                  print("Timing: 12.00PM ,5.00PM,10.00PM")
                                  print("no of shows" ,mv[a3+1])
                                  print("Timings" ,mv[a3+2]) 
                                  k=int(input("select the time"))
                                  for i in range(0,len(tm2)): 
                                    if tm2[i]==k:
                                        print("number of tickets available")
                                        if q4==0:
                                            for i in range(1,101,10):
                                                 for j in range(i,i+10):
                                                     print(j , end=" ")
                                                     
                                                 print()
                                        if q4>=1:
                                            for i in range(1,101,10):
                                                 for j in range(i,i+10):                                
                                                      if j in t5:
                                                          print("X", end=" ")
                                                      else:                                                   
                                                            print(j , end=" ")

                                                 print()                                      
                                        m5=int(input("enter the number of ticket"))
                                        for i in range(m5):
                                            l5=int(input("select seat number"))
                                            t5.append(l5)
                                        print(" you ticket has been  booked sucessfully")
                                        print( " your booking is" ,t5)                                  
                                        print("Availble tickets")
                                        for i in range(1,100,10):
                                                    for j in range(i,i+10):
                                                       if j in t5 :
                                                           print("X", end=" ")

                                                       else:
                                                          print(j ,end=" ")
                                                    print()
                                        print("thanks for purchasing")
                                        print("1.book again 2.LOG OUT")
                                        a1=int(input("select any one"))
                                        q4=q4+1
                                        if a1==2:
                                            break                                                                        
                                    if tm2[i]==k:
                                        print("number of tickets available")
                                        if q5==0:
                                            for i in range(1,101,10):
                                                 for j in range(i,i+10):
                                                     print(j , end=" ")
                                                     
                                                 print()
                                        if q5>=1:
                                            for i in range(1,101,10):
                                                 for j in range(i,i+10):                                
                                                      if j in t6:
                                                          print("X", end=" ")
                                                      else:                                                   
                                                            print(j , end=" ")

                                                 print()

                                            
                                        m6=int(input("enter the number of ticket"))
                                        for i in range(m6):
                                            l6=int(input("select seat number"))
                                            t6.append(l6)
                                        print(" you ticket has been  booked sucessfully")
                                        print( " your booking is" ,t6)                                  
                                        print("Availble tickets")
                                        for i in range(1,100,10):
                                                    for j in range(i,i+10):
                                                       if j in t6 :
                                                           print("X", end=" ")

                                                       else:
                                                          print(j ,end=" ")
                                                    print()
                                        print("thanks for purchasing")
                                        print("1.book again 2.LOG OUT")
                                        a1=int(input("select any one"))
                                        q5=q5+1
                                        if a1==2:
                                            break
                                    if tm2[i]==k:
                                        print("number of tickets available")
                                        if q6==0:
                                            for i in range(1,101,10):
                                                 for j in range(i,i+10):
                                                     print(j , end=" ")
                                                     
                                                 print()
                                        if q6>=1:
                                            for i in range(1,101,10):
                                                 for j in range(i,i+10):                                
                                                      if j in t7:
                                                          print("X", end=" ")
                                                      else:                                                   
                                                            print(j , end=" ")

                                                 print()
                                            
                                        m7=int(input("enter the number of ticket"))
                                        for i in range(m7):
                                            l7=int(input("select seat number"))
                                            t7.append(l6)
                                        print(" you ticket has been  booked sucessfully")
                                        print( " your booking is" ,t7)                                  
                                        print("Availble tickets")
                                        for i in range(1,100,10):
                                                    for j in range(i,i+10):
                                                       if j in t7 :
                                                           print("X", end=" ")

                                                       else:
                                                          print(j ,end=" ")
                                                    print()
                                        print("thanks for purchasing")
                                        print("1.book again 2.LOG OUT")
                                        a1=int(input("select any one"))
                                        q6=q6+1
                                        if a1==2:
                                            break
        
                               elif mv[a3]==h1:
                                 print("no of shows 2")
                                 print("Timing: 4.00PM ,7.00PM")
                                 print("no of shows" ,mv[a3+1])
                                 print("Timings" ,mv[a3+2]) 
                                 k=int(input("select the time"))
                                 for i in range(0,len(tm3)): 
                                    if tm3[i]==k:
                                        print("number of tickets available")
                                        if q7==0:
                                            for i in range(1,101,10):
                                                   for j in range(i,i+10):
                                                     print(j , end=" ")
                                                     
                                                   print()
                                        if q7>=1:
                                            for i in range(1,101,10):
                                                 for j in range(i,i+10):                                
                                                      if j in t8:
                                                          print("X", end=" ")
                                                      else:                                                   
                                                            print(j , end=" ")

                                                 print()

                                            
                                        m8=int(input("enter the number of ticket"))
                                        for i in range(m8):
                                            l8=int(input("select seat number"))
                                            t8.append(l8)
                                        print(" you ticket has been  booked sucessfully")
                                        print( " your booking is" ,t8)                                  
                                        print("Availble tickets")
                                        for i in range(1,100,10):
                                                    for j in range(i,i+10):
                                                       if j in t8 :
                                                           print("X", end=" ")

                                                       else:
                                                          print(j ,end=" ")
                                                    print()
                                        print("thanks for purchasing")
                                        print("1.book again 2.LOG OUT")
                                        a1=int(input("select any one"))
                                        q6=q6+1
                                        if a1==2:
                                            break
                                            
                                        
                                    if tm3[i]==k:
                                        print("number of tickets available")
                                        if q8==0:
                                            for i in range(1,101,10):
                                                 for j in range(i,i+10):
                                                     print(j , end=" ")
                                                     
                                                 print()
                                        if q8>=1:
                                            for i in range(1,101,10):
                                                 for j in range(i,i+10):                                
                                                      if j in t9:
                                                          print("X", end=" ")
                                                      else:                                                   
                                                            print(j , end=" ")

                                                 print()
                                        m9=int(input("enter the number of ticket"))
                                        for i in range(m9):
                                            l9=int(input("select seat number"))
                                            t9.append(l9)
                                        print(" you ticket has been  booked sucessfully")
                                        print( " your booking is" ,t9)                                  
                                        print("Availble tickets")
                                        for i in range(1,100,10):
                                                    for j in range(i,i+10):
                                                       if j in t9:
                                                           print("X", end=" ")

                                                       else:
                                                          print(j ,end=" ")
                                                    print()
                                        print("thanks for purchasing")
                                        print("1.book again 2.LOG OUT")
                                        a1=int(input("select any one"))
                                        q8=q8+1
                                        if a1==2:
                                            break

##                              else:
##                                   print("enter the correct data")                                 
v=0                               
nmt=[]
if b==1:
    for i in range(100):
        print("1.New movie 2.Modify 3.Exit")
        n1=int(input("select any one"))
        mv=["siram",4,["10.00AM","12.00PM","4.00PM","7.00PM"],"leo",3,["12.00PM ","5.00PM","10.00PM"],"joe",2,["4.00PM","7.00PM"]] 
        if n1==1:
           n2=input("enter the movie name")
           n3=input("enter the Show")
           n4=input("eneter the show timings")
           mv.extend([n2,n3])
           nmt.append(n4)
           mv.append(nmt)
 
        elif n1==2:

               for i in range(100):
                           mv=["siram",4,["10.00AM","12.00PM","4.00PM","7.00PM"],"leo",3,["12.00PM ","5.00PM","10.00PM"],"joe",2,["4.00PM","7.00PM"]] 
               
                           print(mv)
                           print("select any one movie")
                           jm=input("enter the name")
                           for i in range(0,len(mv)):
                              if mv[i]==jm:
                                    
                                   print("1. shows ,  2.Timings")
                                   print("select any one ")
                                   j1=int(input("type numbr"))
                           
                                   if j1==1:
##                                      for i in range(1,len(mv),4):
                                         print(mv[i+1])
                                         a=int(input("enter the number of shows"))
                                         mv[i]=a
                                         print(mv[i+2])
                                         b=input("enter the show timings")                                         
                                         mv[i+2]=b
                                         print("Time changed")
                                   if j2==2 :
                                          if none in t1  :
                                         
                                               print(mv[i+2])                                   
                                               b1=input("enter the show timings")                                         
                                               mv[i+2]=b
                                               print("Time changed")
                                          if none in t2 :
                                         
                                               print(mv[i+2])                                   
                                               b1=input("enter the show timings")                                         
                                               mv[i+2]=b
                                               print("Time changed")
                                          if none in t3 :
                                         
                                               print(mv[i+2])                                   
                                               b1=input("enter the show timings")                                         
                                               mv[i+2]=b
                                               print("Time changed")

                                          if none in t4  :
                                         
                                               print(mv[i+2])                                   
                                               b1=input("enter the show timings")                                         
                                               mv[i+2]=b
                                               print("Time changed")
                                          if none in t5 :
                                         
                                               print(mv[i+2])                                   
                                               b1=input("enter the show timings")                                         
                                               mv[i+2]=b
                                               print("Time changed")
                                          if none in t6 :
                                         
                                               print(mv[i+2])                                   
                                               b1=input("enter the show timings")                                         
                                               mv[i+2]=b
                                               print("Time changed")
                                          if none in t7  :
                                         
                                               print(mv[i+2])                                   
                                               b1=input("enter the show timings")                                         
                                               mv[i+2]=b
                                               print("Time changed")
                                          if none in t8 :
                                         
                                               print(mv[i+2])                                   
                                               b1=input("enter the show timings")                                         
                                               mv[i+2]=b
                                               print("Time changed")
                                          if none in t9 :
                                         
                                               print(mv[i+2])                                   
                                               b1=input("enter the show timings")                                         
                                               mv[i+2]=b
                                               print("Time changed")
                                          else:
                                                print("already ticket booked this timing you can not modify this time")

                           v=v+1
                           if v==1:
                                 break
                              

        elif n1==3:
            break
           
    
        
           
 ##                                         if  mv[0]==jm and mv[i]==jm :
##                                                  while a>0:
##                                                      b=input("enter available the show timings")
##                                                      if mv[2][0]==b and len(t1)>0 :
##                                                         print("you can not modify this timing , already show booked you must add this time  " ,mv[2][0])
##                                                         md.append(mv[2][0])
##                                                         a=a-1
####                                                      else:
####                                                          if len(t1)>0:
####                                                             md.append(mv[2][0])
####                                                             a=a-1
####                                                             
##                                                      
##                                                      elif mv[2][1]==b  and  len(t2)>0 :
##                                                         md.append(mv[2][1])
##                                                         a=a-1
##                                                         print("you can not modify this timing ,already show booked you must add this time  " ,mv[2][1])                                                         
##                                                      elif mv[2][2]==b and len(t3)>0 :
##                                                         print("you can not modify this timing , already show booked you must add this time  ", mv[2][2])                                                         
##                                                         md.append(mv[2][2])
##                                                         a=a-1
##                                                      elif mv[2][3]==b and len(t4)>0 :
##                                                         md.append(mv[2][3])
##                                                         a=a-1
##                                                         print("you can not modify this timing , already show booked you must add this time  ", mv[2][3])
##                                                      else:
##                                                         md.append(b)
##                                                         a=a-1
##                                                  print(md)
##                                                  mv[i+2]=md
##                                                  print("Time changed")
##                                                  print(mv)
##                                             
##                                         if  mv[3]==jm and mv[i]==jm :
##                                                  while a>0:
##                                                      b=input("enter available the show timings")
##                                                      if mv[5][0]==b and  len(t5)>0 :
##                                                         print("you can not modify this timing ,already show booked you must add this time  " ,mv[5][0])
##                                                         md2.append(mv[5][0])
##                                                         a=a-1
##                                                      elif mv[5][1]==b  and  len(t6)>0 :
##                                                         md2.append(mv[5][1])
##                                                         a=a-1
##                                                         print("you can not modify this timing , already show booked you must add this time " ,mv[5][1])                                                         
##                                                      elif mv[5][2]==b and len(t7)>0 :
##                                                         print("you can not modify this timing , already show booked you must add this time ", mv[5][2])                                                         
##                                                         md2.append(mv[5][2])
##                                                         a=a-1
##                                                      
##                                                      else:
##                                                         md2.append(b)
##                                                         a=a-1
##                                                  print(md2)
##                                                  mv[i+2]=md2
##                                                  print("Time changed")
##                                                  print(mv)
##                                         if  mv[6]==jm and mv[i]==jm:
##                                                  while a>0:
##                                                      b=input("enter available the show timings")
##                                                      if mv[8][0]==b and  len(t8)>0 :
##                                                         print("you can not modify this timing , show booked ,so  you add this time " ,mv[8][0])
##                                                         md3.append(mv[8][0])
##                                                         a=a-1
##                                                      elif mv[8][1]==b  and  len(t9)>0 :
##                                                         md3.append(mv[8][1])
##                                                         a=a-1
##                                                         print("you can not modify this timing , show book you add this time " ,mv[8][1])                                                         
##                                                      
##                                                   
##                                                      else:
##                                                         md3.append(b)
##                                                         a=a-1
##                                                  print(md3)
##                                                  mv[i+2]=md3
##                                                  print("Time changed")
##                                                  print(mv)
##                                                    
##                           
##                                   if j1==2 :
##
##                                       bm=input("enter  available the show timings")  
##                                       for i in range(0,len(mv),3) :
##                                          
##                                          if len(t1)==0 and mv[i]==jm and mv[2][0]==bm :
##                                         
##                                               print(mv[i+2])                                   
##                                               b1=input("enter the show timings")                                         
##                                               b1=mv[2][0]
##                                               print("Time changed")
##                                          if len(t2)==0 and mv[i]==jm and mv[2][1]==bm :
##                                         
##                                               print(mv[i+2])                                   
##                                               b1=input("enter the show timings")                                         
##                                               b1=mv[2][1]
##                                               print("Time changed")
##                                          if len(t3)==0 and mv[i]==jm and mv[2][2]==bm:
##                                         
##                                               print(mv[i+2])                                   
##                                               b1=input("enter the show timings")                                         
##                                               b1=mv[2][2]
##                                               print("Time changed")
##
##                                          if len(t4)==0 and mv[i]==jm and mv[2][3]==bm:
##                                         
##                                               print(mv[i+2])                                   
##                                               b1=input("enter the show timings")                                         
##                                               b1=mv[2][3]
##                                               print("Time changed")
##                                          if len(t5)==0 and mv[i]==jm and mv[5][0]==bm:
##                                         
##                                               print(mv[i+2])                                   
##                                               b1=input("enter the show timings")                                         
##                                               b1=mv[5][0]
##                                               print("Time changed")
##                                          if len(t6)==0 and mv[i]==jm and mv[5][1]==bm:
##                                         
##                                               print(mv[i+2])                                   
##                                               b1=input("enter the show timings")                                         
##                                               b1=mv[5][1]
##                                               print("Time changed")
##                                          if len(t7)==0 and mv[i]==jm and mv[5][2]==bm:
##                                         
##                                               print(mv[i+2])                                   
##                                               b1=input("enter the show timings")                                         
##                                               b1=mv[5][2]
##                                               print("Time changed")
##                                          if len(t8)==0 and mv[i]==jm and mv[8][0]==bm:
##                                         
##                                               print(mv[i+2])                                   
##                                               b1=input("enter the show timings")                                         
##                                               b1=mv[8][0]
##                                               print("Time changed")
##                                          if len(t9)==0 and mv[i]==jm and mv[8][0]==bm:
##                                         
##                                               print(mv[i+2])                                   
##                                               b1=input("enter the show timings")                                         
##                                               b1=mv[8][0]
##                                               print("Time changed")
##                                          else:
##                                                print("already ticket booked this timing you can not modify this time")
   
      
          
      








    
      
