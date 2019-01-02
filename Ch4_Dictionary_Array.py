contacts = [
{
"name1" : 9999999999,
"name2" : 9999999999,
"name3" : 9999999999
},
{
"name4" : 9999999999,
"name2" : 9999999999
},
{
"name3" : 9999999999,
"name5" : 9999999999,
"name6" : 9999999999
}
]

for i in contacts:
    for j in i:
        print(j,"=",i[j])

        
