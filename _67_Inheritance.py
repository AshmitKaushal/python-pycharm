"""
Acquiring the properties of the one class into another is known as inheritance.
"""

'''
1. Single Level Inheritance
2. Multi Level Inheritance 
3. Mutiple Inheritance
4. Hybrid Inheritance 
5. Heiarchical Inheritance
'''

print("--------------------Single Level Inheritance------------------------")

class A:

    def show(self):
        print("Hello from class A")

class B(A):

    def display(self):
        print("Hello from class B")



a1 = A()
a1.show()

b1 = B()
b1.show()
b1.display()
print()


print("-----------------Class Employee----------------")

class Employee:

    def __init__(self,name,id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"The name of the Employee: {self.id} is {self.name}")


# Inheriting the class Employee
class Programmer(Employee):

    def showLanguage(self):
        print("The default programming language is python")


e1 = Employee('GOGO',101)
e1.showDetails()

e2 = Programmer('John',102) # Parent class constructor is called.
e2.showDetails()
e2.showLanguage()

"""
Here's what happens in your code:

You have a base class Employee with an __init__ method that takes two parameters (name and id) and 
initializes instance variables self.name and self.id.

You have a subclass Programmer that inherits from Employee 
but does not define its own __init__ method. Since Programmer does not have its own constructor, 
it inherits the constructor from Employee.

When you create an instance e2 of the Programmer class with e2 = Programmer("Bob", 102),
Python looks for an __init__ method in Programmer. 
Since Programmer does not have an __init__ method, Python goes up the inheritance chain and 
uses the __init__ method of the superclass (Employee).

The __init__ method of Employee is then called with the arguments "Bob" and 102, 
initializing e2.name as "Bob" and e2.id as 102.
"""

'''
Why Does This Work?

Even though e2 is an instance of the Programmer class, it can use the parent class's constructor because Programmer inherits all non-private members of Employee.
The attributes self.name and self.id are part of the object e2, regardless of whether they were set in the parent or child class.
'''
print()


print("--------------------When the child have its own constructor----------------")

class Employee1:

    def __init__(self,name,id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"The name of the Employee is {self.id} is {self.name}")


class Programmer1(Employee1):

    def __init__(self,name,id,langauge):
        super().__init__(name,id)
        self.language = langauge

    def showDetails(self):
        print(f"The name of the employee is {self.id} is {self.name} and the language is {self.language}")


e1 = Employee1('GOGO',101)
e1.showDetails()
e2 = Programmer1('John',102,'python')
e2.showDetails()










