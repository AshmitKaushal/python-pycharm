# Before the fstring was introduce in python
# The formmating of string done using format method
# In the format method we pass the value and it returns the new string with pass value inserted into it.

msg = 'The age of {} is {}'
# The value which is passed first is placed inside the first curly brackets and the value which passed second is placed inside the second curly brackets
res = msg.format('john',30)
print(res)


# We can also change the order by writing the indexing inside the curly brackets of the strings.
letter = 'She is {1} and she is from {0}'
letter = letter.format('Uk','ALice')
print(letter)

