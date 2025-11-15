# TASK 1:


a=[100,200,[300,400],500,600] 
b=int(input("write a number to find the index")) 
for i in range(len(a)): 
   if type(a[i]) == list:   
       for j in range(len(a[i])): 
           if a[i][j] == b:  
               z=f"The index of {b} is a[{i}][{j}]"  
               break 
   else: 
       if a[i] == b:   
           z=f"The index of {b} is a[{i}]]"   
           break 
print(z)



##practice TASK 2:

##a=[10,20,[10,30],40,10,[50,10,40],10,[10],100] 
##b=[]
##c=[]
##
##z=0
##y=0
##c=int(input("write a number to find the count ")) 
##for i in a: 
##    if type(i)==list: 
##        for j in i: 
##            b.append(j) 
##    else: 
##        b.append(i) 
##print(b.count(c))
##
##d=[]
##count=0
##z=0
##for i in b:
##    
##     if i==10 and count==0:
##         d.append(i)    
##         count=count+1
##          
##     if i==10 and count>=1:
##         continue     
##     if i==40 and z==0:
##        d.append(i)    
##        z=z+1
##     if i==40 and z>=1:
##        continue
##     else:
##         d.append(i)
##
##print(d)
##       
##    





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


##TASK 2:
##
##a=[10,20,[10,30],40,10,[50,10,40],10,[10],100] 
##b=[]
##c=int(input("write a number to find the count ")) 
##for i in a: 
##    if type(i)==list: 
##        for j in i: 
##            b.append(j) 
##    else: 
##        b.append(i) 
##print(b.count(c))
##
##d=[]
##
##for i in b:
##    if i not in d:
##         d.append(i)
##
##print(d)
##       
    



### TASK 4:
##list1=[1,1,2,3,4,4,5,6,6,8,8,8,9,9,0,0,0,0,0]
##list2=[]
##for i in list1:
##     if i not in list2:
##         list2.append(i)
##print(list2)
##
