##a=[]
##b=10
##print(a)
##if None in a :
##    print("snk")
t1=[]
count=0
q=0
##for i in range(100):
##   m=int(input("enter the number of ticket"))
##   for a5 in range(m):
##     l=int(input("select seat number"))
##     if l not in t1:
##           t1.append(l)
##           count=count+1
##     else:
##        q=q+1
##        for i range(q)
##        print("already booked this sheat")
        
m=int(input("Enter the number of ticket :"))      
while m>0:
    l=int(input("select seat number :"))
    if l not in t1:
        t1.append(l)
        m=m-1
        print("Remaining Tickets :",m)
    else:
        print("Remaining TIckets :",m)
        print("This seat already booked")


print(t1)
print(m)
##                                                for a5 in range(m):
##                                                         l=int(input("select seat number"))
##                                                         if l not in t1:
##                                                               t1.append(l)
##                                                               count=count+1
##                                                               if count==m:
##                                                                     break
##                                                         else:  
##                                                            print("already booked this sheat")
##                                                            for r in range(count-m):
##                                                                  l=int(input("select seat number"))
##                                                                  t1.append(l)  

##else:
##     if m==count:
##              break  

##nmt=[]
##mv=["siram",4,["10.00AM","12.00PM","4.00PM","7.00PM"],"leo",3,["12.00PM ","5.00PM","10.00PM"],"joe",2,["4.00PM","7.00PM"]]
##for i in range(100):
##        print("1.New movie 2.Modify 3.Exit")
##        n1=int(input("select any one"))       
##        print(mv)
##        if n1==1:
##           n2=input("enter the movie name")
##           n3=input("enter the Show")
##           n4=input("eneter the show timings")
##           mv.extend([n2,n3])
##           nmt.append(n4)
##           mv.append(nmt)
##           print(mv) 
##        elif n1==2:
##               for i in range(100):                           
##                           print("select any one movie")
##                           jm=input("enter the your modify MOVIE name")
##                           for i in range(0,len(mv),3):
##                              if mv[i]==jm:                                    
##                                   print("1. shows ,  2.Timings")
##                                   print("select any one ")
##                                   j1=int(input("type numbr"))
##                           
##                                   if j1==1:
##                                         print("runnin shows",mv[i+1])
##                                         a=int(input("enter your needed the number of shows"))
##                                         mv[i+1]=a
##                                         print(mv[i+2])
##                                         b=input("enter available the show timings")                                         
##                                         mv[i+2]=[b]
##                                         print("Time changed")
##                                   print(mv)
##                           else:
##                               break
