# Certainly! The match statement is a feature introduced in Python 3.10 as part of Pattern Matching. It provides a more concise and expressive way to perform structured pattern matching on values. The match statement allows you to match patterns against a value and execute code based on the matched pattern.

# Here's a basic overview of the match statement:

# Basic Syntax:
# python
# Copy code
# match value:
#     case pattern_1:
#         # Code to execute if the value matches pattern_1
#     case pattern_2:
#         # Code to execute if the value matches pattern_2
#     case _:
#         # Code to execute if none of the above patterns match

# In Match case we dont need to write the break statement after each case.
# if the pattern or the case is matched then the code inside the case will be executed and will be exited

# In python we can write multiple defaults cases in a single match case.
# And we can use if in default cases also


day = input("Enter a day ")

match day:
    case 'Sun':
        print("Holiday")
    case 'Mon':
        print("Work")
    case 'Tue':
        print("Work")
    case 'Wed':
        print("Work")
    case 'Thur':
        print("Work")
    case 'Fri':
        print("Work")
    case _:
        print("Holiday")



x = 42

match x:
    case n if n > 0:
        print("x is a positive number")
    case n if n < 0:
        print("x is a negative number")
    case _:
        print("x is zero")


t1 = ("Alice",30)
print(t1,type(t1))

match t1:
    case (name,age):
        print(name,age)

    case (name,age):
        print("F",name,age)


x= 15
match x:
    case 15 if (x%2==0 and x%3==0):
        print("Divisible by both")
    case _:
        print("Oh!!!")



num = 3

match num:
    case 0:
        print("Zero")
    case 1|2:
        print('Small Positive')
    case 3|4|5|6|7:
        print("Mid Positive")
    case 8|9:
        print("larger Positive")
    case _ if num<0:
        print("Negative Number")
    case _:
        print("Very large number")