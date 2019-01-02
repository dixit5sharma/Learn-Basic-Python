print("Enter number of elements")
n=int(input())
a=[]

for i in range(n):
    print("Enter element",i)
    temp=input()
    a.append(temp)

a[2]='Sharma'
print("Input",a)
