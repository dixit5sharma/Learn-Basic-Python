print("Enter the Integer List")
a=list(map(int,input().split()))
print("Enter the completed List")
c=list(map(int,input().split()))
#   pending = [ item for item in assignments if item not in completed ]

p=[i for i in a if i not in c]

print(p)
