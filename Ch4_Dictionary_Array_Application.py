"""
This is a Good application of Array of Dictionary.
Key value pair are arranged and value from one transfered to another.
"""

students = {
"140101001" : [ "CS101" , "EE101" , "CS201" ],
"140102001" : [ "MA101" , "EE101" , "EE201" ],
"140103001" : [ "CS101" , "ME101" ],
"140123001" : [ "MA101" , "CS101" , "MA201" ]
}
result = {
"MA321" : [ "140101001" , "140123001" ],
"EE301" : [ "140102001" , "140103001" ],
"ME301" : [ "140103001" ]
}

for cs in result:
    for rn in result[cs]:
        students[rn].append(cs)

for k in students:
    print(k,"=",students[k])
