# "Dunder" methods in Python are special methods that are surrounded by double underscores,
# hence the term "dunder" (short for "double underscore"). These methods have specific names and
# are used for various built-in operations and functionality in Python classes.
# Dunder methods are also known as magic methods or special methods.

'''
In Python, dunder methods (short for "double underscore" methods) refer to special methods that are prefixed and suffixed with double underscores (__).
These methods are used to define the behavior of objects in certain operations, such as arithmetic operations, comparison, or object representation.
They are often referred to as "magic methods" or "special methods"
because they provide hooks to customize and control how objects interact with Python's built-in functionality.
'''

print('-----------------------Common Dunder Methods------------------')
print('----------------------__init__ methods------------------')
# Used to initialize the instance variables of the class.
class Student:

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        print(f"The constructor of the class Student")

s1 = Student('GOGO',100)
print()

print("------------------------__len__ Method-----------------------")
# It used to calculate the length of the object attribute like name.

class Student1:

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        print(f"The constructor of the class Student")

    def __len__(self):
        i = 0
        for c in self.name:
            i = i + 1
        return i

# On calling len() the __len__ method define in the class is called.
s1 = Student1('GOGO',100)
print("The length of the attribute is",len(s1))
print()


print('--------------------__str__ Method----------------------')
class Employee:

    def __init__(self):
        print("Constructor")

    def __str__(self):
        return "The string representation of the object"

# On printing object e1 __str__ method define in the class is called,
# which is responsible for the string representation of the object.
e1 = Employee()
print(e1)
# We call str() with object __str__ method automatically called.
print(str(e1))
print()

print("--------------------__repr__ method--------------------")
# It is also used for the string representation of the object.
# It used to recreate the object.

class Employee:

    def __init__(self):
        print("Constructor")

    def __repr__(self):
        return "The string representation of the object repr"

e1 = Employee()
print(e1)
print()


print("---------------------__call__ method----------------------")
class Employee:

    def __init__(self):
        print("The constructor of the class")

    def __call__(self):
        print("Used to make object callable")

e1 = Employee()
# On __call__ method is used to make object callable.
# means that it can be act as function
e1()