# class A:
#     def __init__(self,x,y):    # Default construter(self) and parameterised constructer (self, x,y)

#         self.name=x
#         self.age=y
#         print(self.name)
#         print(self.age)
    
#     def fun1(self,m,n):
#         print("Addition of 2 no is", m+n)
#         return m+n


# # obj=A("Arun",20)
# a=input("enter you name")
# b=int(input("enter the age"))
# obj2=A(a,b)
# obj2.fun1(10,20)
# print(obj2.fun1(10,20))


# # class A:
# #     def __init__(self):
# #         print("hai")

# # obj=A()

# # class A:
# #     def __init__(self,x,y):
# #         z=x+y
# #         print(z)

# # obj=A(12,1)



# # class A:
   
# #     def  __init__(self):
# #         print("naveen")
# #     def __init__(self,x,y):
# #         self.name=x
# #         self.age=y
# #         print(self.name)
# #         print(self.age)

# # # obj=A()
# # obj=A(2,5)


# class student:
#     def __init__(self,name,age) :
#         self.name=name
#         self.name="naveen "
#         self.age=age

#     def fun2(self) :
       
#         print("my name is:", self.name )
#         print("my age is:", self.age)
   
# obj=student("kavin",23)
# obj.fun2()
# print(obj.name)



# class student:
#     def __init__(self,name,age) :
#         self.name=name

#         self.age=age

#     def fun2(self) :
       
#         print("my name is:", self.name )
#         print("my age is:", self.age)
   
# obj=student("kavin",23)
# obj2=student("naveen",26)
# obj.fun2()
# obj2.fun2()
# print(obj.name)

# class student :
#     def __init__(self,name="hari",age=30):
#         self.name=name
#         self.age=age
    
#     def fun1(self):
#         print("my name is : " , self.name)
#         print("my age is : " , self.age)

# obj=student("jai",56)
# obj.fun1()



# class test:
#     z=0
#     def __init__(self,x,*y):
#         z=x
#         for i in y:
#             z=z +i
#         print("sum" ,z )

# obj=test(10,2,8,9,2)

# class test:
#     def __init__(self,name,**values):
#         print("name" ,name)
#         print("values" ,values["age"])
#         print("values" ,values["city"])
#         print("values" ,values["ph"])
       
# obj=test("john",age=43, city="chennai", ph=9786699395 )

# class A:
#     def fun1(self):
#         self.a=10



# class B:
#     def fun2(self):
#         print(obj.a)

# obj=A()
# obj2=B()
# obj.fun1()
# obj2.fun2()


## constructer does not return int , str  , bool  and anything 
# class add :
#     def __init__ (self,a,b) :
#         c=a+b
#         print(c)
#         return c

# add1=add(10,20 )





  




 