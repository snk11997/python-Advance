class dog:    # single ,  hierarical,mutiple -hybird inhetitance  
    def fun1(self):
        print("hello i am dog")
class cat(dog):
    def fun2(self):
        print("hello i am cat")

class elephant(cat):
    def fun3(self):
        print("hello i am elephant")
    
class horse(cat,elephant):
    def fun4(self):
        print("hello i am horse")
        
obj=horse()
obj.fun1()
obj.fun2()
obj.fun3()
obj.fun4()


# single,multi level ,multiple

class dog:
    def fun1(self):
        print("hello i am dog")
class cat(dog):
    def fun2(self):
        print("hello i am cat")

class elephant(cat):
    def fun3(self):
        print("hello i am elephant")
    
class horse(dog,elephant):
    def fun4(self):
        print("hello i am horse")


# Hierarchical Inheritance
# Multiple child classes inherit from a single parent class.

class Parent:
    def __init__(self):
        self.value = "I'm a parent"

    def show(self):
        print(self.value)

class Child1(Parent):
    def display(self):
        print("I'm child 1")

class Child2(Parent):
    def display(self):
        print("I'm child 2")

child1 = Child1()
child2 = Child2()
child1.show()    # I'm a parent
child1.display() # I'm child 1
child2.show()    # I'm a parent
child2.display() # I'm child 2
