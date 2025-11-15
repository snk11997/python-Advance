# store=0
# counts=0
# for i in range(100):
#    a=int(input("enter a number"))
#    store=store+a
#    counts=counts+1
   
#    if a==0:
#       break 

# print(store)
# print(counts)    



store=0
count=0
z=0
for i in range(10):
    a=int(input("enter a number"))
    store=store+a
    count=count+1
    if a==0:
        z=z+1
        if z==3:
            break

    
print(store)
print(count)
