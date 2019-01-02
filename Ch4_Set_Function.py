a=[11,54,23,76,45,87,98,23,76,45]
print("a =",a)
a_set=set([11,54,23,76,45,87,98,23,76,45])    # Duplicate values will be removed
print("a_set =",a_set)

for i in a_set:
    print(i,end=" ")    # Elements of a set cannot be accessed by index value.

"""
add() , remove() , len() ----- works in sets.
clear() removes all elements from set.
"""

a_set.add(34)
print("a_set after adding 34 =",a_set)  # adds the number at randome position

a_set.remove(23)
print("a_set after removing 2 =",a_set) # removes the number from the set

print(len(a_set))

k=45
if k in a_set:  # Searching in a set
    print(k,"Found")
else:
    print(k,"Not Found")
