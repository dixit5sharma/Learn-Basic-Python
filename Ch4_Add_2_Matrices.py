a = [ [ 3, -5, -7, 9 ],[ 13, 0, -2, 1 ],[ -9, 8, 3, -1 ] ]
b = [ [ 0, -5, 10, 8 ],[ 6, 8, 13, -4 ],[ 8, 9, -7, -1 ] ]

print("Element a =",a)
print("Element b =",b)
flag=1

ans=[]
if len(a)==len(b):
    for i in range(len(a)):
        ans.append([])
        if len(a[i])!=len(b[i]):
            flag=0
            break
        else:
            for j in range(len(a[i])):
                ans[i].append(a[i][j]+b[i][j])
else:
    flag=0

if(flag==0):
    print("Addition of Matrices not possible")

else:
    print("Addition =",ans)
