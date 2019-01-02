a = [1]*101
print("Prime Numbers -",end=" ")

for i in range(2,101):
    if a[i]==1:
        for j in range(2*i,101,i):
            a[j]=0

for i in range(2,101):
    if a[i]==1:
        print(i,end=" ")
