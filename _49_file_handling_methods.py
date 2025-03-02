print('-------------read function------------')
# it used to return the entire content of the file as a string.
f = open('myfile.txt','r')
text = f.read()
print(text)
f.close()
print()


print('------------readline function--------')
# It is used to return one line at a once from the file as a string.
# If we want entire content of the file the we can use loop.
# Once the first line is printed then the file cursor is placed to the starting the of the new line.

# the behavior of f.readline() in Python.
# When you call f.readline() multiple times consecutively without any other operations in between,
# it reads the next line each time.
# If the file pointer is already at the end of a line, it reads an empty string (""), indicating the end of the file.

# Printing one line at a time using readline function
print("printing one line")
f = open('marks.txt','r')
text = f.readline();
print(text)
text = f.readline()
print(text)

# printing the entire content of the file using readline function.
# Bydefault the string return by the readline method content new line in the end.
print("printing entire content")
f = open('marks.txt','r')
i = 0
while True:
    i = i + 1
    line = f.readline()
    if not line:
        break
    m1 = line.split(',')[0]
    m2 = line.split(',')[1]
    m3 = line.split(',')[2]
    print(f"The marks of the student s1 in English is {m1}")
    print(f"The marks of the student s1 in Hindi is {m2}")
    print(f"The marks of the student s1 in Maths is {m3}")
    print(line)
print()

print("---------------readlines function-----------------")
# it used to return the entire content of the file as a list item.
f = open('myfile3.txt','r')
text = f.readlines()
print(text)
print()
print()

print("---------------Writelines Method---------------")
# It used to write the sequences of the string inside the file.
# we can also pass the iterable object such as list or tuple.
# whose individual elements are added at the separate line if we want.
# It does not override the previous content with new content.

f = open('myfile3.txt','w')
f.writelines('line\nline2\nline3\n')
f.close()

f = open('myfile3.txt','r')
text = f.read()
print(text)

"Pass the iterable object inside the writelines method"
# In the writelines method we can pass an iterable object such as list,tuple,dictionary,set etc.
# In that a practicular data at the particular index will be written in the file as a separate line

l1 = ['line1','line2','line3']
f = open('myfile4.txt','w')
f.writelines(l1)
l2 = ['line4\n','line5\n','line6\n']
f.writelines(l2)


# here important to note that writelines method doesn't add a new line character at the end of the file
# If We want to add newline  we can use a loop.

l1 = ['line1','line2','line3']
f = open('myfile5.txt','w')
for i in l1:
    f.write(i+'\n')
print("Now reading the content of the file using read function")
f.close()
f = open('myfile5.txt','r')
text = f.read()
print(text)
