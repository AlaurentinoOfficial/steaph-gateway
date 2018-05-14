import requests
import json

SERVER_PORT = "8080"
SERVER_HOST = "http://ec2-18-204-229-11.compute-1.amazonaws.com:{0}".format(SERVER_PORT)

def login(email, password):
    payload = {'email': email, 'password': password}
    headers = {'content-type': 'application/json'}
    
    return requests.post(SERVER_HOST + '/login', data=json.dumps(payload), headers=headers).json()

def getEnvironment(token, uuid):
    headers = {'Authorization': token}

    return requests.get(SERVER_HOST + '/environment/' + uuid, headers=headers).json()