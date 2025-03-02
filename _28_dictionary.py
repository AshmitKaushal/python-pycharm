# Dictionary is the collection of data in the form of key value pair
# where key will be always unique and values may be duplicate.
# dictionary is created using {}

d1 = {'name':'Alice','role':'SDE','age':'30'}
print(d1)
print(type(d1))

# We can access the value of the key using dictionary name[Key_name]
# if we are trying the access the value of the key and key is not present then it will return an error
print(d1['name'])


# Access the value of the key using get method
# if the particular key is not present then it will not raise an error else return none.
print("As there is no name2 inside the dictionary so it will return none ",d1.get('name2'))

# We can access all the keys of the dictonary using dict.keys() method
print(d1.keys())
print(type(d1.keys()))

# We can access all the values of the dictonary using dict.values() method
print(d1.values())
print(type(d1.values)())

# Dictionary Methods:

# keys(): Returns a view object containing the keys of the dictionary.
# values(): Returns a view object containing the values of the dictionary.
# items(): Returns a view object containing the key-value pairs as tuples.
# get(key, default=None): Returns the value for the specified key. If the key is not found, it returns the default value (or None if not provided).

# A view object in Python, specifically in the context of dictionaries, is a dynamic and iterable object that provides a "view" into the contents of a dictionary. It does not create a new copy of the data but rather reflects the current state of the dictionary.
# View objects are designed to provide efficient access and manipulation of dictionary data without duplicating memory usage.

# There are three types of view objects associated with dictionaries:

# dict_keys: This view object represents the keys of a dictionary.
# dict_values: This view object represents the values of a dictionary.
# dict_items: This view object represents the key-value pairs (items) of a dictionary as tuples.
# These view objects are returned by the keys(), values(), and items() methods of a dictionary, respectively.
# It's important to note that view objects are dynamic and reflect changes made to the underlying dictionary.
# If the dictionary is modified after obtaining a view object, the view object reflects those changes automatically.
