# while loop is similar to for loop
# It is know as entry control loop
# bcz first the condition is checked then entered in the loop.


i = 1
while(i<=10):
    print(i,end=' ')
    i = i + 1
print()

print(4 in range(10))
print(15 in range(18))


# In python else is not only used with if
# But it can also be used with while and for loop
# The else statment that is used for and while will be excuted only if we exited from the loop without using the break statement

for i in range(10):
    print(i,end=' ')
else:
    print("Out of loop now")

i = 1
while(i<=10):
    if i==5:
        break
    print(i,end=' ')
    i = i + 1
else:
    print("No")
print()
print("THe else statement above is not executed bcz we exited from the loop using break statement")