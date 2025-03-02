# finally block is always executable block either the exception occurr or not
# The finally block is always executable block either the exception occurred or not
# The finally block is usuaully used with return statement bcz if we return from statement
# and we want to print the a particular statement  every time then we use finally block


# try:
#     print(10/0.0)
# except Exception as e:
#     print(e)
# finally:
#     print("It is always executable block")


def div(a,b):
    try:
        c = (a/b)
        return c
    except ZeroDivisionError as e:
        print(e)
    finally:
        return "THis is always executable statement"
res = div(10,10)
print(res)

# if we use return statment inside the finally then it will ovveride the last return value means override the try
# in this program.

# The try block attempts to divide a by b.
# If the division succeeds without errors (i.e., no division by zero),
# it will return the result of a / b (which is stored in c).
# In the case where the division is successful, c would be returned as the result of the function.
# However, note that the function has a finally block,
# which means even if an exception occurs, or a value is returned from the try block,
# the finally block will execute, and any value returned from the finally block will override the return value
# from the try block.


def div1(a,b):
    try:
        c = a/b
        return c
    except ZeroDivisionError as e:
        return e

res = div1(10,0)
print(res)