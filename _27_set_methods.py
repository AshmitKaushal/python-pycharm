# Set Methods
s1 = {10,20,30,40,50}
print(s1)
print(type(s1))

print('------------Union Method-------------')
# THis will return the new set which conatins all the elements of both the sets.
s1 = {10,20,30,40,50}
s2 = {50,60,70,80}
print(s1.union(s2))

print('-----------Intersection Method----------')
# THis will return the new set which conatins common elements from both the sets.
s1 = {10,20,30,40,50}
s2 = {50,60,70,80}
print(s1.intersection(s2))

print('------------Update Method----------')
# This will not return the new set the changes will be done in the original set with which the method is called.
# all the elements of both the set are sets into original set.
s1 = {10,20,30,40,50}
s2 = {50,60,70,80}
s1.update(s2)
print(s1)

print("-----------IntersectionUpdate Method-----------")
# This will not return the new set the changes will be done in the original set with which the method is called.
# comman elements from both the set are sets into original set.
s1 = {10,20,30,40,50}
s2 = {50,60,70,80}
s1.intersection_update(s2)
print(s1)


print('---------------Difference Method---------------')
# Difference method return the elements which are only present in the set with which the method is called not present in another in set
s1 = {10,20,30,40,50}
s2 = {50,60,70,80,90}
s3 = s1.difference(s2)
print(s3)

print("---------------------Difference Update----------------------")
# The difference_update method updates the current set with items that are only present in the original set and not in both the set
s1 = {10,20,30,40}
s2 = {40,50,60,60}
s1.difference_update(s2)
print(s1)

print('----------------Symmetric Difference------------')
# return the new set which contains the non comman elements from both the set.
s1 = {10,20,30,40}
s2 = {30,40,50,60}
s3 = s1.symmetric_difference(s2)
print(s3)


print('------------------isdisjoint Method---------------')
# The isdisjoint method checks if items of given set are present in another set.
# This method returns False if items are present else it will print True.
s1 = {10,20,30,40}
s2 = {40,50,60,70}
s3 = s1.isdisjoint(s2)
print("As 40 is present is both the set so it will return false",s3)

print('-------------------issubset Method------------------')
# This method return true if one or more than one element of the set in present into another set.
s1 = {10,20,30,40}
s2 = {30,40}
print(s2.issubset(s1))

print('-------------------issuperset Method------------------')
# issuperset method is used to check if all the items of a particular set are present in the original set.
# It returns True if all the items are present else it will return false.
s1 = {10,20,30,40}
s2 = {30,40}
print(s1.issuperset(s2))

print('------------------Add Method--------------------------')
# it is used to add the element in the set
s1 = {10,20,30,40}
print("Before adding 100 in the set s1 the set s1 is",s1)
s1.add(100)
print("After adding 100 in the set s1 now the set s1 is",s1)


print('---------------Discard Method----------------------')
# It is used to delete the element from the set
s1 = {10,20,30,40}
s1.discard(10)
print("After deleting the 10 from the set s1",s1)


print("-----------------Remove Method-------------------")
# It is used to delete the element from the set
# If the element is not present then it will raise an error
s1 = {10,20,30,4,90}
s1.remove(30)
print("After deleting the 30 from the set s1",s1)

print('---------------Pop method--------------')
# It is used to remove last element from the set
# But the problem is that we dont know which is the last element of the set
print(s1.pop())

print("-----------------------Clear Method----------------")
# Deletes all the elements of the set.
s1 ={19,10,20,30}
s1.clear()
print("Now the set s1 is empty",s1)


print('-------------------------Del keyword--------------')
# It is used to delete the set itself.
s1 = {10,20,30,40}
del(s1)