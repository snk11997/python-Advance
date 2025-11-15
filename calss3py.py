##TASK 1:

##a=[100,200,[300,400],500,600] 
##b=int(input("write a number to find the index")) 
##for i in range(len(a)): 
##    if type(a[i]) == list:   
##        for j in range(len(a[i])): 
##            if a[i][j] == b:  
##                z=f"The index of {b} is a[{i}][{j}]"  
##                break 
##    else: 
##        if a[i] == b:   
##            z=f"The index of {b} is a[{i}]]"   
##            break 
##print(z)
##
##

##TASK 2:

a=[10,20,[10,30],40,10,[50,10,40],10,[10],100] 
b=[] 
c=int(input("write a number to find the count ")) 
for i in a: 
    if type(i)==list: 
        for j in i: 
            b.append(j) 
    else: 
        b.append(i) 
print(b.count(c)) 
for i in range(b.count(c)): 
    b.pop(b.index(c)) 
print(b)



#TASK 3:

##a=[100,200,[300,[400,500],300],600,[700,800]]
##b=[]
##for i in a:
##   if type(i)==list:
##       for j in i:
##           if type(j)==list:
##               for k in j:
##                   b.append(k)              
##           else:
##                    b.append(j)
##   else:
##       b.append(i)
##print(b)
