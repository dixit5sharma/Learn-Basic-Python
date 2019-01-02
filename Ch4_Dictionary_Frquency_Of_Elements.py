a=list(map(str,input("Enter strings separated by space - ").split()))

d={}    # Best Usage of Dictionary in finding frequency. Very efficient.
for i in a:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1

print(d)
