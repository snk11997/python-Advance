class detail :
    def fun1(self,name,no):
        self.name=name
        self.no=no
        print(self.name)
        print(self.no)
    def fun2(self,name,no):
        self.name=name
        self.no=no
        print(self.name)
        print(self.no)

obj=detail()

obj.fun1("naveen",25) 
obj2=detail()

obj2.fun2("naveen",25) 


class detail:
    school_name = "ABC SCHOOL"
    def __init__(self , name, no) :
        self.name = name
        self.no = no
        print(detail.school_name)
        print(self.school_name)

s1= detail( "shiva" , 10)
print(s1.name , s1.no , s1.school_name)
print(s1.name , s1.no , detail.school_name)