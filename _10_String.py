# String is one of the datatype that is created either single or double quotes.
# Strings are the sequence of character
# Strings are created using single quotes or double quotes.

str = "THis is a string"
print(str)

# String of multi line is created either using triple single or double quotes.
str1 = '''This is a 
        multi 
        line string'''
print(str1)
print()

print("------------Indexing in String-----------------")
# it is used to access the particular character of the string.


print("-------------Postive Indexing-------------------")
# Positive INdexing
# Indexing in string starts with 0 and end upto (length of string -1).
str = "This is a string containing characters"
print(str[0])
print(str[1])
print(str[2])
print(str[3])
print(str[4])
print()


# Negative INdexing
print("-----------------Negative Indexing-------------")
# It starts with -1 from the last character of the string and ends on first character of the string.
# And decreases by -1 every time upto the first character of the string.

str = "This is a string containing characters"
print(str[-1])
print(str[-2])
print(str[-3])


for i in str:
    print(i,end="")
print()


str = '''THis 
is 
a multi 
line string.'''
for i in range(len(str)):
    if str[i]!='\n':
        print(str[i],end='')


