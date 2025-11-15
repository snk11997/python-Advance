##a=(10,20,30,(10,20),10,50)
##b=[]
##for i in  a:
##    if type(i)==tuple:
##        for j in i:
##            b.append(j)
##    else:
##        b.append(i)
##
##print(b.count(10))


# c=(100,200,(300,40),500)
# d=[]
# for i in c:
#     if type(i)==tuple:
        
#         for j in i:
#             d.append(j)
#     else:
#         d.append(i)

# d[3]=400
# print(d)  
# f=tuple(d)
# print(f)

a=(100,200,(300,40),500)
b=list(a)

b[2]=(300,400)
c=tuple(b)
print(c)


        
       
    
