print("Enter a number to find its factorial")
n = int(input())

a=1
for i in range(1,n+1):
    a=a*i
print("Factorial of",n,"is",a)
