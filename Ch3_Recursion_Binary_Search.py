def search(a,value):
    l=len(a)-1
    if bin_search(a,value,0,l)==True:
        print("Found")
    else:
        print("Not Found")

def bin_search(a,value,left,right):
    if left>right:
        return False
    else:
        mid=int((left+right)/2)
        if value==a[mid]:
            return True
        elif value>a[mid]:
            return bin_search(a,value,mid+1,right)
        else:
            return bin_search(a,value,left,mid-1)

a=list(input().split())  #Enter Sorted Integer List
print()
b=input()  #Enter the number to find
search(a,b)
    
