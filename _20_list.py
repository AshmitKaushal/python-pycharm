# list in python are the collections of similar or different data types values;
# list is ordered collection of data items this means that each item has a unique index and we can access any item using this index.
# list are changeable means we can change any item in the list.
# list is created using square brackets.[]

l1 = [10,20,30,40]
print(l1)
print(type(l1))

# Indexing in list
# Indexing in list is same as string. it also starts from 0
# Indexing is the process of accessing the value of an item in a list using its unique index.
# Indexing is done using square brackets.

print("----------------------Positive Indexing-----------------------")
print(l1[0])
print(l1[1])

print("----------------------Negative Indexing-----------------------")
print(l1[-1])
print(l1[len(l1) - 1])


print("-------------------------Stepping In List---------------------")
# We can also skip the items in the list using the step value.
# Stepping is basically incrementing the value of index by a given value.
# Step is the 3 parameter in square rackets.
# Syntax :
#       list[start:end:step]

# Suppose we want to print the every second element of the list.
print("Printing the values of the even indexes")
l1 = [10,20,30,40,50,60]
print(l1[0:len(l1):2])


# Checking that whether the value is present in the list or not using memebership operator
print("Is apple present in the list","apple" in l1)
print("Is 60 present in the list ",60 in l1)


print(
    "------------------------List Comprehension------------------------------")
# list Comprehension
# list Comprehesion is used for creating new lists from other iterable like list,tuple,dictionary,sets
# and even in arrays and strings.

# Syntax:
# list = [Expresion(item) for i in iterable if(condition) to add or not]

# Expresion = It is the that is being iterated.It is the value that is being added to the new list.
# Iterable =  It can be list,tuple,dictionary,set,array and string.
# Condition = Condition checks whether the item should be added to the new list or not.


l1 = [10,20,30,40]
l2 = [i*i for i in l1]
print(l2)
print(type(l2))

# # Here we are creating a new list using a already created list
# # we can also using tuple,dictoriary etc...
l3 = [10,20,30,40,50,60,70,80,90,100]
l4 = [i for i in l3 if i>30]
print(l4)


# The basic syntax of list comprehension in Python is as follows:
'''new_list = [expression for item in iterable if condition]'''

# Here's what each part of the syntax represents:

# expression: This is the expression to be evaluated for each element in the iterable.
# It can involve the item variable, which represents the current element being processed.

# item: This variable represents each element in the iterable.

# iterable: This is the original iterable (e.g., a list, tuple, or string) from which elements are taken to create the new list.

# condition (optional): This is an optional condition that filters elements from the original iterable.
# Only elements for which the condition evaluates to True are included in the new list.


# Creating the list which contains tuple inside it as individual element.
print("----------Creating list which contains tuple as a element---------")
l5 = [10,20,30,40,50]
l6 = [((i*i)) for i in l5]
print(l6)
print(type(l6[0]))

l5 = [10,20,30,40,50]
l6 = [(i,i*i) for i in l5]
print(l6)
print(type(l6[0]))


print('-------Creating list which contains dictionary as a element-------')
l1 = ["apple",'mango','banana','kiwi']
d1 = [{i:len(i)} for i in l1]
print(d1)
print(type(d1[0]))

print('-------Creating list which contains sets as a element-------')
l1 = [10,20,30,40,50]
s1 = [{i} for i in l1]
print(s1)
print(type(s1))
print(type(s1[0]))