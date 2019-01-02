print("Enter first number")
a = int(input())
print("Enter second number")
b = int(input())
print("Enter third number")
c = int(input())

if a>b:
    if a>c:
        print(a,"is the largest")
    else:
        print(c, "is the largest")

else:
    if b>c:
        print(b,"is the largest")
    else:
        print(c, "is the largest")

