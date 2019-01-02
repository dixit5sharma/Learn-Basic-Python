import json

f = open("Files\example_2.json","r")
data = json.load(f)
f.close()

print(data)
