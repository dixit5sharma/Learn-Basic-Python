a = 9
b = [1,2,3]
c = '78'
d = 'qwerty'
e = {'name1': 9999999999, 'name2': 9999999999, 'name3': 9999999999}

if isinstance(a,int):    # This is equivalent to using type(var)==type<> function
    print("Integer")

if isinstance(b,list):
    print("List")

if isinstance(c,str):
    print("String")

if isinstance(d,str):
    print("String")

if isinstance(e,dict):
    print("Dictionary")
