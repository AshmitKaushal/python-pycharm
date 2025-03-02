# In Python, the raise statement is used to explicitly raise an exception or error during program execution.
# When you use the raise statement, you indicate to Python that a particular condition or situation warrants an exception,
# and you specify the type of exception to be raised.

# The raise statement is used to raise an exception, which is an error that occurs during program execution.

# The general syntax of the raise statement is as follows:

# raise exception_type("Optional error message")
# Here's a breakdown of each part of the raise statement:

# raise: This keyword is used to raise an exception.

# exception_type: This specifies the type of exception to be raised. It can be a built-in exception class
# (e.g., ValueError, TypeError, ZeroDivisionError, etc.) or a custom exception class that you have defined.

# "Optional error message": This is an optional argument that allows you to provide additional information about the exception.
# It is typically a string describing the reason for raising the exception.

# Creating a user define exception

print("-----------Using raise keyword for user define exception inside the function-----")
def div(a,b):
    try:
        if b==1:
            raise ZeroDivisionError("division by one")
        else:
            print (a/b)
    except Exception as e:
        print(e)

res = div(10,1)
print(res)



# raise keyword is used to throw the exception also.

print("--------Using the raise keyword to throw an exception--------")
def division(a,b):
    if b==1:
        raise ZeroDivisionError("Division by one")
    return a/b

try:
    res = division(10,1)
    print(res)
except ZeroDivisionError as e:
    print(e)
