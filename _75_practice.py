class Employee:

    def __init__(self,name,role):
        self.name = name
        self.role = role

    def show(self,data):
        print("This is the show method")

e1 = Employee('GOGO','Developer')
e1.show(10)
Employee.show(e1,10)

'''
How Methods Are Called with an Object
Here’s what happens step-by-step when you call e1.show():

Instance Attribute Lookup:

Python first checks if e1 has an attribute show in its __dict__. It doesn't because methods are stored in the class, not the instance.
Class Attribute Lookup:

Python looks in the Employee class for a method named show.
Method Binding:

When it finds show in the class, Python automatically binds it to the instance (e1). This is done by passing the instance (e1) as the first argument to the method.
Internally, e1.show() is equivalent to:

python
Copy code
Employee.show(e1)
'''

class Student:
    sch_name = "XYZ"

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    @classmethod
    def class_method(cls):
        print("This is the class method")

    def show(self):
        print(f"The name of the student is {self.name} and the marks is {self.marks}")

s1 = Student('GOGO',100)
s1.show()
Student.class_method()
# pass class as the first parameter
Student.class_method.__func__(Student)

'''
In Python, when you define a method (including a @classmethod), 
it gets wrapped in a descriptor object that handles how the method behaves 
when accessed via a class or an instance. 
The __func__ attribute of a method allows you to retrieve the raw function object 
(the unbound version of the method). Here's how this relates to calling a class method and 
why using __func__ differs from a normal method call.

Normal Behavior of a Class Method
When you call a class method using:

python
Copy code
Student.class_method()
Python automatically recognizes class_method as a class method (due to the @classmethod decorator).
The Student class is automatically passed as the first argument to the method (cls).
This automatic behavior happens because the @classmethod decorator modifies the method's behavior to use the class (instead of an instance) as the first parameter.

Accessing the Raw Function Using __func__
When you access Student.class_method.__func__, 
you bypass the descriptor mechanism and retrieve the raw function object behind the class method. 
This raw function does not have the automatic behavior of passing the class (Student) as the first argument.

For example:

python
Copy code
Student.class_method.__func__(Student)
'''