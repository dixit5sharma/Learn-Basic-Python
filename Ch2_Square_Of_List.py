print("Enter number of elements")
n=int(input())
a=[]
a_square=[]

for i in range(n):
    print("Enter number",i)
    temp=int(input())
    a.append(temp)
    a_square.append(temp**2)

print("Input",a)
print("Output",a_square)
