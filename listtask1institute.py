a="Institute"
print(a.center(162,"*"))
x=[]

for i in range(100):
  print("1.Admin, 2.User 3.Exit" )
  b=int(input("select any one"))
  if b>=4:
    continue
  if b==3:
    break

  if b==1:
      c=int(input("enter the number of students"))
      for i in range(c):
          name=input("enter the nmae")
          uniq_id=int(input("enter Uniq id"))
          course=input("enter the course")
          u=int(input("amount paid"))
          v=30000-u
          location=input("enter your location")
          
          x.extend([name,uniq_id,course,v,location])

      print(x)
      print("uploaded sucessfully")
      continue
      
  if b==2:
    for i in range(100):
       print("1.name , 2.course, 3. Balance Fees, 4.Location")
       d=int(input("select any one"))
       if d==1:
         n=input("enter the students nmae") #Display all details 
         for i in range(0,len(x),5):
            if x[i]==n:
                print(x[i])
                print(x[i+1])
                print(x[i+2])
                print(x[i+3])
                print(x[i+4])
            
       elif d==2:

            for i in range(2,len(x),5):
                  e=input("Enter the course  name") #display student nmae
                  if x[i]==e:
                       print(x[i-2])
                                               
       elif d==3:
          
         f=int(input("Enter the balance amount")) # Display Student name
         
         for i in range(3,len(x),5):
            if x[i]==f:
                print(x[i-3])
                print(" your balance amount is" ,f  )
       elif d==4:
          g=input("enter the location") #Display student name
          for i in range(4,len(x),5):
            if x[i]==g:
                
                 print(x[i-4])
        
