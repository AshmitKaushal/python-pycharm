class Test:
    # Here a and b are the class variables and they are accessed using class name and object name.
    a = 100
    b = 200

    def __init__(self,c,d,e):
        # this are instance variables which makes separate copy for every object.
        self.c = c
        self.d = d
        self.e = e

t1 = Test(10,20,30)
t2 = Test(100,200,300)
print(t1.a)
print(t2.c)
print(t2.d)
print(t2.e)
print(t1.c)
print(t1.d)
print(t1.e)
