# class A :
#     def fun1(self):
#         self.a=int(input("enter 1st number"))
#         self.b=int(input("enter 2nd number"))
#     def __add__(hello1,hello2):
#         print(hello1.a+hello2.a+hello1.b+hello2.b)
#         # print(hello1.b+hello2.b)
# obj1=A()
# obj2=A()
# obj1.fun1()
# obj2.fun1()
# #3
# obj1+obj2


#error
# class A :
#     def __init__(self):
#         self.a=int(input("enter 1st number"))
        
#     def __add__(hello1,hello2):
#         print(hello1.a+hello2.a+hello3.a)
#         # print(hello1.b+hello2.b)
# obj1=A(2)
# obj2=A(4)
# obj3=A(1)

# a=obj1+obj2+obj3


# class A:
#     def __init__(self, num):
#         self.a = num

#     def __add__(self, other):
#         if isinstance(other, A):
#             return A(self.a + other.a)
#         else:
#             raise TypeError("Unsupported operand type(s) for +: 'A' and '{}'".format(type(other)))

# obj1 = A(2)
# obj2 = A(4)
# obj3 = A(1)

# result = obj1 + obj2 + obj3
# print("Sum of attributes:", result.a)



# class A :
#     def fun1(self):
#         self.a=int(input("enter 1st number"))
#         self.b=int(input("enter 2nd number"))
#     def __add__(hello1,hello2,hello3):
#         print(hello1.a+hello2.a+hello1.b+hello2.b +hello3.a+hello3.b)
      

# obj1=A()
# obj2=A()
# obj3=A()
# obj1.fun1()
# obj2.fun1()
# obj2.fun1()

# obj1+obj2+obj3


class A:
    def fun1(self):
        self.a = int(input("Enter 1st number: "))
        self.b = int(input("Enter 2nd number: "))
    
    def __add__(self, other1, other2):
        if isinstance(other1, A) and isinstance(other2, A):
            return self.a + other1.a + other2.a + self.b + other1.b + other2.b
        else:
            raise TypeError("Unsupported operand type(s) for +: '{}' and '{}' and '{}'".format(type(self), type(other1), type(other2)))


obj1 = A()
obj2 = A()
obj3 = A()


obj1.fun1()
obj2.fun1()
obj3.fun1()

result = obj1 + obj2 + obj3
print("Result of addition:", result)
