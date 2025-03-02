'''
In file handling, seek() and tell() are two methods used to manipulate and
determine the current position (offset) of the file cursor within a file.
Here's a brief explanation of each:

seek(offset, whence=0):

The seek() method is used to change the current file position (cursor) within an open file.
It takes two parameters:
offset: Specifies the number of bytes to move the cursor. A positive offset moves the cursor forward, and a negative offset moves it backward.
whence (optional, default is 0): Specifies the reference point for the offset. It can take the following values:

0: Start of the file (absolute positioning)
1: Current position (relative positioning)
2: End of the file (relative positioning)
'''

f = open('myfile.txt','r')
# Now the data is started reading from the 3 index.
f.seek(3)
print(f.read())
f.close()

f = open('myfile.txt','rb')
f.seek(-10,2)
# Why This Happens
# When you open a file in text mode ('r', 'w', 'a'), Python performs additional processing, such as handling line endings (\n vs. \r\n) and character encodings (e.g., UTF-8). This abstraction makes it difficult to calculate the exact byte positions reliably.
# As a result, Python restricts seek() with whence=2 to binary mode files only.
print(f.read())
print()


print("---------------Tell Method---------------")
# the tell method return the current position of the file cursor.
# The tell() method returns the current file cursor position (offset) within an open file.
# It doesn't take any parameters and simply returns an integer representing the current position in bytes from the beginning of the file.
f = open('myfile1.txt','r')
f.seek(5)
print(f.read())
print(f.tell())