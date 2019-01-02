a=[0,1,2,3,4,5,6,7,8,9]
b="This is a sentence"

p=a[2:6]    # a[start:end]   start index is inclusive, end index is exclusive.
q=b[3:15]

print(p)    # [2, 3, 4, 5]
print(q)    # s is a sente

# Increasing the Jump value

c=a[2:7:2]
d=b[3:15:3]

print(c)    # [2, 4, 6]
print(d)    # ss n

# Start index not required if want to start from the beginnning.
#Similarly for the end index

c = a[:6]
d = b[3:]

print(c)    # [0, 1, 2, 3, 4, 5]
print(d)    # s is a sentence

#Reverse Order

c = a[::-1]
d = b[:3:-3]

print(c)    # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]    # If Jump is negative, reverse
print(d)    # eeeai
