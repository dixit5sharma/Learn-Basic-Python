def rec_sum(a,pos):
    if len(a)==pos:
        return 0
    else:
        return int(a[pos]+rec_sum[pos+1])

print("Enter a list of integers")
m=list(map(int,input().split()))
print(m)
print("Enter position, where to start from")
n=int(input())
print("Sum of numbers from",n,"=",int(rec_sum(m,n)))
