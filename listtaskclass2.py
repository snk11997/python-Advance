##TASK 1

a=[100,200,[300,400],500,600]
b=a.index(200)
c=a.index(600)
##d=b+c
##print(d)
##
##
##for i in a:
##    if type(i)==list:
##        g=int(input("enter the input"))
##        for j in i:
##            if j==300 and g==300:
##                print(" a[2][0] ")
##                break
##            if j==400 and g==400:
##                print(" a[2][1] ")
##                break
##    else:
##         continue

##TASK 2


##a=[10,20,[10,30],40,10,[50,10,40],10,[10],100]
##b=[]
##for i in a:
##    if type (i)==list:
##        for j in i:
##            b.append(j)
##    else:
##          b.append(i)
##
##print(b)
##d=[]
##c=b.count(10)
##print("the count of 10 in this list is " ,c)
##
##for i in  b:
##    if i==10:
##        continue
##    if i!=10:
##        d.append(i)
##
##print(d)


#TASK 3:

a=[100,200,[300,[400,500],300],600,[700,800]]
b=[]
for i in a:
   if type(i)==list:
       for j in i:
           if type(j)==list:
               for k in j:
                   b.append(k)              
           else:
                    b.append(j)
   else:
       b.append(i)
print(b)
   
## TASK 4:

##a=[100,200,[300,[400,[12,15,16],500],300],600,[700,800]]
##b=[]
##for i in a:
##   if type(i)==list:
##       for j in i:
##           if type(j)==list:
##               for k in j:
##                   b.append(k)
##                   if type(k)==list:
##                       for e in k:
##                          b.append(e)
##                  
##
##           else:
##                 b.append(j)
##   else:
##       b.append(i)
##print(b)








