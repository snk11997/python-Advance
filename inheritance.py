class python:
    def fun1(self):

        print("basic class method") # parent class

class batch37(python):
    def fun2(self):
        print("derived class method1")   #child class  
    def fun3(self):
        print("derived class method2")



obj=batch37()
obj.fun2()
obj.fun1()
obj.fun3()


import unittest

class Fun1(unittest.TestCase):  # Class name should follow CamelCase by convention
    def test_myfun(self):
        pass

    def test_myfun3(self):
        print("naveen2") 

    def test_myfun4(self):
        print("naveen2")
    

class Fun2(unittest.TestCase):  # Class name should follow CamelCase by convention
    def test_myfun(self):
        pass

    def test_myfun3(self):
        print("naveen2") 

    def test_myfun4(self):
        print("naveen2")
        
if __name__ == "__main__":
    unittest.main()


