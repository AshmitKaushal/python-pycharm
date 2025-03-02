# Decorator is the function that another function done some moditification and return it.
# Suppose we add function that perform addition of the numbers
# We want before the addition of the function greeting to the use
# So we will use decorator

# The problem is that if we have 1000 of function modifying the 1000 of function is time-consuming and complex
# instead we use decorator function which will be called before the function calling.

# Decorator is the function that takes another function as a argument return the new function which modify the behaviour of the original function.
# The new function is often refered as the decortor

# Decorator are the functions that take another function done some modification in that and return it.

#Decorator is a powerful and verstile tool that allows you to modify the behavior of functions and methods. It is a way to extend the functionality of a function or method without modifying the source code.

# A Decorator is a function that take another function as an argument and return a new function that modifies the behaviour of the original function. The new function is often referred to as a "decorator function"

# In Python, a decorator is a design pattern that allows you to modify the behavior of functions or methods. Decorators are implemented using the @decorator_name syntax, where decorator_name is a function that takes another function as an argument and typically returns a new function that enhances or modifies the behavior of the original function.

# when you apply a decorator to a function in Python, the memory allocation for the original function is essentially replaced by the memory allocation for the wrapper function created by the decorator. This means that the original function is no longer accessible from outside the decorator, and any references to it will not work.

# The basic syntax is :
# @greet
# def hello():

# If we are using @greet decorator on a function,then first greet function is called which takes hello function as an argument and returns a new function that modifies the behaviour of the original function.

# The new function is often referred to as a "decorator function"

print("--------------------Decorator function without decorator function---------------")
def greet(fx):
    def mfx():
        print("Before calling the function")
        fx()
        print("After calling the function")
    return mfx

def hello():
    print("This is a hello function")

hello = greet(hello)
hello()
print()

print("-----------------Decorator Keyword------------------")


def greet1(fx):
    def mfx():
        print("Before calling the function")
        fx()
        print("After calling the function")
    return mfx

@greet1
def hello1():
    print("This is the hello function")

hello1()
print()

print("---------Passing Arugment while using decorator--------------")

def greet2(fx):
    def mfx(a,b):
        print("Before calling the function")
        fx(a,b)
        print("After calling the function")
    return mfx

def add1(a,b):
    print(a+b)

greet2(add1)(10,20)