print("Enter the Integer List")
a=list(map(int,input().split()))

b=[]
for i in a:     # Very easy method
    if i%2==0:
        b.append(i)

print(b)
