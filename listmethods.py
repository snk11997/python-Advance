

x=["apple","orange","banana"]
y=x.pop(1)
print(y)


a=[10,20,30]
print(a.append(40))

b=[100,200,300]
print(b.pop(2))

b=[10,20,[30,40],60]
print(b.pop(2))
print(b)




a=[10,20,30,[40,50],60]
b=a.pop(3)
print(b)
c=a.index(30)
print(c)
a.append(121)
print(a)
for i in a:
   if type(i)==list:
       for j in i:

           print(j)
   else:
       print(i)




    

  


