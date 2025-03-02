# In python if we import an module then we can access the functions and variables defined in that module
# But if the imported module also print something then default that is also printed in our code also

# Example
# Here I have imported the module named own_module and then I have used the function
# defined in that module
# The module that i am importing is ownmodule.py also print the function due to which
# a definition of the function is printed ones extra then it is called.

import _42_own_module
_42_own_module.welcome()



# Here the definition of the function welcome is printed twice bcz the module that we are importing and also calling welcome function due to which we getting the output twice.
# To avoid that in python we have if __name__=="__main__"
# In Python, the if __name__ == "__main__": block is used to define the main entry point of a Python script or module.
# It allows you to write code that will only be executed when the script is run directly, not when it is imported as a module into another script.

'''

Here's a breakdown of how it works:

Module Execution vs. Import:
When a Python script is executed directly (e.g., using python script.py), it is considered the main module being run. On the other hand, if the script is imported as a module into another script, it is not the main module but rather a module being imported.

__name__ Attribute:
Every Python module has a built-in __name__ attribute. When the module is run directly, __name__ is set to "__main__". When the module is imported, __name__ is set to the module's name (e.g., "module_name").

Usage of if __name__ == "__main__": block:
By using if __name__ == "__main__":, you can write code that should only run when the script is executed directly. This is commonly used for script initialization, testing, or running specific tasks when the script is invoked directly from the command line.

'''
