print("Enter X")
x=float(input())

sum=1.0
den=1
for i in range(1,100000):
    num=(x)**(i-1)
    den=den*i
    print(den)
    div=num/den
    if div<0.0001:
        break
    sum=sum+div

print(sum)
