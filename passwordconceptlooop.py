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
##


##a=input("enter usernmae")
##for i in range(100):
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
 

##TASK:

#Factorial of any number you give:

a=input("enter a number")
x=1
if a:
    for i in range(1,a+1):   
        x=x*i
    
    
    print("factorial of" , a, "is" , x)
    print("do you want to contiunue")

    b=int(input("1.Continue 2.Exit"))
    if b==1:
          continue
    elif b==2:
          break



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
