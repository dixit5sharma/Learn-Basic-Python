a = 9
b = [1,2,3]
c = '78'
d = 'qwerty'
e = {'name1': 9999999999, 'name2': 9999999999, 'name3': 9999999999}

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

if type(c)==type(d):
    print("C and D both are String")

if type(a)==int:    # This is equivalent to using isinstance(var,type) function
    print("Integer")

if type(b)==list:
    print("List")

if type(c)==str:
    print("String")

if type(d)==str:
    print("String")

if type(e)==dict:
    print("Dictionary")
