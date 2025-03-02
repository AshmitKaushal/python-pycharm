# class method is the method that is associated with the class not to the instance of the class.
# In other words it is used to operator on class as whole rather than any specific instance of the class.
# class methods are created with @classmethods.


"""
Need to use Class method:-

When want to change the value of the class variable for all the instance of the class then we use class method
bcz in class method the first parameter is the class itself not the instance.
"""

'''
Key Features of Class Methods:
Bound to the Class: A class method works with the class as its context, not the object instance.
Access Class Variables: It can access and modify class-level variables.
Cannot Modify Instance Variables: Since it is not tied to any instance, it cannot directly modify or access instance-specific variables.
Used for Factory Methods: Class methods are often used to create factory methods that return an instance of the class.

'''

class Employee:
    company = "Apple"
    def __init__(self,name,role):
        self.name = name
        self.role = role

    @classmethod
    def changeCompany(cls,newCompanyName):
        cls.company = newCompanyName

    def display(self):
        print(f"The name of the employee is {self.name} the role is {self.role} and the company name is {self.company}")

e1 = Employee('GOGO','Developer')
e1.display()
# Changing the value of the class variable for all the instance of the class.
print()
print("-----------After changing the company name------------")
e1.changeCompany("Tesla")
e1.display()


'''
Static Method:

Static methods are not tied to the class state or instance state.
They don't take any implicit first argument like self or cls.
They are purely utility functions that happen to reside in the class's namespace.
Class Method:

Class methods are associated with the class itself and take the class (cls) as their first implicit argument.
They can access and modify the class state or properties.


'''


