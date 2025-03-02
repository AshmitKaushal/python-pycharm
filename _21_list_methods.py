print("--------Length Method---------")
l1 = [10,20,30,40]
print(l1)
print(len(l1))
print()

print('---------Append Method--------')
l1 = [10,20,30,40]
print("Before appending the element 90",l1)
l1.append(90)
print('After appending the element 90',l1)
print()

print('---------Insert Method--------')
l1 = [10,20,30,40]
l1.insert(0,100)
print("After inserting the element 100",l1)
print()


print('---------Pop Method-----------')
# It return the poped element
# pop method is used to delete last element of the list.
# And we also specify index in the pop method for the element to be deleted.
l1 = [10,20,30,40]
print("Before pop",l1)
l1.pop()
print("After pop",l1)
l1.pop(1)
print("After poping the First index element from the list",l1)
print()


print('----------------Index Method----------')
# Return index of the element if the element is present else raise an error if the element is not present.
l1 = [10,20,30,40,50]
print("50 is at the index of",l1.index(50))
print()


print("----------------Sort Method----------")
l1 = [9,4,2,4,1,49,48,10]
print("Before Sorting the list",l1)
l1.sort()
print("After sorting the list",l1)

# In sort method we have a parameter reverse which is bydefault false
# If it is true then the list in sorted in the decreasing order.
l1 = [9,4,2,4,1,49,48,10]
print("Before Sorting the list",l1)
l1.sort(reverse=True)
print("After sorting the list in decreasing order",l1)
print()


print("------------Count Method---------")
# Return the total occurrences of the element in the list
l1 = [10,20,10,10,20,340,50,190,190]
print("The total count of 10 in the list",l1.count(10))
print()


print('-------------CLear Method-----------')
l1 = [10,20,30,40]
# it will delete all the elements of the list.
print(l1.clear())
print("After deleting all the element of the list l1 is empty",l1)
print()

print('------------------Copy Method--------------')
# Suppose we want to copy all the element of list into another list
# so we write
l1 = [10,20,30]
m = l1
# But the problem is that m is references to l1 ,a copy is not created
# Changes done in m is reflected in l1
# so copy method is used to copy the element of the one list into another list.
m = l1.copy()
print(m)
print()


print('----------------Extend Method----------------')
# IT is used to add one list to another list from the last index.
l1 = [10,20,30]
l2 = [40,50,60]
print("Before extending the list",l1)
l1.extend(l2)
print("After extending the list",l1)