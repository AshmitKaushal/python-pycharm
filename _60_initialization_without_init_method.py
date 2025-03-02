# if we are not using init method then how the initialization of the object in done?

# If you don't explicitly define an __init__() method in a Python class, the initialization of an object can still occur through an implicit mechanism provided by Python. This mechanism involves the use of the default constructor provided by Python.

# When you create an object without an __init__() method in the class, Python automatically uses a default constructor to initialize the object. This default constructor doesn't perform any specific initialization unless you provide default values for attributes directly in the class definition.

# Here's how the initialization works without an explicit __init__() method:

# Default Initialization:

# When you create an object of a class without an __init__() method, Python initializes the object by allocating memory for it and creating an empty object.
# Attribute Assignment:

# If the class defines attributes with default values directly in the class definition, those attributes are automatically initialized with their default values when an object is created.

# For example, consider a class without an __init__() method but with default attribute values:

class Person:
    name = "anonymous"
    age = 0

p1 = Person()

# After creating an object from such a class,
# you can access its default attributes directly using dot notation (object_name.attribute_name).
print(p1.name)
print(p1.age)


# Dynamic Attribute Assignment:
# You can also dynamically assign attributes to an object without an __init__() method
# after object creation using dot notation.

p2 = Person()
p2.country = "India"
print("---------Details of the persion p2-------------")
print(p2.name)
print(p2.age)
print(p2.country)


# In summary, if you don't define an __init__() method in your class, Python provides a default constructor that initializes objects by creating an empty object. Attribute initialization can occur through default values defined in the class or dynamically after object creation.
# However, using an __init__() method allows for more explicit and controlled initialization of object attributes during object creation.