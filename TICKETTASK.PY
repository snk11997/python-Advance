print("\t\t\t\tWELCOME TO PVR CINEMA")
print("1.Book movie tickets, 2.EXIT")
print("1.LEO,2.JOE,3.MATHIMARAN" )
print("select any one movie name ")
a=(input()).upper()
b=int(input("enter the number of ticket"))
c=int(input("number of adult"))
d=int(input("No of child"))
if a=="LEO" or a=="1":
    print("cost of  the adult ticket price :300")
    e=c*300
    print("Total price of adult tickets : " ,e)
    print("cost of the child ticket price :200")
    f=d*200
    print("Total price of child tickets : " ,f)
    print("TOTAL price of tickets: " , e+f )
    g=e*(18/100)
    print("Adult  ticket GST Amount: " ,g)
    h=f*(18/100)
    print("child ticket GST Amount: " ,h )
    i=g+h  
    print("The total GST amount: " ,i)
    j=e+f+i
    print("Total Amount" , j)
elif a=="JOE" or a=="2":
    print("cost of the adult ticket price :400")
    e=c*400
    print("Total price of adult tickets : " ,e)
    print("cost of the child ticket price : 300")
    f=d*300
    print("Total price of child tickets : " ,f)
    print("TOTAL price of tickets: " , e+f )
    g=e*(18/100)
    print("Adult  ticket GST Amount: " ,g)
    h=f*(18/100)
    print("child ticket GST Amount: " ,h )
    i=g+h
    print("The total GST amount: " ,i)
    j=e+f+i
    print("Total Amount" , j)    
elif a=="MATHIMARAN" or a=="3":
    print("cost of the adult ticket price :500")
    e=c*500
    print("Total price of adult tickets : " ,e)
    print("cost of the child ticket price :100")
    f=d*100
    print("Total price of child tickets : " ,f)
    print("TOTAL price of tickets: " , e+f )
    g=e*(18/100)
    print("Adult  ticket GST Amount: " ,g)
    h=f*(18/100)
    print("child ticket GST Amount: " ,h )
    i=g+h
    print("The total GST amount: " ,i)
    j=e+f+i
    print("Total Amount" , j)    
    
    
    

