f = open("samplefile.txt","r")

for i in range(5):
    this = f.readline() # readline() function also gives string output, like read(). Only readlines gives list output.
    print(this)

f.close()
