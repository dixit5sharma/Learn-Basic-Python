n=int(input("Enter the number of points : "))

points=[]
print("Enter 3 decimals separated by space for each point")

for i in range(n):
    print("Coordinates for point",i+1,":",end=" ")
    x,y,z=map(float,input().split())
    p=(x,y,z)
    points.append(p)

print(points)
