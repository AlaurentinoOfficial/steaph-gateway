import json

filename = "database.json"

file = open(filename, "r")
database = json.load(file)

def saveDatabase():
    with open(filename, 'w') as f:
        json.dump(database, f)