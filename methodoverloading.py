from multipledispatch import dispatch        # type: ignore
class A:
    def fun(self,a):
        print(a)
    def fun(self,a,b):
        print(a+b)
    def fun(self,a,b,c):
        print(a+b+c)
    def fun(self):
        print("naveen kumar ")

obj=A()
# obj.fun(1,3,3)
obj.fun()


# class A:
#     def fun(self,a=None,b=None,c=None):
#         if (a!=None and b!=None and c!=None):
#             print(a+b+c)
#         elif(a!=None and b!=None):
#             print(a+b)
#         else:
#             print(a)

# obj=A()
# obj.fun(10,20,30)
# obj.fun(10,20)
# obj.fun(10)


# class a:
#     def fun(self,*v):
#         value=0
#         for i in v:
#              value=value+i
#         print("added value:", value)

# obj=a()
# obj.fun(10,20,30)
# obj.fun(10,20)
# obj.fun(10)


# class A:
#     def fun(self,a=None ,b=None ):
#         if (a!=None and b!=None and a!=b):

#             print("rectangle area : " , a*b)
#         else:
#            print("square area" ,  a*a)

# obj=A()
# obj.fun(10,20)
# obj.fun(10)


# @dispatch(int,int)
# def add(a,b):
#     return a+b
# @dispatch(int,int,int)
# def add(a,b,c):
#     return a+b+c

# print(add(3,4))
# print(add(1,2,3))

