print("Enter X")
x=float(input())

sum=1.0
den=1
div=1
i=1
while div>0.00001:
    num=(x)**(i-1)
    den=den*i
    div=num/den
    sum=sum+div
    i+=1

print(sum)
