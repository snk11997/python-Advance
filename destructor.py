# deallocate the memory 
# it called when object destroyed

class test : 
    def __init__(self) : 
        print("object created")
    def __del__ (self) :
        print("object deleted")
    
w=test()
del w


