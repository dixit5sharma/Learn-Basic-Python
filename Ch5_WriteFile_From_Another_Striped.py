f = open("samplefile.txt","r")
out = f.readlines()
a=[]
for each in out:
    if each!="\n":
        a.append(each)

f.close()
n = open("newfile.txt","w")
n.writelines(a)
print("Data striped and copied to new file")
n.close()
