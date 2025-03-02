# local variables are the variables which are defined inside the functions,classess,modules
# global variables are the variables which are defined outside the functions,classess,modules

x = 10

print("-------------Local and Global Variable-------------")
def add(a,b):
    # y is the local variable which is defined inside the function add.
    y = 20
    print(a+b)
    print("Local variable y and its value is",y)
add(10,20)
# x is the global variable which is defined outside the function.
print("global variable x and its value is",x)
print()

# If we want to create,access or change the value of the global variable inside the function.
# we can done with help of global variable.

print("-------Accessing the value of the global variable inside the function------")
x = 20
def add1(a,b):
    global x
    print("Accessing the value of global variables inside the function",x)
    y = 10
    print("The local variable y inside the ",y)
add1(10,20)
print("The value of gobal variable x outside the function",x)
print()


print("-------Changing the value of the global variable inside the function------")
x = 20
def add2(a,b):
    y = 10
    global x
    x = 30
    print("After changing the value of the global variable x using global keyword inside the function",x)
    print("The local variable y inside the ", y)
add2(10,20)
print("The value of gobal variable x outside the function",x)


print("-------Creating global variable inside the function------")
def add3(a,b):
    y = 10
    global x
    # creating the global variable x inside the function
    x = 30
    print("Global variable x inside the function",x)
    print("Local variable y inside the function",y)

add3(10,20)
print("The variable x which is created as global inside the function and its value outside the function is",x)
print()

def add4(a,b):
    y = 30
    # this give error bcz variable y is already define as local varibale inside the function.
    # if it is not defined before then can be created as global.
    # global y
    # print("The local variable which is y is now global variable by using global keyword to redefine it again",y1)
add4(40,450)
