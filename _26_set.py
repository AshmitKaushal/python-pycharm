# Set is unordered collection of similar or different data type.
# Set is mutable means that once the set is created it can be changed.
# By unordered means that we cann't access the elements of the set using indexs and set does not support indexing
# And ever time we print the set the elements of the set is printed in different order.
#  set is created using curly brackets.
# Set does contains the duplicate elements

s1 = {10,20,30,40,50,10}
print(s1)
print(type(s1))

# to create the set with single element we use set function
# bcz both set and dictionary is created using curly brackets
# and bydefault it is considered as a dictionary so we use set to indicate that it is set with 0 element
# and then use the add function to add the elements to it.

s2 = set()
print(s2)
print(type(s2))
s2.add(10)
s2.add(20)
print("Now the elements in the set s2 is",s2)