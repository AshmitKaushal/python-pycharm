# Enumerate is a built-in function in python that is used to iterate over a sequence.

# such as list , tuple, string, dictionary, etc.

# And get the indexes and values of each element in the sequence at the same time.

# In enumerate function there are two parameters, first is iterable object and the second is start index from which index we want start iterating.

# If we don't pass the second parameter then it will start from 0 by default.

# Syntax:
'''
    for index,value in enumerate(sequence,start=0):
        # code

    Here enumerate is the function in which iterable object is passed as an
    argument.

    if we are using enumerater function then we dont have to use the range function

'''
"""
The enumerate function returns an enumerate object, which is an iterator that generates
tuples containing the index and value pairs.
You can convert this enumerate object to a list or iterate over it directly in a loop. 
"""

"""
When to Use enumerate()?
Tracking the index: When you need both the index and the value of elements in a loop, enumerate() makes the code cleaner and more Pythonic compared to manually maintaining an index variable.
Enumerating over iterables: It can be used with any iterable, such as lists, strings, and tuples.
"""

print("------------Enumerate Function------------")
l1 = [10,20,30,40,50]
for index,value in enumerate(l1):
    print("Index",index,"Value",value)

'''
    if in place of index,value only one variable is used 
    then it return the data in the form of tuple

      for t in enumerate(sequenece):
        # code 

    Here t is the tuple which contains the index and value of the element in the sequence.

    The data in packet in the form of the tuple is stored in the variable t.
'''
print("---------------------The data in tuple form-------------------------")
l2 = [100, 200, 300, 400, 500]
for t in enumerate(l2):
  print("In tuple form", t)
  print(f"The value at index {t[0]} is {t[1]} {type(t)}")
print()


print('------------Printing using the start index-----------------')
# Starts the iteration from the first index (1).
l2 = [100, 200, 300, 400, 500]
for t in enumerate(l2,1):
    print(t)



