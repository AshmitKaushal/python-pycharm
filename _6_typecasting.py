# Typecastring is a way of converting one datatype into another one
a = int("123")
print(a)
print(type(a))

# This is ordinal value same as ASCII Value
# In ord function we can pass only string.
a = ord('a')
print(a)
print(type(a))

b = float("123")
print(b)
print(type(b))

c = int(True)
print(c)
print(type(c))

d = int(False)
print(d)
print(type(d))

e = float(True)
print(e)
print(type(e))

f = float(False)
print(f)
print(type(f))

g = complex(False)
print(g)

i = True+False+True
print(i)

l1 = [10,20,30,40]
print("The summation of all the values of the l1 is",sum(l1))

res = "1"+str(False)
print(res)

res = 5+6J+int(True)
print(res)

