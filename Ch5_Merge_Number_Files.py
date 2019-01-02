f1 = open("Files/list1.txt","r")
f2 = open("Files/list2.txt","r")
f3 = open("Files/list3.txt","r")
Rs = open("Files/Result.txt","w")

out1 = f1.readlines()
out2 = f2.readlines()
out3 = f3.readlines()
# My try method :-
"""
temp=[]
for k in out1,out2,out3:    # New Find. 1 variable can iterate through many lists in a single for loop.
    for each in k:      # KEY POINT - k is a array of 3 elements each containing sub array of value of each output (out1, out2 and out3)
        if each!="\n":  # Each will be the value of each of the sub array in out1, out2 and out3
            temp.append(each)
"""
# PDF Method (Single line better code for merging strings but not for integer sorting) :-

initial = out1 + out2 + out3
temp=[]
for each in initial:
    if each!="\n":
        temp.append(each)

# Rest of the code

final=list(map(int,temp)) # Learning. Value of readlines is always list (string list). convertion to int always needed.
final.sort()
print(final)
print("Data sorted and stored in Result.txt")
l = [ str(x)+"\n" for x in final ]
Rs.writelines(l)

f1.close()
f2.close()
f3.close()
Rs.close()
