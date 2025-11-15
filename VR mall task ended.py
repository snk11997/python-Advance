a="VR MALL"
print(a.center(120,"*"))
ps,nmt,h22=[],[],[]
mv=["siram",4,["10.00AM","12.00PM","4.00PM","7.00PM"],"leo",3,["12.00PM","5.00PM","10.00PM"],"joe",2,["4.00PM","7.00PM"]]
t1,t2,t3,t4,t5,t6,t7,t8,t9=[],[],[],[],[],[],[],[],[]
q,q1,q2,q3,q4,q5,q6,q7,q8,H2=0,0,0,0,0,0,0,0,0,0 
md,md2,md3,mt1,mt2,mt3=[],[],[],[],[],[]
for i in range(100):
   print("1.Admin 2.user")
   b=int(input("select any one"))
   if b==2:
      for i in range(100):
            print("1.sig in , 2 .log in , 3.EXIT")
            c=int(input("select any one"))
            if c==3:
                  break
            if c==1:
                d=input("enter the user name")
                f1=0
                while 1>f1:
                   e=input("enter the password")
                   if len(e)>8 :
                      if "1" in e or "2" in e or "3" in e or "4" in e or "5" in e or "6" in e or "7" in e or "8" in e or "9" in e or "0" in  e:
                          if "@" in e or "!" in e or "#" in e or "$" in e or "%" in e or "&" in e or "*" in e:
                                  print("sign in sucessfully")
                                  ps.extend([d,e])
                                  f1=f1+2                                              
                          else:
                              print("minimu one special charcter")
                      else:
                          print("minimum one number")     
                   else:
                        print("minimum 8 character")        
            if c==2:
               for a11 in range(100):
                  f=input("enter the user name")
                  g=input("enter the password")                  
                  if f in ps and g in ps:
                        print("log in sucessfully")
                        h22.append(f)
                        for a2 in range(100):                             
                           print(mv)                               
                           h1=input("select any one movie").lower()
                           for a3 in range(0,len(mv),3):                          
                               if  mv[a3]==h1 and mv[a3]==mv[0]:
                                   h22.append(h1)
                                   print("no of shows" ,mv[a3+1])
                                   print(" Shows Timings" ,mv[a3+2])                                                                                                                                       
                                   k=input("select the time")
                                   if mv[2][0]==k:                                                                                                     
                                                print("number of tickets available")
                                                h22.append(k)
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
                                                m=int(input("Enter the number of ticket :"))      
                                                while m>0:
                                                    l=int(input("select seat number :"))
                                                    if l not in t1:
                                                        t1.append(l)
                                                        m=m-1                                                        
                                                    else:                                                       
                                                        print("This seat already booked")                                                                                                
                                                print(" you ticket has been  booked sucessfully")
                                                print( " your booking is" ,t1)                                  
                                                print("Availble tickets")
                                                h22.append(t1)
                                                for i in range(1,100,10):
                                                     for j in range(i,i+10):
                                                         if j in t1 :
                                                             print("X", end=" ")
                                                         else:
                                                             print(j ,end=" ")
                                                     print()                                                
                                                print("thanks for purchasing")
                                                print("1.book again 2.LOG OUT")
                                                a1=int(input("select any one"))
                                                q=q+1                                                
                                   if mv[2][1]==k:
                                           print("number of tickets available")
                                           h22.append(k)
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
                                           m2=int(input("Enter the number of ticket :"))
                                           while m2>0:
                                                    l2=int(input("select seat number :"))
                                                    if l2 not in t2:
                                                        t2.append(l2)
                                                        m2=m2-1                                                        
                                                    else:                                                       
                                                        print("This seat already booked") 
                                           print(" you ticket has been  booked sucessfully")
                                           print( " your booking is" ,t2)                                  
                                           print("Availble tickets")
                                           h22.append(t2)
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
                                           
                                   if mv[2][2]==k :
                                            print("number of tickets available")
                                            h22.append(k)
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
                                            m2=int(input("Enter the number of ticket :"))
                                            while m2>0:
                                                    l2=int(input("select seat number :"))
                                                    if l2 not in t3:
                                                        t3.append(l2)
                                                        m2=m2-1                                                        
                                                    else:                                                       
                                                        print("This seat already booked") 
                                            print(" you ticket has been  booked sucessfully")
                                            print( " your booking is" ,t3)                                  
                                            print("Availble tickets")
                                            h22.append(t3)
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
                                   if mv[2][3]==k:
                                              print("number of tickets available")
                                              h22.append(k)
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
                                              m2=int(input("Enter the number of ticket :"))
                                              while m2>0:
                                                    l2=int(input("select seat number :"))
                                                    if l2 not in t4:
                                                        t4.append(l2)
                                                        m2=m2-1                                                        
                                                    else:                                                       
                                                        print("This seat already booked")
                                              h22.append(t4)
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
                                              q3=q3+1
                                              print("1.book again 2.LOG OUT")
                                              a1=int(input("select any one"))                                                                                                                         
                               elif mv[a3]==h1 and mv[a3]==mv[3]:
                                  h22.append(h1)
                                  print("no of shows" ,mv[a3+1])
                                  print("Timings" ,mv[a3+2]) 
                                  k=input("select the time")
                                  if mv[5][0]==k:                                     
                                        print("number of tickets available")
                                        h22.append(k)
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
                                        m2=int(input("Enter the number of ticket :"))
                                        while m2>0:
                                                    l2=int(input("select seat number :"))
                                                    if l2 not in t5:
                                                        t5.append(l2)
                                                        m2=m2-1                                                        
                                                    else:                                                       
                                                        print("This seat already booked") 
                                        print( " your booking is" ,t5)                                  
                                        print("Availble tickets")
                                        h22.append(t5)
                                        for i in range(1,100,10):
                                                    for j in range(i,i+10):
                                                       if j in t5 :
                                                           print("X", end=" ")

                                                       else:
                                                          print(j ,end=" ")
                                                    print()
                                        print("thanks for purchasing")
                                        print("1.book again , 2.LOG OUT")
                                        a1=int(input("select any one"))
                                        q4=q4+1
                                                                                                                
                                  if mv[5][1]==k:
                                        print("number of tickets available")
                                        h22.append(k)
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

                                            
                                        m2=int(input("Enter the number of ticket :"))
                                        while m2>0:
                                                    l2=int(input("select seat number :"))
                                                    if l2 not in t6:
                                                        t6.append(l2)
                                                        m2=m2-1                                                        
                                                    else:                                                       
                                                        print("This seat already booked") 
                                        print(" you ticket has been  booked sucessfully")
                                        print( " your booking is" ,t6)                                  
                                        print("Availble tickets")
                                        h22.append(t6)
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
                                       
                                  if mv[5][2]==k:
                                        print("number of tickets available")
                                        h22.append(k)
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
                                            
                                        m2=int(input("Enter the number of ticket :"))
                                        while m2>0:
                                                    l2=int(input("select seat number :"))
                                                    if l2 not in t7:
                                                        t7.append(l2)
                                                        m2=m2-1                                                        
                                                    else:                                                       
                                                        print("This seat already booked") 
                                        print(" you ticket has been  booked sucessfully")
                                        print( " your booking is" ,t7)                                  
                                        print("Availble tickets")
                                        h22.append(t7)
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
                                        
        
                               elif mv[a3]==h1 and mv[a3]==mv[6]:
                                 
                                 h22.append(h1)
                                 print("no of shows" ,mv[a3+1])
                                 print("Timings" ,mv[a3+2]) 
                                 k=input("select the time")
                                 if mv[8][0]==k:
                                       
                              
                                        print("number of tickets available")
                                        h22.append(k)
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
                                        m2=int(input("Enter the number of ticket :"))
                                        while m2>0:
                                                    l2=int(input("select seat number :"))
                                                    if l2 not in t8:
                                                        t8.append(l2)
                                                        m2=m2-1                                                        
                                                    else:                                                       
                                                        print("This seat already booked")
                                        h22.append(t8)                
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
                                 if mv[8][1]==k:   
                                        print("number of tickets available")
                                        h22.append(k)
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
                                        m2=int(input("Enter the number of ticket :"))
                                        while m2>0:
                                                    l2=int(input("select seat number :"))
                                                    if l2 not in t9:
                                                        t9.append(l2)
                                                        m2=m2-1                                                        
                                                    else:                                                       
                                                        print("This seat already booked") 
                                        print(" you ticket has been  booked sucessfully")
                                        print( " your booking is" ,t9)                                  
                                        print("Availble tickets")
                                        h22.append(t9)
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
                           else:
                                 if a1==1:
                                       continue
                                 if a1==2:
                                    H2=H2+1   
                                    break        
                        if H2==1:
                     
                            break
   if b==1:      
      for i in range(100):
         print("1.New movie 2.Modify 3.My booking 4.Exit")
         n1=int(input("select any one"))       
         print(mv)
         if n1==3:
            print("1.Movie 2.Total Tickets sold 3.History ")
            g2=int(input("select any one"))
            if g12==1:
               print(mv)
               g3=inpur(enter the any one name")
               for y in range(0,len(mv,3):
                 if mv[0]=g3:
                        g4=len(t1)+len(t2)+len(t3)+len(t4)
                        print("Total tickets" , g4)
                 if mv[3]=g3:
                        g5=len(t5)+len(t6)+len(t7)
                        print("Total tickets" , g5)
                 if mv[6]=g3:
                        g6=len(t8)+len(t9)
                        print("Total tickets" , g6)
                 else:
                    print("correct  movie nmae")
               
            if g13==2:
               g7=len(t1)+len(t2)+len(t3)+len(t4)+len(t5)+len(t6)+len(t7)+len(t8)+len(t9)
               print("Total Tickets sold", g7)

            if g14==3:
               print(h22)               
               
         if n1==1:
           n2=input("enter the movie name").lower()
           n3=int(input("enter the Show"))
           n4=input("eneter the show timings")
           mv.extend([n2,n3])
           nmt.append(n4)
           mv.append(nmt)
           print(mv) 
         elif n1==2:
               for i in range(20):
                           print(mv)
                           print("select any one movie")
                           jm=input("enter the  MOVIE name").lower()
                           for i in range(0,len(mv),3):
                              if mv[i]==jm:                                    
                                   print("1. shows &Timing modify ,  2.Timings modify")
                                   print("select any one ")
                                   j2=int(input("selct any one"))                           
                                   if j2==1:
                                         if mv[i]==jm and mv[0]==mv[i]:
                                                  v3=mv[i+1]
                                                  print("running shows",v3)
                                                  ddd=[t1,t2,t3,t4]
                                                  n2=0
                                                  n3=0
                                                  for i8 in ddd:
                                                     
                                                     if len(i8)>0:
                                                        for j in range(1):                                                   
                                                          md.append(mv[2][n3])
                                                          n2=n2+1
                                                     n3=n3+1 
                                       
                                                  print("already booked shows" ,n2 ,md )                                            
                                                  a=int(input("enter your needed the number of shows"))
                                                  a5=a-n2
                                                  if a>n2:
                                                     a6=n2+a5
                                                     mv[i+1]=a6
                                                  else:
                                                     print("you can not changes at  all shows are booked")
                                                     mv[i+1]=n2
                                                  while a5>0:
                                                     b=input("enter available the show timings")
                                                     if b not in md:                                                
                                                          md.append(b)
                                                          a5=a5-1
                                                     else:                                                       
                                                          print("This show time already booked")
                                                  print(md)
                                                  mv[i+2]=md
                                                  print("Time changed")
                                                  print(mv)                                                 
                                         if mv[i]==jm and mv[3]==mv[i]:
                                                  v3=mv[i+1]
                                                  print("running shows",v3)
                                                  ddd=[t5,t6,t7]
                                                  n2=0
                                                  n3=0
                                                  for i8 in ddd:
                                                     
                                                     if len(i8)>0:
                                                        for j in range(1):                                                   
                                                          md2.append(mv[2][n3])
                                                          n2=n2+1
                                                     n3=n3+1                                                                                          
                                                  print("already booked shows" ,n2 ,md2 )                                            
                                                  a=int(input("enter your needed the number of shows"))
                                                  a5=a-n2
                                                  if a>n2:
                                                      a6=n2+a5
                                                      mv[i+1]=a6
                                                  else:
                                                     print("you can not changes at  all shows are booked")
                                                     mv[i+1]=n2
                                                  while a5>0:
                                                     b=input("enter available the show timings")
                                                     if b not in md2:                                                
                                                          md2.append(b)
                                                          a5=a5-1
                                                     else:                                                       
                                                          print("This show time already booked")
                                                  print(md2)
                                                  mv[i+2]=md2
                                                  print("Time changed")
                                                  print(mv)
                                         if mv[i]==jm and mv[6]==mv[i]:
                                                  v3=mv[i+1]
                                                  print("running shows",v3)
                                                  ddd=[t8,t9]
                                                  n2=0
                                                  n3=0
                                                  for i8 in ddd:
                                                     
                                                     if len(i8)>0:
                                                        for j in range(1):                                                   
                                                          md3.append(mv[2][n3])
                                                          n2=n2+1
                                                     n3=n3+1                                                                                          
                                                  print("already booked shows" ,n2 ,md3)                                            
                                                  a=int(input("enter your needed the number of shows"))
                                                  a5=a-n2
                                                  if a>n2:
                                                      a6=n2+a5
                                                      mv[i+1]=a6
                                                  else:

                                                     print("you can not changes at  all shows are booked")
                                                     mv[i+1]=n2
                                                
                                                  while a5>0:
                                                     b=input("enter available the show timings")
                                                     if b not in md3:                                                
                                                          md3.append(b)
                                                          a5=a5-1
                                                     else:                                                       
                                                          print("This show time already booked")
                                                  print(md3)
                                                  mv[i+2]=md3
                                                  print("Time changed")
                                                  print(mv)
                                   if j2==2:
                                     if mv[i]==jm and mv[0]==mv[i]:
                                                  v3=mv[i+1]
                                                  print("running shows",v3)
                                                  ddd=[t1,t2,t3,t4]
                                                  n2=0
                                                  n3=0
                                                  for i8 in ddd:                                                     
                                                     if len(i8)>0:
                                                        for j in range(1):                                                   
                                                          mt1.append(mv[2][n3])
                                                          n2=n2+1
                                                     n3=n3+1                                                                                        
                                                  print("already booked shows" ,n2 ,mt1)                                            
                                                  a5=v3-n2                                                  
                                                  while a5>0:
                                                     b=input("enter show timings")
                                                     if b not in mt1:                                                
                                                          mt1.append(b)
                                                          a5=a5-1
                                                     else:                                                       
                                                          print("This show time already booked")
                                                  print(mt1)
                                                  mv[i+2]=mt1
                                                  print("Time changed")
                                                  print(mv)
                                     if mv[i]==jm and mv[3]==mv[i]:
                                                  v3=mv[i+1]
                                                  print("running shows",v3)
                                                  ddd=[t5,t6,t7]
                                                  n2=0
                                                  n3=0
                                                  for i8 in ddd:                                                     
                                                     if len(i8)>0:
                                                        for j in range(1):                                                   
                                                          mt2.append(mv[2][n3])
                                                          n2=n2+1
                                                     n3=n3+1                                                                                        
                                                  print("already booked shows" ,n2 ,mt2)                                            
                                                  a5=v3-n2                                                  
                                                  while a5>0:
                                                     b=input("enter available the show timings")
                                                     if b not in mt2:                                                
                                                          mt2.append(b)
                                                          a5=a5-1
                                                     else:                                                       
                                                          print("This show time already booked")
                                                  print(mt2)
                                                  mv[i+2]=mt2
                                                  print("Time changed")
                                                  print(mv)
                                     if mv[i]==jm and mv[6]==mv[i]:
                                                  v3=mv[i+1]
                                                  print("running shows",v3)
                                                  ddd=[t8,t9]
                                                  n2=0
                                                  n3=0
                                                  for i8 in ddd:                                                     
                                                     if len(i8)>0:
                                                        for j in range(1):                                                   
                                                          mt1.append(mv[2][n3])
                                                          n2=n2+1
                                                     n3=n3+1                                                                                        
                                                  print("already booked shows" ,n2,mt3)                                            
                                                  a5=v3-n2                                                  
                                                  while a5>0:
                                                     b=input("enter available the show timings")
                                                     if b not in mt3:                                                
                                                          mt3.append(b)
                                                          a5=a5-1
                                                     else:                                                       
                                                          print("This show time already booked")
                                                  print(mt3)
                                                  mv[i+2]=mt3
                                                  print("Time changed")
                                                  print(mv)
      
                                                            
                           else:
                               break                     
                              
         elif n1==3:
            break
           
    
        
          
