a=list(map(int,input("Enter list of number to be entered in a list separated by space: ").split()))
b=list(map(int,input("Enter different number of another list of number to be entered in a list separated by space: ").split()))
c=list(map(int,input("Enter different number of another list of number to be entered in a list separated by space: ").split()))

d=list(zip(a,b,c))
print("Zip of both list -",d)   # shortest number of list is taken. Rest are ignored.
