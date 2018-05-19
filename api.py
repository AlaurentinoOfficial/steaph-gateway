import requests
import json

SERVER_PORT = "8080"
SERVER_HOST = "http://ec2-18-204-229-11.compute-1.amazonaws.com:{0}".format(SERVER_PORT)

def login(email, password):
    payload = {'email': email, 'password': password}
    headers = {'content-type': 'application/json'}
    
    return requests.post(SERVER_HOST + '/login', data=json.dumps(payload), headers=headers)

def getEnvironments(token):
    return requests.get(SERVER_HOST + '/environment', headers={'Authorization': token})

def getEnvironmentByUUID(token, uuid):
    return requests.get(SERVER_HOST + '/environment/' + uuid, headers={'Authorization': token})

def getSchedulesByUUID(token, uuid):
    return requests.get(SERVER_HOST + '/environment/' + uuid + '/schedule', headers={'Authorization': token})

if __name__ == "__main__":
    token = login("alaurentino.br@gmail.com", "1234567890n")["token"]
    environments = getEnvironments(token)

    for env in environments:
        environment = getEnvironmentByUUID(token, env["uuid"])
        print("true" if env["status"] else "false")