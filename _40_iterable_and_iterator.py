'''
Iterables:
An iterable (like a list or a string) is a data structure that holds a collection of elements.
For example, a list stores all its elements in memory. So, the memory used by an iterable will be proportional to the number of elements it contains.

For example:

python
Copy code
# List (Iterable)
numbers = [1, 2, 3, 4, 5]
In this case, the entire list [1, 2, 3, 4, 5] is stored in memory.
However, iterables are not necessarily inefficient when it comes to memory.
It's just that they store all their elements at once, which could be a concern for very large datasets.

Iterators:
An iterator, on the other hand, is an object that provides a way to access elements from an iterable one at a time,
without needing to store the entire sequence in memory.
When you create an iterator from an iterable using the iter() function,
the iterator doesn't actually hold all the elements of the iterable.
Instead, it simply keeps track of its current position in the sequence and returns the next element when requested.

Memory Efficiency of Iterator:
The iterator doesn't load the entire data into memory;
it just knows the current position and retrieves the next element when needed.
The iterator doesn’t store the entire collection; instead, it fetches one element at a time from the iterable,
which means it uses less memory.
'''



"""
In Python, an iterator is an object that implements the iterator protocol, which consists of two main methods: __iter__() and __next__(). Iterators are used to iterate over sequences of data, allowing you to access elements one at a time without the need to load the entire sequence into memory at once.
Here are the key characteristics and concepts related to iterators in Python:

Iterable:
An iterable is any object in Python that can be iterated over, such as lists, tuples, strings, dictionaries, sets, and more. Iterables have an __iter__() method that returns an iterator.

Iterator:
An iterator is an object returned by the __iter__() method of an iterable. It implements the __next__() method, which allows you to fetch the next element in the sequence. When you call __next__() on an iterator, it returns the next item in the sequence until there are no more items, at which point it raises a StopIteration exception.

Iteration Protocol:
The iteration protocol in Python defines how iteration works. When you use a for loop or an iterator in Python, it follows this protocol:

The iter() function is called on the iterable to obtain an iterator.
The __next__() method is called on the iterator to fetch elements one by one.
When there are no more elements, StopIteration is raised to signal the end of iteration.
"""



'''
Iterables:
An iterable (like a list or a string) is a data structure that holds a collection of elements. 
For example, a list stores all its elements in memory. So, the memory used by an iterable will be proportional to the number of elements it contains.

For example:

python
Copy code
# List (Iterable)
numbers = [1, 2, 3, 4, 5]
In this case, the entire list [1, 2, 3, 4, 5] is stored in memory.

However, iterables are not necessarily inefficient when it comes to memory. It's just that they store all their elements at once, which could be a concern for very large datasets.

Iterators:
An iterator, on the other hand, is an object that provides a way to access elements from an iterable one at a time, 
without needing to store the entire sequence in memory. When you create an iterator from an iterable using the iter() function, the iterator doesn't actually hold all the elements of the iterable. Instead, it simply keeps track of its current position in the sequence and returns the next element when requested.

Memory Efficiency of Iterator:
The iterator doesn't load the entire data into memory; it just knows the current position and retrieves the next element when needed.
The iterator doesn’t store the entire collection; instead, it fetches one element at a time from the iterable, which means it uses less memory.
'''

# Iterable
l1 = [10,20,30]

# Creating Iterator from the iterable.
iterator = iter(l1)

# Access the elements from the iterator
print(next(iterator))
print(next(iterator))
print(next(iterator))

for i in iterator:
    print(i)