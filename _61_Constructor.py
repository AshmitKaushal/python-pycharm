# Constructor is a special method in a class used to create the object of the class and intialize the instance variable of the class.

# Constructor is invoked automatically when an object of a class is created.

# Constructor is a unique function that gets called automatically when an object is created of a class.

# The main purpose of a constructor is to initialize or assign values to the data members of that class. It cannot return anything.

# In python construtor is defined using the __init__() function.

# In which the first parameter is always self.
# The self parameter is a reference to the current instance of the class and is used to access the variables that belongs to the class.

# In Python, a constructor is a special type of method that is automatically called when a new instance of a class is created. It's used to initialize the object's attributes or perform any setup tasks needed for the object to be in a valid state. In Python, the constructor method is named __init__.

# Here are some key points about constructors in Python:

# Name: The constructor method is named __init__. It's a dunder method (double underscore on each side), indicating its special nature.

# Purpose: The main purpose of a constructor is to initialize the attributes of an object when it is created. This includes setting initial values for instance variables.

# Automatic Invocation: The constructor is automatically called when you create a new instance of a class using the class name followed by parentheses, like obj = ClassName().

# Parameters: The constructor can take parameters just like any other method. Typically, the first parameter is self, which refers to the instance being created, followed by other parameters as needed to initialize the object.

# Instance Initialization: Inside the constructor, you use self to access and initialize instance variables (attributes) of the object. For example, self.attribute_name = initial_value.


"""
Constructors in Python is a special class method for creating and initializing an object instance at that class. In Python every class has a constructor; it's not required to define explicitly. The purpose of the constructor is to construct an object and assign a value to the object's members.


# There two types of constructor in python:

# Parameterized Constructor
  The Constructor which receives the arugements as parameters with self is know as parameterized constructor.

# Default Constructor
   The Constructor which doesn't receives the arugements as parameters excpet self is know as default constructor.
"""

class Employee:

    def __init__(self,name,role):
        self.name = name
        self.role  = role

    def show(self):
        print(f"The name of the employee is {self.name} and his role is {self.role}")


e1 = Employee("John","Developer")
e1.show()