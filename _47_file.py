# python provide several opertions to perform on file
# Before we perform any operation on file the must be open it.

# Python provide open function to open the file,this function take two argument,the name of the file and mode in which
# the file must be open.
# r is the reading mode, w is the writing mode, a is the appending mode

# The open function bydefault return the file object does not print the content of the file.

# When you print a file object in Python, it typically prints information about the file object itself,
# such as its type and memory address, rather than the contents of the file.
# The exact output you see may vary depending on the Python environment you are using.

f = open("myfile.txt",'r')
# Here we are printing the file object.
print('-----------Printing the file object------------')
print(f)

# To read the content of the file , we can use the read function of the file object.
# We have call the read function with the file object.

print('--------------Reading Function----------------')
text = f.read()
print(text)
print()

print('-------------Writing Function-----------------')
# The write function is use to write the content inside the file.
# write function override the previous content of the file with new content.
# if the file is not create then it first creates the file and then write content inside the file.
# write is the function which is used with the file object to write the content inside the file.

f = open('myfile1.txt','w')
f.write('The file is created and its new content')
f.close()
print()
print()

print('---------------Append function-------------------')
# The a is the append mode inside the open function.
# the write function is used to add the content to the end of the file.
# It will not override the previous content of the file with new content.
# if the file is not created then the file is created first and then the content is insert.
f = open('myfile2.txt','a')
f.write('Appending the content inside the file.')
f.close()
print()
print()

print('--------------------Text Mode-----------------')
f = open('myfile.txt','rt')
# The 't' is used to open the file in text mode
text = f.read()
print(text)
print()
print()

print('--------------Binary Mode------------------')
f = open('myfile.txt','rb')
text = f.read()
print(text)
print()
print()

# close() is the function that is used to close the file.
# It is important to close the file after you are done with it.

# When you print a file object in Python using the print() function, it prints a representation of the file object, which includes information about the file such as its name, mode, and whether it's closed or not.
# The printed output may vary depending on the specific implementation of the __str__() or __repr__() methods for file objects in Python.
# The __str__() method is used to return a string representation of the file object. It is called when you

# read(size=-1): Reads and returns the specified number of bytes (size) from the file. If size is not specified or negative, reads the entire file.
# readline(size=-1): Reads and returns the next line from the file. If size is specified, reads at most size bytes.
# readlines(hint=-1): Reads and returns a list of lines from the file. If hint is specified, reads at most hint bytes or lines.

