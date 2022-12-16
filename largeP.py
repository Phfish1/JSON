import json

file = open("large.json")
readfile = file.read()
file.close()

# pasring json file
pasredJson = json.loads(readfile)

# Opening "people" inside json file
people = pasredJson["people"]

print(f"JSON: {pasredJson}")
print("------------------------------------------------------------------")
print(f"People: {people}")

print("Person0:", people[0]["name"], people[0]["age"] )
print("Person1:", people[1]["name"], people[1]["age"] )
print("Person2:", people[2]["name"], people[2]["age"] )
print("---------")


### Looping every array in json "people" 
arrayLoopCount = 0
for array in people:
    print(array)
    print("---------") # Using LoopCount to get all names ages ++ from people array
    print(people[arrayLoopCount]["name"], people[arrayLoopCount]["age"] )
    print("---------")
    arrayLoopCount += 1

print("#", pasredJson["etternavn"])
print("#", pasredJson["date"])