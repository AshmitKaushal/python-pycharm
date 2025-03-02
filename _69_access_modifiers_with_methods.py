print("---------------Public Methods-------------")
"""
1. Public Methods
These are the default in Python.
Accessible from anywhere: inside the class, subclasses, or any other part of the program.
No special naming convention is required.
"""
class Test:

    def __init__(self):
        print("THis is a constructor")

    def show(self):
        print("This is a public method show")

t1 = Test()
# Every method in python is bydefault public so we simply call with the object.
t1.show()
print()


print("-----------------Protected Method---------------")
'''
Convention: Prefix the method name with a single underscore (_).
Indicates that the method is intended for use within the class and its subclasses.
Not enforced: It can still be accessed from outside the class.
'''

class Employee:

    def __init__(self,name,role):
        self.name = name
        self.role = role

    def _details(self):
        print(self.name,self.role)
        print("This is a protected method intended to use within the class and subclass but still can be accessed outside also.")


e1 = Employee('GOGO','Developer')
e1._details()
print()

print("------------------Private Method---------------------")
'''
Convention: Prefix the method name with a double underscore (__).
Name mangling: The method name is internally changed to _ClassName__methodName to make it harder to access directly.
Partially enforced: Private methods are not directly accessible, but can still be accessed using their mangled names.
'''

class Student:

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def __show(self):
        print(f"The name of the student is {self.name} and marks is {self.marks}")

s1 = Student('GOGO',100)
# Directly inaccessible here it gives error
# print(s1.__show())

# Can be accessed as _className__method name
# Here it is name mangled to avoid name collision between class and subclass method
(s1._Student__show())