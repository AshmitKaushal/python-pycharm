# lambda function is a small anonymous function.
# A anonymous function is a function without name.
# lambda function is defined with help of lambda keyword.
# lambda function can have variable of numbers of parameters but have only one expression.
# lambda function is created when a small function is used for the shorter period of time.
# lambda function is often pass as an arugment to the higher order function.


# def cube(x):
#     return x*x*x

# print(cube(5))

'''
A lambda function in Python is a small anonymous function that can have any number of arguments but only one expression.
It is defined using the lambda keyword, which is followed by a list of parameters (if any), a colon :, and an expression.

Here's the general syntax of a lambda function:

python
Copy code
lambda arguments: expression

Lambda functions are typically used when you need a simple function for a short period of time,
often as an argument to higher-order functions like map(), filter(), and sorted(), or within list comprehensions.
'''

print("-----------Defining Lambda Function---------------")
cube = lambda x: x*x*x
print(cube(5))

avg = lambda x,y:(x+y)/2
print(avg(10,20))


print("----------Passing the function As a Arugment----------------")
# Passing Function as an Argument

# In Python, functions can be passed as arguments to other functions.
# This allows you to encapsulate a function within another function.
# Here's an example of a function that takes another function as an argument:

def add(fx,value):
    return 6+fx(value)

print(add(lambda x:x*x,2))


'''
Sure, let's break down how the code works:

Function Definition:

def add(cube, val): defines a function named add that takes two arguments: cube (which is expected to be a function) and val.
Function Call:

add(lambda x: x*x*x, 2) calls the add function with two arguments:
The first argument is a lambda function lambda x: x*x*x which cubes the input x.
The second argument is 2, which will be passed as val.
Lambda Function:

The lambda function lambda x: x*x*x takes an input x and returns its cube (x*x*x).
Function Body Execution:

Inside the add function, cube(val) is called, which means the cube function (in this case, the lambda function) is executed with val (which is 2) as its argument.
So, cube(2) evaluates to 2*2*2, which is 8.
Return Value:

return 10 + 8 in the add function calculates to 18.
Print Statement:

print(add(lambda x: x*x*x, 2)) prints the return value of the add function, which is 18.

Therefore, when you run the code, it will output 18 because the lambda function cubes the input 2 (resulting in 8), and 8 is added to 10 inside the add function, resulting in 18.

'''
print((lambda x,y:x*y)(10,20))
# This is same as
multiply = lambda x,y:x*y
print(multiply(10,20))

print("-------------list comprehension inside lambda function-----------")
# we can't use loop inside the lambda function but we can use list comprehension.
res= lambda x:sum([x for i in range(x)])
print(res(5))

'''
The map() function in Python is a built-in function that applies a specified function to each item of an iterable 
(such as a list, tuple, etc.) and returns an iterator that yields the results.

the map function bydefault return an iterator object that is an map

Here's the general syntax of the map() function:

python
Copy code
map(function, iterable)
function: The function to be applied to each item in the iterable.
iterable: The iterable (e.g., list, tuple) whose items will be passed to the function.
The map() function essentially performs a one-to-one mapping of elements from the input iterable to the output iterable by applying the specified function to each element. It's a convenient way to apply a transformation or calculation to every item in a collection.

Here's an example to illustrate how map() works:
'''
l1 = [10,20,30,40]
res = map(lambda x:x*x,l1)
print(res,type(res))

'''

The filter() function in Python is a built-in function that is used to construct an iterator from elements of an iterable (such as a list, tuple, etc.) for which a specified function returns true. It filters the elements based on the given function's criteria.

Here's the general syntax of the filter() function:

python
Copy code
filter(function, iterable)
function: The function that defines the criteria for filtering. It must return True or False.
iterable: The iterable (e.g., list, tuple) containing the elements to be filtered.
The filter() function applies the specified function to each element in the iterable and includes only the elements for which the function returns True in the resulting iterator.

Here's an example to demonstrate how filter() works:

'''
l1 = [1,2,3,4,5,6,7]
res = filter(lambda x:x%2==0,l1)
print(res,type(res))
# The Iterator is an efficient way to iterate over a collection, especially when we have a large amount of data.
# The Iterator provides a safe way to remove elements from a collection during iteration without causing any concurrent modification exceptions.

# The iterator is an object that allows you to traverse through the elements of a collection.
# It provides a way to access individual elements one by one without exhausting the entire collection.

# I want to say in lambda function first the definition of the function is written then it is assign to a variable ?
# ChatGPT
# Yes, that's correct! In a lambda function, you first define the function inline using the lambda keyword, and then you can assign this lambda function to a variable. This variable then acts as a reference to the lambda function, allowing you to call the function using the variable name.


l1 = [10,20,30,40]
res = list(map(lambda x:x*2,l1))
print(res)