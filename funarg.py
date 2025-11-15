def fun1(x,y,z):
    print(x+y)

fun1(10,20,30)
fun1(100,-100,100)

def fun2(*a):
    print(a[0])
    print(a[1])
    print(a)
fun2(100,200)