# Class-Based Decorator in Python
# A class-based decorator in Python is a decorator implemented using a class instead of a function.
# It provides more flexibility and allows maintaining state across multiple calls,
# which is harder to achieve with function-based decorators.

# To use a class as a decorator, the class must define:

# An __init__ method: This initializes the decorator and stores the function to be decorated.
# A __call__ method: This is executed when the decorated function is called.


class Mydecorator:

    def __init__(self,func):
        self.func = func

    def __call__(self,*args,**kwargs):
        print("Before calling")
        self.func(*args,*kwargs)
        print("After calling")

@Mydecorator
def greet(name):
    print(f"Hello {name}")

greet("ALice")

'''
Step 1:-
This is equivalent to:

greet = MyDecorator(greet)
Here, an instance of MyDecorator is created.
Inside the __init__ method, the original greet function is stored in self.func.
After this, the variable greet now points to the MyDecorator instance instead of the original greet function.
'''

'''
Step 2:-
What greet Represents Now:

greet is now an instance of MyDecorator.
The MyDecorator class defines a __call__ method, making its instances callable like functions.
'''

'''
Step 3:-

When You Call greet("Ashmit"):

greet("Ashmit")
Since greet is now an instance of MyDecorator, Python interprets this as:

greet.__call__("Ashmit")
Python automatically invokes the __call__ method of the MyDecorator instance
'''