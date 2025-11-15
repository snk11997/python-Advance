
#multi level inheritance

class one:
    def fun1(self):
        print("i am naveen")
class two(one):
    def fun2(self):
        print("i am kavin")
class three(two):
    def fun3(self):
        print("i am mani")    

obj=three()
obj.fun1()
obj.fun2()
obj.fun3()









