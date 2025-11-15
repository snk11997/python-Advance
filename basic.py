a=1 
b=18
c=1
if (a>=b) and (a>=c) :
    large = a
elif (b>=a) and (b>=c) :
    large = b
else:
    large = c

print("the largest number among:" , a ,b,c, " is: " , large)
