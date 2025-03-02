"""

The nonlocal keyword in Python is used to indicate that a variable inside a nested function is not local to that function, nor is it global.
Instead, the variable belongs to the nearest enclosing scope that is not the global scope.
This keyword is primarily used in nested functions where you want to modify a variable defined in an outer (enclosing) function.


"""
# If we want modify or access the value of a variable defined inside the outer function, inside the inner function we can use the nonlocal keyword.
# The nonlocal keyword is used to work with variables inside nested functions, where the variable is neither a local nor global variable.
# Here the nonlocal refers to the nearest enclosing scope.



def add():
    a=10
    def add1():
        a =20
        def add2():
            nonlocal a
            a = 30
            # Here the value of the variable a is not only chnaged for add2 but also for add1() also.
            print("The value of the variable a from add2",a)
        add2()
        print("The value of the variable a from add1",a)
    add1()
    print("The value of the variable a from add",a)
add()

"""

let's break down the concept of the nonlocal keyword in Python with a simpler example and explanation.

Consider the following scenario:

python
Copy code
def outer_function():
    x = 10  # Variable defined in the outer function

    def inner_function():
        nonlocal x  # Indicates that x belongs to the outer function's scope
        x += 5  # Modifying the value of x from the outer function

    inner_function()
    print("Value of x after modification:", x)

outer_function()
In this example, we have an outer function outer_function and an inner function inner_function defined inside it. The variable x is defined within outer_function, and we want to modify its value from inner_function.

Here's how the nonlocal keyword works in this context:

Default Behavior Without nonlocal:

By default, variables defined inside a function are considered local to that function. This means that x is a local variable to outer_function, and any attempt to modify x from inner_function would create a new local variable x inside inner_function, shadowing the outer x.
Using nonlocal to Access Outer Scope:

When we use the nonlocal keyword inside inner_function (nonlocal x), it tells Python that x belongs to the nearest enclosing scope that is not the global scope. In this case, x is from the scope of outer_function.
By using nonlocal, we can modify the value of x from inner_function, and the change will be reflected in the original x variable from outer_function.
Output:

When you run the code, it will print Value of x after modification: 15, indicating that x was successfully modified inside inner_function and the change persisted in the outer scope.
In summary, the nonlocal keyword allows you to access and modify variables from the nearest enclosing scope that is not the global scope. It bridges the gap between local and global scopes in nested functions, providing a way to work with variables from outer functions within inner functions.

"""