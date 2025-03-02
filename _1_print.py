# Print function in python is used to print the text or object.
print("Hello World")

# To used the data on multiple lines used either single triple quotes or double triple quotes
print("""
    THis is  a
    statment1 
    """)

print('''
    THis is  a
    statment2 
    ''')

'''
The print() function in Python is an object of the built-in builtin_function_or_method type, which is a part of Python's object system.

Understanding print() as an Object
Type of print:

python
Copy code
print(type(print))
# Output: <class 'builtin_function_or_method'>
print is a built-in function object. It is implemented in C (for CPython) and exposed to Python programs.
What It Represents:

print is a reference to a callable object provided by the Python runtime.
Internally, print is part of Python's built-in namespace and directly tied to the C implementation of the print() function.
How print() Works Internally
Function Signature:

python
Copy code
def print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False):
    pass
It takes any number of objects and formats them into a string.
The string is written to the standard output (or a file if specified).
Implementation in CPython:

In CPython, print() is defined in C as part of the core library (Python/bltinmodule.c).
When you call print(), the Python interpreter internally calls the C implementation, which writes the formatted string to the desired output stream.
Core Steps:

Python evaluates the arguments passed to print().
Converts the objects to strings using their __str__ or __repr__ methods.
Joins the strings using the sep argument.
Appends the end string.
Writes the resulting string to the file object (default is sys.stdout).
print() as a First-Class Object
Since everything in Python is an object, you can:

Pass print as an argument.
Assign it to a variable.
Store it in a data structure.
Example:
python
Copy code
# Assign print to a variable
my_print = print
my_print("Hello from my_print!")  # Output: Hello from my_print!

# Store print in a list
functions = [print, len, sum]
functions[0]("This is stored in a list!")  # Output: This is stored in a list!
Can We Replace or Override print()?
Yes, since print is just a reference, you can override or replace it.

Example:
python
Copy code
print = lambda x: "Print is overridden!"
print("Hello!")  # Output: Print is overridden!

# Restore the original print
del print
print("Hello!")  # Output: Hello!
'''

print("Hello",sep='!')