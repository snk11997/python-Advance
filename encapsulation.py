class A:
    def data(self):
        self.name="naveenkumar"
        self.a=12
        self._b=20
        self.__c=30 
        self.c=666  
    def __data2(self): 
          print(self.__c)      

class B:
     def data3(self):
          print(obj.c)
          


obj=A()
obj2=B()
obj.data()
obj2.data3()
print(obj._A__c)
obj._A__data2()









