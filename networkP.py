import json

file = open("./network.json")
readfile = file.read()
file.close()

parsedJson = json.loads(readfile)

devices = parsedJson["device"]
interfaces = parsedJson["interfaces"]


#for item in interfaces[0]:
#    print(item, interfaces[0][item])

for item in interfaces:
    
    for var in item:
        print(var, item[var])
    
    print("-----")

