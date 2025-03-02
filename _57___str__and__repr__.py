class Test:
    a = 10

t1 = Test()
# Whenever we print the object of the class it will print the class name and the memory address of the object.
print(t1)

# Whenever we print the object internally two methods are called.
print(t1.__str__())
print(t1.__repr__())

# # The __str__() method is defined to return a human-readable string representation of the instance,
# while the __repr__() method is defined to return a string representation of the instance that can be used to recreate the object.

# We can change the representation of the object instead of class name and memory address to our choice using __str__() method or __repr__() method.
# When you print an object of a class in Python, the output you see depends on how the __str__() or __repr__() method is implemented in that class.
# These are special methods in Python that control how an object is represented as a string when it is printed or converted to a string.


# Both method does not print something but it returns something that is a string.
# when an object is printed in Python using the print() function or when it is converted to a string explicitly using str(), the __str__() method is called internally if it's defined in the class.
# If __str__() is not defined, Python falls back to calling the __repr__() method. Here's how it works:

class Test1:

    a = 10
    def __str__(self):
        return f"this is __str__ method of the class Test"

t1 = Test1()
# Now on printing the t1 object of the class Test it does not print the class name and memory address of the object
# bcz we have override the __str__ method which is responsible for the string representation of the object.
print(t1)



# When we use str() method on the object of the class, it calls the __str__() method internally.
print("Printing using str() method", str(t1))


'''
Sure! Let's go through this code step by step to understand its functionality and what it demonstrates.

#Code Explanation
Class Definition
python
Copy code
class Color:
    def __init__(self, suffix):
        self.suffix = suffix
        self.title = f"Golden {suffix}"

    def __repr__(self):
        return f"Color('{self.suffix}')"
__init__ Method: This is the constructor method that initializes the instance of the Color class. It takes suffix as a parameter and sets two instance variables:

self.suffix is set to the provided suffix.
self.title is constructed as a string combining "Golden " with the provided suffix.
__repr__ Method: This method returns a string that represents the object in a way that can be used to recreate the object. In this case, it returns a string of the form Color('suffix').

Creating an Instance

python
Copy code
c1 = Color("Yellow")
An instance c1 of the Color class is created with the suffix "Yellow".
The __init__ method sets c1.suffix to "Yellow" and c1.title to "Golden Yellow".
Creating Another Object Using eval() on repr()

python
Copy code
c2 = eval(repr(c1))
repr(c1) calls the __repr__ method on c1, which returns the string Color('Yellow').
eval(repr(c1)) evaluates this string as a Python expression, effectively executing Color('Yellow') to create a new Color object.
This new object is assigned to c2.
Printing the Titles

python
Copy code
print("c1.title:", c1.title)
print("c2.title:", c2.title)

c1.title is "Golden Yellow", as set during the creation of c1.

c2.title is also "Golden Yellow", because c2 is created with the same parameters as c1 using eval() on repr(c1).

Summary
The Color class initializes objects with a suffix and a title derived from the suffix.

The __repr__ method provides a string representation that can recreate the object 
using eval().

By using eval(repr(c1)), we create a new object c2 with the same attributes as c1.
The titles of both c1 and c2 are printed, showing they have the same title.

Output
python
Copy code
c1.title: Golden Yellow
c2.title: Golden Yellow

This demonstrates that c2 is a new object with the same properties as c1, created dynamically using the eval() function on the string representation provided by the __repr__ method.

'''
