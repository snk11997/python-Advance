# a=[10,20,30,40,50,60,70]
# for i in (a):
#     print(i)



# a=[10,20,[30,40,[50],60],70]

# a=[10,20,300,[30,40,[50],60],70] 
# a[3].insert(1,400)
# print(a)




a=["arun",20,"chennai","kumar",23,"karur","santhosh",30,"chennai"]
n=input("enter your name")
for i in range(0,len(a),3):
     if a[i]==n:
         print(a[i])
         print(a[i+1])
         print(a[i+2])
         

