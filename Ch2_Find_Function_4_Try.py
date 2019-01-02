#Does not work with both int and str. Depends on the element to find variable.
#Str matches str and int matches int.

n=["Dixit","Sharma","is","Learning",21,324,423]
print("Input String -", n)
print("Enter element to find")
f=input()
if f in n:
    print("Present")
else:
    print("Not Present")
