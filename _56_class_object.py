class Test:
    # Here a and b are the class variable as they are defined in the class definition.
    a=10
    b=20

# Here the t1 and t2 are the instance of the class Test
t1 = Test()
t2 = Test()


# Here both the both the object t1 and t2 are creating the new instance variable 'a'
# outshadowing the class variable 'a'.
t1.a = t1.a+1
t2.a = t2.a-1


print(Test.a) #---> Class variable a
print(t1.a)   #---> instance variable a
print(t2.a)    #---> instance variable a
