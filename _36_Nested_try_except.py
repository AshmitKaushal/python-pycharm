a = int(input("Enter the first value : "))
b = int(input("Enter the second value : "))

try:
    try:
        print(a/b)
    except ZeroDivisionError as e:
        print(e)
except Exception as e:
    print(e)
