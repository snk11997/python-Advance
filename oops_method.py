class A:
        def fun1(self, name, age):
                self.name = name
                self.age= age
        def fun2(self):
                print(self.name)
                print(self.age)

obj=A()

obj.fun1("naveen",25)   
obj.fun2()
obj2=A()
obj2.fun1("nave",29)
obj2.fun2()
print(obj.name)               
        