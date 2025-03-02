# Default Arugment
# Types of function Arugments

# 1.  Default Arguments
# Default arguments have default values specified in the function definition. If a  argument is not provided during the function call,
# then the  default value is used.
# Default arguments are useful for making certain parameters optional.
# Default argument are provided during the function definition.
# It is know as default argument bcz the parameter is acutally representing the argument values.
# Here's an example:

print("---------------Default Arugment-------------")
def add(a=10,b=200):
    return a+b

print(add())
print(add(100))
# If we want to pass only the second parameter then we have write the name of the parameter and then the value to it.
# Bydefault it is passed to the first parameter.
print(add(b=300))


# 2.# 2  Keyword Argument
# # Keyword arguments are specified by their parameter names during the function call.
# Unlike positional arguments, the order of keyword arguments does not matter.
# This type of argument allows for more flexibility and clarity when calling functions, especially with functions
# that have many parameters.
# Here's an example:

print("-------------Keyword Arugment-------------")
def greet(name,age):
    return f"The age of {name} is {age}"

print(greet(age=30,name='Alice'))


# 3.Required Arugment
# if the function parameter does not contains default value
# then it is required to pass the value during the function call.

# Here it is nessecary to pass the value of a,b
def add(a,b,c=1):
    return a+b+c

print(add(10,20))




# 4. Variable length Arugment
# Sometimes, you may want to pass a variable number of arguments to a function.
# This can be done by using the * symbol before the parameter name.
# The * symbol allows the function to accept an arbitrary number of arguments.

# Here's an example:
# the paramter with * is called as variable length argument and it is tuple
# def add(*args):
# *args is the tuple


def sum(*args):
    print("The datatype of the args is",type(args))
    sum = 0
    for i in args:
        sum = sum + i

    return sum

print(sum(1,2,3,4))

# 5. Keyword Arbitrary Argument
# Sometimes, you may want to pass a variable number of keyword arguments to a function. This can be done by using the ** symbol before the parameter name.
# The ** symbol allows the function to accept an arbitrary number of keyword arguments.
# the parameter with double ** is called as keyword arbitrary argument and it is dictionary

# def greet(**kwargs):

def employee(**kwargs):
    print("The data type of the kwargs",type(kwargs))
    for i in kwargs:
        print(i)

employee(name='Alice',role='SDE',age=30)


