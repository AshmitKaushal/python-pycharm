'''
Need for Multiple Constructors
Multiple constructors are required when one has to perform different actions on the instantiation of a Python class.

This is useful when the class has to perform different actions on different parameters.

How to Have Multiple Constructors in Python?
The class constructors can be made to exhibit polymorphism in three ways which are listed below.

Overloading constructors based on arguments.
Calling methods from __init__.
Using @classmethod decorator.
'''


print("---------------------Overloading Constructor based on Arugment-----------------")

class Test:

    def __init__(self,*args):

        if len(args)>1:
            self.ans = 0
            for i in args:
                self.ans+=i

        elif isinstance(args[0],int):
            self.ans = args[0]*args[0]

        elif isinstance(args[0],str):
            self.ans = "Hello," + args[0]


t1 = Test(1,2,3,4)
print("The summation of all the numbers is",t1.ans)

t2 = Test(2)
print("The square of the number is ",t2.ans)

t3 = Test("john")
print("Greeting",t3.ans)
print()

print("-----------------------Alternate of the instance method-----------------------")

class Test:

    def __init__(self,*args):

        if len(args)>1:
            self.ans = 0
            for i in args:
                self.ans = self.ans + i

        elif type(args[0])==int:
            self.ans = args[0]*args[0]


        elif type(args[0])==str:
            self.ans = "Hello,"+args[0]

t1 = Test(1,2,3,4,5)
print("The summation of all the value is",t1.ans)

t2 = Test(4)
print("The square of the number is",t2.ans)

t3 = Test("John")
print("Greeting",t3.ans)
print()

print("------------Calling method from __init__------------------")

class Test:

    def __init__(self,*args):

        if len(args)==2:
            self.ans = self.eq1(args)

        elif len(args)==3:
            self.ans = self.eq2(args)

        elif len(args)>3:
            self.ans = self.eq3(args)

    def eq1(self,args):
        return args[0]*args[0] - args[1]*args[1]

    def eq2(self,args):
        return (args[0] * args[0] - args[1]*args[1]) + args[2]

    def eq3(self,args):
        sum = 0
        max = args[0]
        for i in args:
            if max<i:
                max = i
            sum+=i
        return sum/max


t1 = Test(20,10)
print("The ans of the eq1 is",t1.ans)

t2 = Test(20,10,5)
print("The ans of the eq2 is",t2.ans)

t3 = Test(1,2,3,4,5)
print("The ans of the eq3 is",t3.ans)