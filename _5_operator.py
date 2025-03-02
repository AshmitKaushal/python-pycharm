# ArithmeticOperator
import math

print("-----------------Arithmetic Operator-------------")
a = 15
b = 7
print("The addition of  a+b is",a+b)
print("The subtraction of a-b is",a-b)
print("The multiplication of a*b is",a*b)
print("The division of a/b is",a/b)
print("The floor value of a//b is",a//b)
print("The modulus of a%b is",a%b)
print("The ceil value of a and b is",math.ceil(a/b))
print()

print("----------------Relation Operator-----------------")
a = 15
b = 7
print("The value of a>b is",a > b)
print("The value of a<b is ", a < b)
print("The value of a>=b is",a>=b)
print("The value of a<=b is",a<=b)
print("The value of a==b is",a==b)
print("The value of a!=b is",a!=b)
print()


print("--------------Assignment Operator----------------")
a = 15
print("The value of a is",a)
a +=5
print("The value of a is",a)
a *=4
print("The value of a is",a)
a //=10
print("The value of a is",a)

# Left Shift Operator
a = 10<<2
print("The value of a after left shift by 2",a)

# Right Shift Operator
a = 10>>2
print("The value of a after right shift by 2",a)


# Logical Operator
# And Operator
a = 10
b = 5

'''In Python, the and operator returns the first false operand or the last operand if both are true. 
If both operands are true, it returns the second operand.

In the case of print(10 and 5), both 10 and 5 are considered true in a boolean context. 
Therefore, the and operator returns the second operand, which is 5.

So, the output of print(10 and 5) will be 5.'''
print(a and b)

# Or operator
a = 10
b = 5
'''In the expression print(10 or 5), the or operator returns the first true operand or the last operand if none are true.
Since 10 is considered true in a boolean context, the or operator returns the first operand, which is 10'''
print(a or b)

a = 0
b = 0
c = 10
d =  a or b or c
print("The value of d is",d)

# MemberShip Operator
print("-----------------MemberShip Operator--------------------------")
# It is used to check if a value or variable is present in a sequence (list, tuple, string etc.)
l1 = ["Apple","Orange","Mango",10,20,30]
print(l1)
print("Checking whether Apple is present in the list or not answer is","Apple" in l1)
print("Is 60 is not present in the list",60 not in l1)
print()

print('-----------------------Identity Operator---------------------')
# Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
'''In Python, identity operators are used to compare the memory locations of two objects, checking if they refer to the same object. There are two identity operators: is and is not.

1)is Operator:

The is operator returns True if both operands refer to the same object (have the same memory address), and False otherwise.

2)is not Operator:

The is not operator returns True if both operands do not refer to the same object, and False if they do.'''

x = [10,20,30]
y = [10,20,30]
z = x
# It will return false as x and y are two different object
print("Is x and y are same object",x is y)

# It will return true as x and z are same object.
# As z is reference to the memory location of x
print("Is x and z are same object",x is z)
print()


print('---------------Bitwise Operator----------------------')
a = 10
b = 4

print("The binary value of a is",bin(a))
print(type(bin(a)))
print("The value of a&b is",a&b)
print("The value of a|b is",a|b)
a = 2
print("The value of ~a",~a)
print("The value of a ^ b",a^b)
