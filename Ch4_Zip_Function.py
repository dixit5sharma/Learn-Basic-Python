a=list(map(int,input("Enter list of number to be entered in a list separated by space: ").split()))
b=list(map(int,input("Enter same number of another list of number to be entered in a list separated by space: ").split()))

c=list(zip(a,b))
print("Zip of both list -",c)   # zip function is used like map
