'''The ternary operator in Python is a shorthand way of expressing a conditional statement. Its syntax is as follows:

"result_if_true   if    condition    else    result_if_false"

result_if_true if condition else result_if_false
condition: An expression that evaluates to either True or False.
result_if_true: The value to be returned if the condition is true.
result_if_false: The value to be returned if the condition is false.
Here's a breakdown of the parts:

If the condition is true, the entire expression evaluates to result_if_true.
If the condition is false, the entire expression evaluates to result_if_false.'''

a = 10
b = 20
c = a if a>b else b
print(c,"is the greatest value")

a =10
b = 200
c = 30

res = a if a>b and a>c else b if b>c else c
print("The largest value among them is",res)


