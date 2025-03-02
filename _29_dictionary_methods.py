# Dictionary Methods
d1 = {'name':'ALice','role':'SDE','age':40}
print(d1)
print(type(d1))

print('----------------------Get Method------------------')
# Accessing the value of the key using get method
print(d1.get('name'))

print('----------------Adding the element in the dictionary-------------------')
# Adding the element in the dictionary
d1['country'] = 'Uk'
print(d1)

print('-------------------Update Method------------------------')
# it is used to add the key-value in the dictionary
d2 = {'name':'john','fruit':'mango'}
d1.update(d2)
print(d1)

print('---------------Pop method-----------------')
# It is used to remove key value pair from the dictionary which is passed as key in the method
print(d1.pop('fruit'))
print("After deleting the fruit key from the dictionary",d1)

print('----------------popitem method------------')
# It is used to remove the last key-value pair from the dictionary
# It return the poped item also.
print("After deleting the last key value pair from the dictionary")
print(d1.popitem())

print('---------------------Clear method--------------')
# it is used to delete all the elements of the dictionary
d2 = {'name':'Alice','age':30}
print(d2.clear())
print("After clear method d2 is empty now",d2)

print('----------------del keyword-----------------')
# It is used to delete the dictionary itself.
del(d1)
# Now the dictionary d1 is deleted so it will give error.
# print(d1)