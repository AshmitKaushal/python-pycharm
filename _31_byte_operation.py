x = b'Hello'
print(x)
print(type(x))

# Indexing and Slicing
# It will return the Ascii value of the alphabets as it works with binary values.
print(x[0])
print(x[1])
print(x[2])
print(x[3])


# Concatenation
# We can concatenate two byte datas
x = b"hello"
y = b' world'
print(x+y)

# repeatition
# We can repeat the byte data by multiplying a number with it.
x = b'hi'
print(x*3)

# Membership Testing in Byte
# Checking that a particular character or sequence of character is present in the byte or not.
b = b'hello'
print(b'll'in b)

# Iterating
x = b"hello world"
for i in x:
    print(i)