print("Enter first number")
a=int(input())
print("Enter second number")
b=int(input())
print("Enter a symbol")
c=input()

if c=='*':
    print(a*b)
elif c=='+':
    print(a+b)
elif c=='-':
    print(a-b)
elif c=='/':
    print(a/b)
elif c=='**':
    print(a**b)
elif c=='%':
    print(a%b)
else:
    print("Invalid Symbol")
