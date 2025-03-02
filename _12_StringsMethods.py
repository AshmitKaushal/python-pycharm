# Length method return the count of number of characters in the string.
str = "String"
print(len(str))

# count method return the number of ocurrence of the particular character in the string.
str= 'Apple'
print(str.count('p'))

# centre method
# It is used to align the string to the center as per the parameter given by the user
str='apple'
print("Center",str.center(100))
print(len(str.center(100)))

# capitalizle method return the new string With the first letter capital and rest of other in small case.
str = 'appLE'
print(str.capitalize())

# title method return the new string in which first letter of each word is capital.
str = 'bank of america'
print(str.title())

#replace method is used to replace all the ocurrence of the character or sequence of character with new character or the sequence
str = 'Marry'
str1 = str.replace('M','C')
print(str1)

# UpperCase method is used return the new string that contains all the characters of the original string in upper case.
str="String"
ustr= str.upper()
print(ustr)

# lower method is used return the new string that contains all the characters of the original string in lower case.
str="String"
lstr= str.lower()
print(lstr)

# trim method is used to remove all the leading and trailing character that is passed as a arugment in this method.
# bydefault remove the whitespace.
str ='         This   '
print(len(str))
print(str.strip())

# it is used to remove all the left whitespace
str1 = str.lstrip()
print(str1.lstrip())

#it is used to remove all the right whitespace
print(str.rstrip())


# isalpha return true if the string only contains alphabets.
str = "vkndfkvlndf"
print(str.isalpha())

# isalnum return true if the string only contains alphabets and numbers.
str = "09876tghjkl*"
print(str.isalnum())

# isspace return true if the string contains whitespace.
str="THis is a string"
print(str.isspace())

# istitle return true if the first letter of the each word is capital
str = 'THis is a string'
print(str.istitle())

# startswith return true if the word starts with letter of sequence passed as a parameter in the str.
str="this"
print(str.startswith('t'))

# endswith return true if the startswith return true if the word ends with letter of sequence passed as a parameter in the str.
# we pass also pass the parameter from which index we want to starts searching in substring.
str="this is a string"
print("Ends with",str.endswith('is',5,7))

# split method split the string by the specific instance return string item as a separate element of the string.
str = 'This is a string'
newstr = str.split()
print(newstr)

# find method return index if the particular character or sequence of character is present in the string.
str = 'This is a string'
print(str.find('is'))
print(str.find('rr'))

# index method is similar to find method but if the particular character or sequence of character is not
# present in the string then it will raise an error instead of returning -1.
print(str.index('p'))

