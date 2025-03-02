class Test:
    def __init__(self,a):
        self.a = a

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def info(self):
        print("This is info method")

t1 = Test(10)
t2 = Test(100,200)


'''
We use Python’s inbuilt __init__ method to define the constructor of a class. 
It tells what will the constructor do if the class object is created.

If multiple __init__ methods are written for the same class, 
then the latest one overwrites all the previous constructors and the reason for this can be that Python
stores all the function names in a class as keys in a dictionary so
when a new function is defined with the same name, the key remains the same 
but the value gets overridden by the new function body.

'''

# If we have more than one constructor with same number of arguments,
# then internally the object of the class will always call the last/ newly created constructor.

# In python the newly created method with same as declare before always override the content of the previous one.
# In Python, you can technically define multiple methods with the same name in a class, including multiple methods with the same number of parameters. However, unlike some other programming languages like Java, Python does not support method overloading based on the number of parameters or parameter types. This means that defining multiple methods with the same name but different parameter lists in a Python class will not result in method overloading as it does in languages like Java.

# Instead, in Python, the method that is defined last in the class will overwrite any previously defined methods with the same name. When you call a method on an object, Python will look for the method starting from the object's class and then search through its inheritance hierarchy until it finds a matching method name. If it finds multiple methods with the same name, it will use the most recently defined method.
