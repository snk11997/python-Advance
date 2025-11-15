
b=int(input("Enter a number"))
 

if b==1 or b==0:
     print("it is not a prime number")
elif b==2 or b==3 or b==5 or b==7 or b==9 or b==13 or b==17 or b==19 or b==23 or b==29 or b==31 or b==37 or b==41 or b==43 or b==47:
     print("it is a prime number") 
elif b%2==0 or b%3==0 or b%5==0 or b%7==0 or b%11==0 or b%13==0 or b%17==0 or b%19==0 or b%23==0 or b%29==0 or b%31==0 or b%37==0 or b%41==0 or b%47==0:
     print("it it a not prime number")
else:
     print("it is a prime number")





