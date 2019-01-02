def changeformat(a):
    b=list(a.split("-"))
    c=b[1]+"-"+b[0]+"-"+b[2]
    return c

print("Enter dates in mm-dd-yy format space separated")
q=list(map(changeformat,input().split()))

print("Changed format -",q)


"""
Alternative method

def changeformat(a):
l = list(a) # Get the string in list form
l[0],l[3] = l[3],l[0] # Swap first digits of date and month
l[1],l[4] = l[4],l[1] # Swap second digits of date and month
new_date = ''.join(l) # Convert list back into string
return new_date

"""
