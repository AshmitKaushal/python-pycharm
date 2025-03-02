class Test:

    def __init__(self,a,b):
        self.a = a
        self.b = b

t1 = Test(10,20)
# Here t2 is references to the memory location of the object t1.
t2  =  t1
print(t1.a)
print(t2.a)