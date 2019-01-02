f = open("samplefile.txt","r")
out = f.read()
f.close()

n = open("newfile.txt","w")
n.write(out)
n.close()
print("File copied from one to another successfully")
