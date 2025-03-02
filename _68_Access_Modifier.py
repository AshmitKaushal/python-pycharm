# Access Modifier in python programming language is used to limit the access of class variables and class method
# outside of class while implementing the concepts of inheritance.

# In python there is no public ,private and protected access modifiers.

# Instead they used a name convention to indicate the type of access to a variables and method
# but it does not restrict the access to the variables and methods.

# In Python, access modifiers are conventions or techniques used to control the visibility and accessibility of class members (attributes and methods) from outside the class.
# Unlike some other programming languages like Java or C++, Python does not have explicit keywords for access modifiers such as public, private, or protected.
# Instead, Python uses naming conventions and language features to indicate the intended visibility of class members.

print("----------------------Public Member-----------------------------")
'''
Default Modifier: All class members in Python are public by default.
Accessibility: Can be accessed and modified from anywhere (inside or outside the class).
'''

class Employee:

    def __init__(self,name,role):
        self.name = name
        self.role = role
        print(f"The name of the employee is {self.name} and its role is {self.role}")


e1 = Employee('GOGO',"Developer")
print('Accessing the name attribute of the object e1',e1.name)
print()

print("------------------------Protected Member---------------------")
'''
Convention: Denoted by a single underscore prefix (_).
Accessibility: Intended to be used only within the class and its subclasses. However, 
it is still accessible from outside the class by convention, and Python does not enforce strict protection.
'''

class Employee:

    def __init__(self,name,role):
        self.name = name
        # here role attribute is define with single underscore to indicate that it is private variable.
        # although it can be accessed outside the class.
        self._role = role

e1  = Employee("GOGO",'developer')
print("Accessing the role attribute of the object e1 which means that can be accessed only within the class and its subclass but it still can be accessed outside the class",e1._role)
print()


print('------------------------Private Member------------------------')
'''
Convention: Denoted by a double underscore prefix (__).
Name Mangling: Python performs name mangling to make private members harder to access from outside the class. 
    The member’s name is changed to _ClassName__memberName.
Accessibility: Cannot be accessed directly outside the class. 
    However, it can be accessed indirectly using the mangled name (not recommended).
'''

class Employee:

    def __init__(self,name,role):
        self.name = name
        self.__role = role


e1 = Employee('GOGO',"Developer")
# We cannot access the priavte varaible directly
# It gives error here
# print(e1.__role)

# Althought we can access indirectly _Classname__variable name
# Here a name mangling is perform which change variable to  _Classname__variable name to avoid name collision between class and subclass attribute
print("Acessing the private attribute of the object e1",e1._Employee__role)
"""

***************************************************
Here's how it works:

Name Mangling:
When you define a variable with double underscores (__) in a class, Python internally renames the variable to _ClassName__variable to make it "private."
In your case, __marks becomes _Student__marks within the Student class due to name mangling.

Need of Name Mangling:

Preventing Name Collisions:

Name mangling helps prevent accidental name collisions between attributes or methods in subclasses and their superclasses.

By modifying the names of private members to include the class name, it reduces the risk of unintended name clashes, especially in large codebases with multiple classes and inheritance hierarchies.


Accessing Private Variables:
Although direct access like s1.__marks is prevented, you can access the private variable indirectly using the mangled name _ClassName__variable.
This allows you to access the private variable outside the class but still maintains a level of encapsulation and data hiding.

****************************************************

"""
