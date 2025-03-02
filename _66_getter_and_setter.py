print("-------------------Getter-------------------")

# Getter are the methods that are used to access the value of the object properties.
# They are used to return the values of specify properties of an object and are typically defined using the "@property" keyword
# Getter are used to acces the values of the object properties (object instance variable)
# Getter are used to get the values they donot take any parameter except self
"""
what is @property decorator?

In Python, @property is a built-in decorator that allows you to define properties in classes. Properties are special attributes that have getter, setter, and deleter methods associated with them. The @property decorator is used to create a read-only property, meaning it allows you to define a method that can be accessed like an attribute but cannot be modified directly.

Here's a brief explanation of the key aspects of @property:

Getter Method: When you use @property above a method in a class, that method becomes a getter method for the property. It is called when you access the property.

Read-only Access: By default, properties created with @property are read-only, meaning you can access them but cannot modify them directly. If you try to assign a value to such a property, it will raise an AttributeError.

Syntax: The @property decorator is followed by a method name in the class. This method will act as the getter for the property.

Usage: You typically use @property when you want to compute some value 
dynamically when accessing an attribute, or when you want to provide controlled access to an attribute.
Here's an example to illustrate the usage of @property:

"""
print("----------------Test Class-----------------")
class Test:

    def __init__(self,value):
        self.value = value

    @property
    def ten_value(self):
        return self.value

t1 = Test(10)
print(t1.ten_value)
print()


print("------------------Employee Class-------------------")
class Employee:

    def __init__(self,name,role,country):
        self.name = name
        self.role = role
        self.country = country

    @property
    def getter(self):
        return self.name,self.role,self.country

    # Here we are returning multiple values from the getter method and the values will be stored in the tuple.


e1 = Employee('john','SDE','India')
print(e1.getter)

"""
In Python, when you define a method using the @property decorator, it transforms that method into a property. 
This property behaves like an attribute rather than a method, allowing you to access it without using parentheses as you would with a regular method call.

When you access s1.getter, it calls the getter method internally due to the @property decorator, 
even though you don't use round brackets after s1.getter. This behavior is by design in Python and is what allows you to use properties seamlessly with attribute-like syntax.

So, s1.getter is effectively calling the getter method, 
returning the value calculated inside the method (10 * self.marks in this case), 
just like accessing any other attribute of an object
"""


print("------------------Setter---------------------")

# Setter are the methods that are used to modify the value of the object properties.They are used to set the value of the object properties.They are typically defined using the "@property" keyword and method name.setter

# Syntax:

# @value.setter(self):
#   self.value  = new_Value

# Setter are used to set the values they take one parameter self and new_value

class Test1:

    def __init__(self,value):
        self.value = value

    @property
    def ten_value(self):
        return 10*self.value

    @ten_value.setter
    def ten_value(self,new_value):
        self.value = new_value
        self.value = (self.value/10)

    def show(self):
        print(f"The value of {self.value}")

t1 = Test1(10)
t1.ten_value = 67
print(t1.ten_value)
t1.show()