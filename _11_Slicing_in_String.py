str = 'String'
print(str)

# Slicing is the extraction of a part of a string, list, or tuple.
# It enables users to access the specific range of elements by mentioning their indices.
# Syntax: Object [start:stop:step] “Start” specifies the starting index of a slice.
# “Stop” specifies the ending element of a slice ,the end element is not included.
# “Step” specifies the incrementation of the index.

# This will print the whole string.
print(str[0:])
print(str[:])
print(str[:len(str)])


print(str[0:4])

print("-------------Positive Stepping----------------")
# Stepping is third paramter that is used for the incremention or decremention.
res = str[0:len(str):2]
# This will print the every second character of the string after printing the first character.
print(res)


print("------------Negatice Stepping-----------------")
# It is used to reverse the string also.
print(str[::-1])
print(str[::-2])
str = 'String'
print(str[-1:-7:-1])
print(str[(len(str)-1)::-1])

