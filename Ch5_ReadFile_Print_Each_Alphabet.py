file = open("samplefile.txt","r")
out = file.read()
file.close()

for s in out:
    print(s)    # prints each alphabet by alphabet
