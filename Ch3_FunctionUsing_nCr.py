from Ch3_Factorial_Function import fact
def nCr(n,r):
    num=fact(n)
    den=fact(n-r)*fact(r)
    return int(num/den)

p=int(input("Enter N : "))
q=int(input("Enter R : "))

print(str(p)+"C"+str(q)+" = ",nCr(p,q))
