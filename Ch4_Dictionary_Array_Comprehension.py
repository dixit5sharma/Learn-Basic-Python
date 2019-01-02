data = [
{
"name" : "name1",
"year" : 1,
"cpi" : 8.5,
"dept" : "ECE"
},
{
"name" : "name2",
"year" : 2,
"cpi" : 8.2,
"dept" : "MNC"
},
{
"name" : "name2",
"year" : 3,
"cpi" : 8.1,
"dept" : "CSE"
}
]

print(data)
d = [x["name"] for x in data]   # Putting square bracket makes it a list of string
print(d)    # ['name1', 'name2', 'name2']

for i in data:  # Alternative method
    print(i["name"])

"""
Output of last print command - 
name1
name2
name2
"""
