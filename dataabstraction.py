from abc import ABC,abstractmethod
class A(ABC):
    def fun(self):
        print("abstract class public method")
    @abstractmethod
    def hello(self):
        print("abstract method")
class B(A):
    def hello(self):
        print("derived class")
        super().hello()
 
obj=B()
obj.fun()
obj.hello()

# few  functions will not show the user so we can use the data abstraction 

# class a(ABC):
#     @abstractmethod
#     def method1(self):
#         pass
# class b(a) :
#     def method1(self):
#         print(" i am from class b ")
# obj=b()
# obj.method1()  

# class a(ABC):
#     @abstractmethod
#     def method1(self):
#         print("i am in chennai ")
# class b(a) :
#     def method1(self):
#         print(" i am from class b ")
#         super().method1()
# obj=b()
# obj.method1()


# class a(ABC) :
#     @abstractmethod
#     def method1(self) :
#         print("i am method 1")
#     @abstractmethod
#     def method2(self) :
#         print("i am method 1")
# class b(a ):

#     def method1(self) :
#         print("i am method 1")
#     def method2(self) :
#         print("i am method 4")
# class c(a):
#     def method2(self) : 
#         print("i am method 2 ")

# obj=b() 
# obj.method1() 


