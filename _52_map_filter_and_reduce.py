# The map ,filter and reduce are the built in functions in python.
# That is allow us to apply a function to the element of the list,tuple or other iterable object.

# These are also know as higher order functions bcz they take other functions as arguments.

print("----------------------map function------------------")
# the map function take two arguments,the first one is the function and the second one is the iterable object.

# . It is used when you want to apply a single transformation function to all the iterable elements. The iterable and function are passed as arguments to the map in Python.

# The map function returns a map object which is an iterator.

# The map function applies the function to each element of the iterable object and returns a new iterable object containing the transformed elements.

# The map function is used when we have to tranformed each element of the iterable object.

'''
  Syntax:
  map(function, iterable))
'''

l1 = [1,2,3,4,5]
print("The original list l1 is",l1)
res = list(map(lambda x:x*x,l1))
print("The transformed list is ",res)
print()

print("----------------------filter function------------------")
# The filter function takes two arguments,the first one is the function and the second one is the iterable object.
# It used to apply a function to each element of the iterable object and returns a new iterable object containing only the elements for which the function returns True.
# The filter function returns a filter object which is an iterator.

l1 = [1,2,3,4,5]
res = list(filter(lambda x:x%2==0,l1))
print("Original list",l1)
print("Filtered list",res)
print()

print("---------------------reduce function-------------------")
# the reduce function takes two arguments,the first one is the function and the second one is the iterable object.
# The reduce function is applied to the first two element of the iterable object and then the result is applied to the next element and so on.
# The reduce function used when we want single values as an output.

from functools import reduce
l1 = [1,2,3,4,5]
res = reduce(lambda x,y:x+y,l1)
print("The summation of all the values of the list l1 is",res)