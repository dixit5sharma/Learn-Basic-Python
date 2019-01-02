def cube(n):
    return n*n*n

a=[1,2,3,4,5,6,7,8]
b=map(cube,a)
c=list(b)

print("cubes of list",a,"=",c)
