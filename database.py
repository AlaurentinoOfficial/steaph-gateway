import json

filename = "database.json"

# Open the JSON File
file = open(filename, "r")
database = json.load(file)

# Save into JSON File
def saveDatabase():
    with open(filename, 'w') as f:
        json.dump(database, f)