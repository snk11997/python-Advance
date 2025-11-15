##z=0
##a="1234567890"
##c=input("pass word")
##for i in a:
##
##    if  i in c :
##        z=z+1
##if z>0:
##    print("it contain no")
##else:
##    print("does not contain number")




a=input("enter a user name")
for  i in range(3):
   b=input("enter a password")
   if len(b)>8:
        if "1" in b or "2" in b or "3" in b or "4" in b or "5" in b or "6" in b or "7" in b or "8" in b or "9" in b or "10" in b :

            if "@" in b or "#" in b or "!"in b or "$" in b or "%"in b or "&" in b or "*" in b :
                print("registered sucessfully")
                break
            
            else:
                print("minum one special character")
        else:
            print("minimum one number")

   else:
       print("Minimum  8 character")


else:
    print("try password after sometime")
##a=input("enter usernmae")
##for i in range(2):
##    b=input("enter password")
##    if len(b)>8:
##        if "1" in b or "2" in b :
##            if "@" in b:
##                print("registerd sucess")
##                break
##            else:
##                print("minimum one character")
##                continue
##        else:
##             print("minimum one number")
##             continue
##    else:
##        print("Minimum 8 character")
##        continue
##    
## 
##else:
##    print("please try after two hours")


##TASK:

#Factorial of any number you give:

##a=int(input("enter a number"))
##x=1
##if a:
##    for i in range(1,a+1):   
##        x=x*i
##    
##    
##    print("factorial of" , a, "is" , x)
##    print("do you want to contiunue")
##
##


####NESTED FOR:
##
##for i in range(-5,5,5):
##    for j in range(-10,0,1):
##        print(i,j)
##
####for i in range (-10,10,10):
####    for j in range(1,7,3):
####        print(i,j)
####
####for i in range (5,10,2):
####    for j in range(10,20,5):
####        print(i,j)
