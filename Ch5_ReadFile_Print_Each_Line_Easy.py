f = open("samplefile.txt","r")

out = f.readlines() # readlines() is a list type variable. Read() is a string
print(type(out))

for i in range(len(out)):
    print(out[i].strip())   # Strip function strips white spaces from both ends.

f.close()
