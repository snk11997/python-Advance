class A:
    def fun2(self):
        print("naveen kuamr")
class B(A):
    
    def fun2(self):
        super().fun2()
        print("kavin kumar")

obj=B()
obj.fun2()

# class A:
#     def __init__(self):
#         print("base class constructor")
# class B(A):
#     def __init__(self):
#         super().__init__()
#         print("derived class constructor")
#     def fun(self):
#         super().__init__()
#         print("derived class method")

# obj=B()
# ob.fun()

