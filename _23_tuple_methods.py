# As the tuple is immutable so there are only few methods of the tuple.
t1 = (10,20,30,40)
print(t1)
print(len(t1))

t1 = (10,20,30,40)
print(t1.count(10))

t1 = (10,20,30,40,50)
print(t1.index(10))

# Tuple concatenation
t1 = (1,2,3,4)
t2 = (5,6,7,8)
t3 = t1 + t2
print(t3)

# Tuple multiplication
t1 = (1,2,3,4)
t1 = t1*1
print(t1)
