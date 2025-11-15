
print("demo:" , __name__)


class a:
    def  detail(self):
        print("this is class a")

class b(a):
    def  detail(self):
        print("this is class bb")

obj=a()
obj.detail()
