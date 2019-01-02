a = [ 8 , 2 , 3 , 12 , 5 , 3 , 7 , 9 ,10]
print("Input String -",a)
median=0.0
temp=0
a.sort()
print("Sorted String -",a)
a_len=len(a)
if len(a)%2==0:
    first=int(len(a)/2)
    second=int(first-1)
    median=(a[first]+a[second])/2
else:
    index=int(len(a)/2)
    median=a[index]

print("Median =",median)
