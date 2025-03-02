print('-----------------------dir method-----------------------')
# dir is the method that return the list of all the attributes and method that are avaiable for the object.
# It is useful tool that help in discovering what we can do with object.
# It return the list containing all the attributes and methods available for the object.
'''
dir():
Purpose: The dir() function is used to return a list of all attributes and methods of an object 
(including its inherited methods), including those that are not directly accessible through the object's __dict__.

Output: dir() returns a list of attribute names (as strings), 
including instance variables, methods, and special attributes (e.g., __init__, __doc__, etc.).

Scope: It provides a more comprehensive list of the attributes and methods of the object, 
including inherited methods from parent classes.

Inclusion of Special Methods: It also includes special methods (such as __str__, __len__, etc.), 
which are not part of the __dict__ but can be dynamically added to objects or classes.
'''



x = [1,2,3,4]
print(x)
print(dir(x))
print(x.count(1))
# print(__dict__ not in  dir(x))
print()
print(dir())
# Here, dir() returns a list of all the names (variables and functions) in the current scope.
print()



print('-------------------__dict__ Attribute-------------------')
# __dict__ attribute return the dictionary represention of the objects attribute when called with the object
# when the dict attribue is called with class it contains all the methods all the class as a key in the dictionary dic

'''
2. __dict__:
Purpose: The __dict__ attribute is a dictionary that contains the instance variables (attributes) 
and their values for an object or class.

Output: __dict__ returns a dictionary, where the keys are the names of the attributes (as strings) and 
the values are the corresponding attribute values. It only includes the instance-level attributes of the object or class.

Scope: It only includes the attributes defined in the object or class, and
not any methods or inherited attributes from parent classes.

Inclusion of Special Methods: It does not include special methods (e.g., __str__, __len__) or '
inherited methods unless explicitly defined in the object itself.
'''


# x = [1,2,3]
# print(x.__dict__)
"""
***********************************************************
The error occurs because the __dict__ attribute is not available for all Python objects by default. Specifically, for built-in data types like lists, sets, and dictionaries, the __dict__ attribute is not present.

Why is this happening?
__dict__ is an attribute that stores an object's instance variables and their values. It is available in user-defined classes and custom objects that allow dynamic attribute assignment.
For built-in data types like lists, the internal structure is not stored in __dict__. Instead, Python's internal C implementation manages these objects differently.
For example, when you create a list in Python, it is not designed to store its elements in a dictionary like custom objects do. Therefore, trying to access x.__dict__ on a list will result in an AttributeError because lists don't have a __dict__ attribute.

*************************************************************
"""

class Student:

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def show(self):
        print(f"The name of the student is {self.name} and marks is {self.marks}")

s1 = Student("GOGO",100)
# At object level it contains all the instance variables and its value in the dictionary.
print(s1.__dict__)

# At the class level it contains all the methods of the class as the key in the dictionary.
print(Student.__dict__)
print()


print("-----------------------------------Help function----------------------------------")
# The help() function is used to get help documentation for an object,
# including a description of its attributes and methods.

'''
The help() function in Python is a built-in function that provides information about Python 
objects, modules, functions, classes, methods, and more. 
It is an interactive help system that is useful for understanding how to use different Python constructs and features.

Syntax:
python
Copy code
help(object)
object: This is the object, module, function, class, or method for which you want to retrieve documentation.

What does it do?
When called, the help() function displays documentation about the specified object. 
The documentation can include information about:

Available methods and attributes
The purpose and usage of the object
The arguments accepted by functions or methods
The return values
'''

print(":::::::::::::::Help function on print:::::::::::::::")
# It will information about the print such the parameter it takes and what it does.
help(print)
print()

import math
print(":::::::::::help function on math module::::::::::::::")
# it will print the information of all the function available in the math module.
(help(math))
print()

print("::::::::::Help function on the class:::::::::::::::::")
# This will show the documentation for MyClass, including its methods and docstrings.
class Student:
    '''This is a class student'''

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def show(self):
        print(f"The name of the student is {self.name} and marks is {self.marks}")

s1 = Student('GOGO',100)
s1.show()
help(Student)
print()

print("::::::::::Help as interactive environment:::::::::::::::::::")
'''
Interactive Help: 
If you call help() with no arguments, 
it will enter an interactive mode where you can type the name of a module, function, or object to get help.
It allows you to explore Python's documentation interactively.
python
Copy code
help()  # This enters the help system, type 'modules' to see available modules
'''
