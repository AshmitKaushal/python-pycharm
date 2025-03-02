'''

In Python, the for loop is used to iterate over a sequence (such as a list, tuple, string, or range) or other iterable objects. It allows you to execute a block of
code for each item in the iterable.

'''

# 1. Iterating over the list
l1 = [10,20,30,40,50]
for i in l1:
    print(i,end=' ')
print()

# 2. Iterating over the string
str = "This is a string"
for i in str:
    print(i,end='')
print()

# 3. Iterating over the tuple
t1 = (10,20,30)
for i in t1:
    print(i,end=' ')
print()

# 4. Iterating over the dictionary
d1 = {'name':"John",'age':90}
for i in d1:
    print(i,":",d1[i],end=' ')

# Range function in python is used to return the sequence of values
# In range function we can pass three parameters
# start : starting value of the loop
# stop :  stopping value of the loop
# step : It is used for the incremention in loop

# Bydefault it returns the value from 0 to range -1 value
# Range with stop:

for i in range(5):
    print(i)

# Range with start and stop:
for i in range(1,10):
    print(i)

# Range with start,stop and step
for i in range(1,11,2):
    print(i)


# Reverse loop
for i in range(10,0,-1):
    print(i)