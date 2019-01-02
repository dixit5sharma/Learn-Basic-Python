def search(a,value):
    l=len(a)-1
    if bin_search(a,value,0,l)>=0:
        k=bin_search(a,value,0,l)
        print("Found at position =",k+1)
    else:
        print("Not Found")

def bin_search(a,value,left,right):
    if left>right:
        return -1
    else:
        mid=int((left+right)/2)
        if value==a[mid]:
            return mid
        elif value>a[mid]:
            return bin_search(a,value,mid+1,right)
        else:
            return bin_search(a,value,left,mid-1)

a=list(map(int,input().split()))  #Enter Sorted Integer List
b=int(input())  #Enter the number to find
search(a,b)
