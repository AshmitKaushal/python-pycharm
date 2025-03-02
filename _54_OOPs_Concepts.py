'''Introduction to Object-Oriented Programming in Python: In programming languages,
mainly there are two approaches that are used to write program or code.

1). Procedural Programming
2). Object-Oriented Programming
The procedure we are following till now is the “Procedural Programming” approach.
So, in this session, we will learn about Object Oriented Programming (OOP).
The basic idea of object-oriented programming (OOP) in Python is to use classes and objects to represent real-world concepts and entities.

# class
A class is a blueprint or template for creating objects.
It defines the properties and methods that an object of that class will have.
Properties are the data or state of an object, and methods are the actions or behaviors that an object can perform.

# Object
An object is an instance of a class, and it contains its own data and methods.
For example, you could create a class called "Person" that has properties such as name and age, and
methods such as speak() and walk(). Each instance of the Person class would be a unique object with its own name and age, but they would all have the same methods to speak and walk.


# Encapsulation
One of the key features of OOP in Python is encapsulation, which means that the internal state of an object is hidden and can only be accessed or modified through the object's methods. This helps to protect the object's data and prevent it from being modified in unexpected ways.

# Inheritance
Another key feature of OOP in Python is inheritance, which allows new classes to be created that inherit the properties and methods of an existing class. This allows for code reuse and makes it easy to create new classes that have similar functionality to existing classes.

# Polymorphism
Polymorphism is also supported in Python, which means that objects of different classes can be treated as if they were objects of a common class. This allows for greater flexibility in code and makes it easier to write code that can work with multiple types of objects.

In summary, OOP in Python allows developers to model real-world concepts and entities using classes and objects, encapsulate data, reuse code through inheritance, and write more flexible code through polymorphism.


Object-Oriented Programming is a methodology or paradigm to design a program using classes and objects. It simplifies the software development and maintenance by providing some concepts defined above :


'''
'''
what is object oriented programming in python


Object-oriented programming (OOP) is a programming paradigm that organizes code around objects and data rather than actions and logic. In Python, OOP is a fundamental concept that allows you to create classes and objects, encapsulate data and behavior, and build modular and reusable code. Here are the key components of object-oriented programming in Python:



Classes:
A class is a blueprint or template for creating objects. It defines properties (attributes) and behaviors (methods) that objects of the class will have.
Classes are defined using the class keyword followed by the class name, and they typically have an __init__ method (constructor) for initializing object attributes.
Example:
python
Copy code
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."



Objects:
An object is an instance of a class. It represents a specific entity with its own unique data and behavior based on the class's blueprint.
Objects are created using the class name followed by parentheses (ClassName()). Each object has its own set of attributes and methods defined by the class.
Example:
python
Copy code
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)



Attributes:
Attributes are variables that belong to an object. They hold data associated with the object's state.
Attributes are accessed using dot notation (object.attribute_name) and can be public, protected, or private based on naming conventions (_attribute for protected, __attribute for private).
Example:
python
Copy code
print(person1.name)  # Output: Alice
print(person2.age)   # Output: 25



Methods:
Methods are functions defined inside a class that perform operations on the object's data.
They can take arguments like regular functions (self refers to the current object) and can modify the object's state or return values.
Example:F
python
Copy code
print(person1.greet())  # Output: Hello, my name is Alice and I am 30 years old.


Inheritance:
Inheritance allows a class (subclass or derived class) to inherit properties and methods from another class (superclass or base class).
It promotes code reuse and hierarchy among classes, where subclasses can add new functionality or override existing methods.
Example:
python
Copy code
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def study(self):
        return f"{self.name} is studying."



Encapsulation:
Encapsulation is the bundling of data (attributes) and methods that operate on that data within a single unit (class).
It allows for data hiding, where internal details of an object are hidden from outside code, and only the interface (public methods) is accessible.
Example:
python
Copy code
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

Polymorphism:
Polymorphism allows objects to be treated as instances of their superclass, enabling flexibility and code reuse.
It includes method overriding (redefining a method in a subclass) and method overloading (defining multiple methods with the same name but different parameters).
Example (method overriding):
python
Copy code
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

def make_sound(animal):
    print(animal.speak())

dog = Dog()
cat = Cat()

make_sound(dog)  # Output: Woof!
make_sound(cat)  # Output: Meow!
In Python, OOP promotes code organization, modularity, and abstraction, making it easier to manage and maintain complex systems. It emphasizes concepts like inheritance, polymorphism, and encapsulation to create scalable and reusable code structures.








'''