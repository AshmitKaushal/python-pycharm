"""
When the method is called with the object it will first search in which __dict__ attribute at class or object ?
ChatGPT said:
ChatGPT
When a method is called on an object, Python first searches for the method in the instance's (object's) __dict__ attribute.
If the method is not found there, it moves to the class's __dict__ attribute to locate the method. Here's a detailed explanation:

Step-by-Step Process
Instance's __dict__:

When you call a method on an object (e.g., obj.method()), Python first checks the instance's __dict__ to see
if the method is defined directly on the instance.
This is because the instance might have an attribute or method that overrides the class definition.

Class's __dict__:

If the method is not found in the instance's __dict__, Python then searches in the class's __dict__.
Methods are typically defined in the class, so this is where most methods are found.
Inheritance Chain:

If the method is not in the immediate class's __dict__,
Python continues searching up the Method Resolution Order (MRO). This includes parent classes and eventually the base object class.

Bound Methods:

If a method is found in the class's __dict__,
Python wraps it as a bound method by associating it with the instance.
This is why self is automatically passed as the first argument when you call an instance method.

"""
print("When the method is called with object first it will be search in the object __dict__ then search in the class __dict__ order to mro method resolution order which define the heiarchy for the searching")
print("Althought methods are stored at the class level they might override by the object by creating the instance with same name as the class name.")
class Test:

    def method1(self):
        print("This is method 1")
    def method2(self):
        print("This is method 2")

t1 = Test()
t1.method1()
t1.method2()
# this is empty bcz method 1 and method 2 objects are stored at class level
# bcz all the method are shared among all the object
# if it is stored at the instance level then additional memory is required by all the object to store they method
# althought they are same for the object.
print(t1.__dict__)

# method 1 and method2 is stored at the class level.
print(Test.__dict__)
print()

print("-----------------Override Example-----------")
class Test:

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def method(self):
        print("this is a method")

t1 = Test(100,200)
t1.method = "This is not a method"
print(t1.__dict__)
print(Test.__dict__)



