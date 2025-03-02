a = int(input("Enter the value : "))
b = int(input("Enter the value : "))
l1 = [10,20,30]
# In this program there are two error
# error which comes first will be handled.

try:
    print(a/b)
    print(l1[9])
except ZeroDivisionError as e:
    print(e)
except IndexError as e:
    print(e)
