# When the class inherits another class then it is know as multiple inheritance

# Multiple Inheritance

# If a class inherits from more than one parent class, it is known as multiple inheritance.

# Multiple inheritance is a feature in Python where a class can inherit attributes and methods
# from more than one parent class. This allows a child class to combine and extend the functionality of multiple base classes.


# Need of MRO

# In object-oriented programming with inheritance, the MRO (method resolution order)
# determines the order in which a method is searched for in a class hierarchy.
# MRO is particularly useful in Python because it supports multiple inheritance,
# meaning that a class can inherit from multiple parent classes.


class A:

    def show(self):
        print("Hello from class A")

class B(A):

    def display(self):
        print("Hello from class B")

class C(B,A):

    def details(self):
        print("Hello from class C")

a1 = A()
a1.show()
print()

b1 = B()
b1.show()
b1.display()
print()

c1 = C()
c1.show()
c1.display()
c1.details()

# It not giving ambiguity error because it follows Mehtod Resolution Order (MRO).
# MRO indicate that if I class inherits more than one class then the class that is first in the list will be the first class to be inherited and then other classes so for the method we are searching will be the first searched in first inherited class and then other classes.

# The method we are searching will be the searched left to right.
# The MRO is as follows:
 # -----> searching left to right we can see mro using mro attribute __mro__ or mro() method.

print(C.__mro__)

# The output will be as follows:
# <class '__main__.C'>
# <class '__main__.B'>
# <class '__main__.A'>
# <class 'object'>

# The output is in the order of the class that is first inherited and then other classes.