a=[1,2,3,4,5]
b=[6,7,8,9]
c=["Dixit","Sharma","is","Learning"]

d=a+b+c
print(d)

"""
Alternative method:-
To use extend function
"""

a.extend(b)
a.extend(c)
print(a)    # Same output
