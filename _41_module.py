"""
In Python, Modules are simply files with the “. py” extension containing Python code that can be imported inside another Python Modules Operations Program.
 In simple terms, we can consider a module to be the same as a code library or a file that contains a set of functions that you want to include in your application.

With the help of import keyword module we can use the code written in the other file into the current file.

Syntax:
import module_name


To import everything from a module we use *
Syntax:
from math import *



As is the keyword that is used to give the alternate name to the module.
Syntax:
import module_name as short_name



Giving the alternate name to the function of the module.
from math import sqrt, pi as p

here pi function is used as p

"""

print("-------------Importing math module----------------")
import math
# math is the module name and sqrt is the function name that is called with module name.
print(math.sqrt(25))
print()

# To not call the function with module name we can use from keyword to specify the things we want to import from the module.
print("---------------------Using from Keyword------------------")
from math import sqrt
# now the sqrt function can be used without the module name.
print(sqrt(25))
print()

print("--------------Using * to import Everything from the module------------")
from random import *
# It will generate the random number between 1 to 10
print(randint(1,10))
print()

print("------------------Using As Keyword-------------------")
# We can use as keyword to give the alternate name to the modules.
import math as m
print(m.sqrt(25))
print()


print('---------------Give Alernate name to functions of the module-----------')
from math import sqrt as s
print(s(24))
print()

print('-----------------dir function-------------')
# dir is used to view the list of all the functions and variables defined in the module.
print(dir(math))
print(dir(math)[0])

