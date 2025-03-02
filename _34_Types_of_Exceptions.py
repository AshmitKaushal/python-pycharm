a = 10
b = 0

print("------- ZeroDivisionError--------")

# 1 .ZeroDivisionError:
# Raised when dividing by zero.

try:
    print(a/b)
except ZeroDivisionError as e:
    print(e)

# 2. IndexError
# Raised when trying to access an index that is out of range in a list or tuple.
print("------------IndexError--------------")
l1 = [1,2,3]
try:
    print(l1[8])
except IndexError as e:
    print(e)

# 3. KeyError
# Raised when trying to access a key in a dictionary that does not exist.
# Return the key itself not any object message.
print('---------------KeyError--------------')
try:
    d1 = {'name':"alice"}
    print(d1['country'])
except KeyError as e:
    print(e)

# 4. TypeError
# Raised when an operation or function is applied to an object of inappropriate type.
print("--------------TypeError--------------")
try:
    print("hello"+5)
except TypeError as e:
    print(e)

# 5. ValueError
# Raised when a function receives an argument of the right type, but an inappropriate value.

print('------------------ValueError----------------')
try:
    c = int("Hello")
    print(c)
except ValueError as e:
    print(e)

# 6. NameError
# Raised when a local or global name is not found.
try:
    print(d)
except NameError as e:
    print(e)