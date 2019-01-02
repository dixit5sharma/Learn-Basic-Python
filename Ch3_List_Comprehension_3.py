print("Enter the Integer List")
a=list(map(int,input().split()))

#   new_list = [ expression(item) for item in old_list if condition(item) ]

b=[i for i in a if i%2==0]

print(b)
