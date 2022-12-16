import json

file = open("string.json")
example = file.read()
file.close()

person = json.loads(example)

print(person["age"])