# tuple is ordered collections of elements
# tuple is immutable means that once the tuple is created we cann't change it
# tuple is created using round brackets.

t1 = (19,2,3,10,30)
print(t1)
print(type(t1))

# to create the tuple with single element we use coma
t1 = (1,)
print(t1)
print(type(t1))

# Indexing in tuple
t1 = (10,20,30,50,60)
print(t1[0])
print(t1[1])
print(t1[2])
print(t1[-1])
print(t1[-2])
print(t1[len(t1)-2])


# Tuple Comprehension
t1 = (i for i in range(1,11))
print(t1)
for i in t1:
    print(i)

"""

the output <generator object <genexpr> at 0x710c7a26a7a0> indicates that tup4 is a generator object created by the generator expression (l1[i] for i in range(len(l1)) if l1[i] % 2 == 0).
A generator object is a special type of iterator in Python that generates values on-the-fly when iterated over, rather than storing all the values in memory at once like a list or tuple. When you print a generator object directly, it displays information about the generator object itself, including its type (<generator object <genexpr>), memory address, and other details.
To actually see the values produced by the generator, you need to iterate over it or convert it to another data structure like a list or tuple. For example, you can iterate over the generator to print each value:
Generators avoid creating a list or other data structure in memory to store the values as they are produced, instead replacing them one by one over time. This makes them more efficient than loops for large datasets and allows for code that runs in linear time.1

"""
import sys
t1 = (i for i in range(1,11))
print(sys.getsizeof(t1))
l1 = [i for i in range(1,11)]
print(sys.getsizeof(l1))