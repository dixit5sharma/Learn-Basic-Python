def fact(a):
    b=1
    c=2
    while(c<=a):
        b=c*b
        c+=1
    return b

def facto(a):   #Alternative Method
    p=1
    for i in range(2,a+1):
        p*=i
    return p


p=int(input("Enter number : "))

print("Factorial of",p,"=",fact(p))
print("Factorial of",p,"=",facto(p))
