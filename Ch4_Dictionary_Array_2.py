contacts = {
"school" : {
"name1" : 9999999999,
"name2" : 9999999999,
"name3" : 9999999999
},
"college" : {
"name4" : 9999999999,
"name2" : 9999999999
},
"work" : {
"name3" : 9999999999,
"name5" : 9999999999,
"name6" : 9999999999
}
}

for k in contacts:
    print(k,"=",contacts[k])
    for i in contacts[k]:
        print(i,"=",contacts[k][i])
