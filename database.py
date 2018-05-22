import json

filename = "database.json"

file = open(filename, "r")
database = json.load(file)

def saveDatabase():
    with open(filename, 'w') as f:
        json.dump(database, f)

if __name__ == "__main__":
    string = "ja"
    try:
        database["environments_status"][string]
    except:
        database["environments_status"].append({string: {"hey": "true"}})
    
    saveDatabase()