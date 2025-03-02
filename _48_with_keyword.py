# In Python, the with statement is used as a context manager to simplify resource management,
# especially when dealing with resources that need to be properly opened, used, and closed.
# The with statement ensures that the necessary cleanup actions are performed, even if an error occurs during execution. It is particularly useful for file handling, database connections, and other resource-intensive operations.

# if we open the file while using with then it will automatically close the file after the block of code is executed.

# as Keyword
# The as keyword in the with statement assigns the file object returned by the open function to a variable.
# This variable can then be used to perform file operations within the block of code.

with open('myfile.txt','r') as f:
    text = f.read()
    print(text)

'''
In Python, the with statement replaces a try-catch block with a concise shorthand. More importantly, it ensures closing resources right after processing them. A common example of using the with statement is reading or writing to a file. A function or class that supports the with statement is known as a context manager. A context manager allows you to open and close resources right when you want to. For example, the open() function is a context manager. When you call the open() function using the with statement, the file closes automatically after you’ve processed the file.

The with statement is a replacement for commonly used try/finally error-handling statements. A common example of using the with statement is opening a file. To open and write to a file in Python, you can use the with statement as follows:

with open("example.txt", "w") as file:
  file.write("Hello World!")
The with statement automatically closes the file after you’ve completed writing it.

Under the hood, the with statement replaces this kind of try-catch block:
f = open("example.txt", "w")

try:
  f.write("hello world")
finally:
  f.close()
The with statement ensures that the file is properly closed after you’ve finished writing it.

'''