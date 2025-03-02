# The term bytes in Python refers to a built-in data type used to represent immutable sequences of bytes.
# Each byte is represented as an integer in the range 0-255. The bytes data type is often used to work with binary data, such as files, images, or data being transmitted over a network.

# What are Bytes?
# Definition:

# A byte is a unit of data that typically consists of 8 bits.
# In Python, the bytes type is used to represent sequences of bytes, which can store raw binary data.
# Nature of bytes:

# It is immutable (once created, it cannot be modified).
# It is a sequence type, like str or list, meaning you can:
# Access individual bytes using indexing.
# Extract parts of it using slicing.
# Iterate over the bytes.
# Purpose:

# The bytes type is designed to handle raw binary data, rather than textual data.
# While strings (str) are for text, bytes is for data like files, streams, or binary protocols.

#  A byte data type is created using prefix b or B with single ,double,triple quotes.
b = b"hello"
print(b)
print(type(b))

# We can create btype using encode in the string object.
x = "hello"
b = x.encode()
print(b)
print(type(b))

# We can create byte using byte constructor.
x = bytes([65,66,67])
print(x)
print(type(x))