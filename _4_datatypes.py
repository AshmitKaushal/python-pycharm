# Datatype specify the type of the data that variable holds
# In python numeric data type contains --> int,float,complex
a = 10
b = 78.90
c = 5+9J
d = True
e = "john"
f = complex(4,5)

# complex is used to create the complex object
# in which first parameter represent real part and second parameter represent imaginary part
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

print('Data type of the variables')
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))


l1 = [10,20,30]
print(l1)
print(type(l1))


t1 = (10,20,30)
print(t1)
print(type(t1))

s1 = {10,20,30}
print(s1)
print(type(s1))
# To create empty set we have to use set function bcz both set and dictionary are created using {}
# So bydefault it is treated as a dictionary
s2 = set()
print(type(s2))

d1 = {}
print(d1)
print(type(d1))