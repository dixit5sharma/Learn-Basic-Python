from Ch3_Factorial_Function import fact
def nPr(n,r):
    num=fact(n)
    den=fact(n-r)
    return int(num/den)

p=int(input("Enter N : "))
q=int(input("Enter R : "))

print(str(p)+"P"+str(q)+" = ",nPr(p,q))
