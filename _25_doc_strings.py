# The docstrings are the string liternal which are written just below the function name,class,method or module .
# The docstring are used to describe the function,class,method or module.
# In short explain the document of the code.
# The docstrings are not ignored by python interpreter.

# The doctstrings are printed using class , function, method or with module name.
# The doctstrings can be of multiple lines

def add(a,b):
    '''
        This is a function which perform addition of the two number.
        Allow to accept int values to perform the addition of passed values.
        c = a+b
        :return a+b:
    '''

    return a+b

add(10,20)
print(add.__doc__)


# Difference Between the comments and docstring.
