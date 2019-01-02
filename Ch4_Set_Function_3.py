rolls1 = {1,3,5,6}
rolls2 = {1,5}
rolls3 = {2,4}
print("rolls1 =",rolls1)
print("rolls2 =",rolls2)
print("rolls3 =",rolls3)

if rolls2 <= rolls1 :
    print("rolls2 is subset of rolls1")

if rolls1.isdisjoint(rolls3) :
    print("rolls1 and rolls3 disjoint sets")
