import json

file = open("array.json")
readfile = file.read()
file.close()

parsedJson = json.loads(readfile)

person0 = parsedJson[0]
person1 = parsedJson[1]["name"]

print(person0)
print(person1)
