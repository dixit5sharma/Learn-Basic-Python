f = open("samplefile.txt","r")

out = f.read()
print(type(out))    # read() function gives string output
eachline = out.split("\n")

for i in range(len(eachline)):
    if eachline[i]!="":
        print(eachline[i])
