class Test:

    def __init__(self):
        print("Default Constructor")

    def __init__(self,a):
        self.a = a

    def __init__(self,a,b):
        self.a = a
        self.b = b

t1 = Test()
t2 = Test(10)
t3 = Test(100,200)

# If multiple __init__ methods are written for the same class, then the latest one overwrites all the previous constructors and
# the reason for this can be that Python stores all the function names in a class as keys in a dictionary so when a new function is defined with the same name, the key remains the same but the value gets overridden by the new function body.


# This class namespace is simply a dictionary mapping the attributes
# and methods of the class to function implementation in memory.
# Now dictionaries cannot have repeated keys so Python does not have function overloading.

'''
why the methods are stored in __dict__ of the class not in instances __dict__
ChatGPT said:
ChatGPT
The methods in Python are stored in the class's __dict__ and not in the instance's __dict__ because it ensures memory efficiency and allows shared access to the same method definition across all instances of the class. Here's a detailed explanation:

1. Memory Efficiency
If methods were stored in every instance's __dict__, each instance would require additional memory to store identical copies of methods. By storing methods in the class-level __dict__, all instances can share the same method, saving memory.

Example:
python
Copy code
class MyClass:
    def my_method(self):
        pass

obj1 = MyClass()
obj2 = MyClass()

# Memory address of the method for both objects
print(obj1.my_method)  # <bound method MyClass.my_method of <MyClass object at 0x...>>
print(obj2.my_method)  # <bound method MyClass.my_method of <MyClass object at 0x...>>
The method definition is shared, but it dynamically binds to different instances (obj1 and obj2) when accessed.
2. Dynamic Binding
When you access a method on an instance, Python dynamically converts the method into a bound method, associating it with the specific instance. This dynamic binding happens only at the time of the method call, not during the instance creation.

Example:
python
Copy code
class MyClass:
    def my_method(self):
        return "Hello from instance!"

obj = MyClass()
print(obj.my_method)  # <bound method MyClass.my_method of <MyClass object at 0x...>>
The method my_method is not stored in the instance. Instead, it is retrieved from the class, and obj is passed as the first argument (self).
3. Shared Behavior Across Instances
Methods define behavior that is typically the same for all instances of a class. Storing methods in the class's __dict__ ensures that all instances share the same behavior without redundancy.

Example:
python
Copy code
class MyClass:
    def greet(self):
        return "Hello!"

obj1 = MyClass()
obj2 = MyClass()

# Both instances share the same method implementation
print(obj1.greet())  # Output: Hello!
print(obj2.greet())  # Output: Hello!
If methods were stored in each instance, modifying the method in one instance would not reflect in others, breaking shared behavior.
4. Separation of State and Behavior
State: Instance-specific data (attributes) is stored in the instance's __dict__.
Behavior: Shared methods and class-level attributes are stored in the class's __dict__.
By this separation:

Each instance only stores its unique data, avoiding redundancy.
Methods remain centralized and consistent in the class.
Example:
python
Copy code
class MyClass:
    def my_method(self):
        return self.data

obj1 = MyClass()
obj1.data = "Data for obj1"

obj2 = MyClass()
obj2.data = "Data for obj2"

# Method is shared, but behavior depends on instance-specific data
print(obj1.my_method())  # Output: Data for obj1
print(obj2.my_method())  # Output: Data for obj2

5. Simplifies Method Resolution
Python uses the Method Resolution Order (MRO) to look for attributes and methods. Storing methods in the class's __dict__ ensures that Python can efficiently resolve method calls by traversing the class hierarchy.

Why Not Store in Instance __dict__?
Redundancy: Every instance would store its own copy of the method, leading to unnecessary memory usage.
Breaking Shared Behavior: Changes to a method in one instance would not propagate to others, defeating the purpose of class-based shared behavior.
Method Resolution Complexity: Searching for methods in each instance's __dict__ would make the method lookup slower and less efficient.
Summary:
Methods are stored in the class's __dict__ for memory efficiency, shared behavior, and simplified method resolution.
Instances store only their unique state (attributes), while all instances share the same methods defined at the class level.
This design ensures Python remains dynamic, flexible, and efficient.
Let me know if you'd like more examples or clarifications! 😊

'''