# In python we dont have the static variable instead we use @staticmethod to define the static method.
# The @staticmethod decorator is used to create a static method in a class that belong the class rather than the object of the class.
# static decorator is the only to create the method which does require self as a parameter.
# If we want a method to shift with class without instance of the class then we use @staticmethod decorator.
"""

Static Method: A static method in Python is a method that belongs to the class rather than an instance of the class. It doesn't operate on instance-specific data and doesn't have access to self or cls. Static methods are defined using the @staticmethod decorator.

Syntax:

class MyClass:

@staticmethod
def my_static_method():
  # code here

Alternate way:
staticmethod(mehthod_name)
"""

"""
Need of static method:

1.Having a single implementation:-
When we don’t want subclasses of a class to change or override a specific implementation of a method, 
we use static methods. In this scenario, we declare a static method to prevent inherited classes from affecting 
our method.


2.Utility Functions: 
They are commonly used for defining utility functions that are related to the class 
but don't require access to instance variables. For example, formatting data, validating inputs, or 
performing calculations that don't depend on instance state.
"""

class Math:

    def __init__(self,num):
        self.num = num
        print(f"The value of the num is {self.num}")
    @staticmethod
    def add(a,b):
        return a+b

# Here add the static method that can be called with instance of the class and the class name.
# it is used to add the utility function to the class.

m1 =Math(10)

# Calling static method using instance of the class.
print(m1.add(10,20))

# Calling static method with the class name.
print(Math.add(10,20))
print()

print("Example of the static method formmating of date which does not any instance of the class")

class Date:

    def __init__(self,date):
        self.date = date

    @staticmethod
    def format(date):
        return date.replace('/','-')


d1 = Date('15-12-2023')
date = '15/12/2023'
newdate = Date.format(date)
if d1.date==newdate:
    print("Same Date")
else:
    print("Different Date")