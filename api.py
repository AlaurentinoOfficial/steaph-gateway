import requests
import json

SERVER_PORT = "8080"
SERVER_HOST = "http://ec2-18-204-229-11.compute-1.amazonaws.com:{0}".format(SERVER_PORT)

def login(email, password):
    payload = {'email': email, 'password': password}
    headers = {'content-type': 'application/json'}
    
    return requests.post(SERVER_HOST + '/login', data=json.dumps(payload), headers=headers).json()

def getEnvironments(token):
    headers = {'Authorization': token}

    return requests.get(SERVER_HOST + '/environment', headers=headers).json()

def getEnvironmentByUUID(token, uuid):
    headers = {'Authorization': token}

    return requests.get(SERVER_HOST + '/environment/' + uuid, headers=headers).json()

if __name__ == "__main__":
    token = login("alaurentino.br@gmail.com", "1234567890n")["token"]
    environments = getEnvironments(token)

    for env in environments:
        print("true" if env["status"] else "false")