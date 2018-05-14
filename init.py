import time
import requests
from nrf24 import sendData

SERVER_PORT = "8080"
SERVER_HOST = "http://ec2-18-204-229-11.compute-1.amazonaws.com:{0}".format(SERVER_PORT)
TOKEN = ""

def login(email, password):
    payload = {'email': email, 'password': password}
    headers = {'content-type': 'application/json'}

    return requests.post(SERVER_HOST + '/login', data=json.dumps(payload), headers=headers)

def getStatus(token, uuid):
    headers = {'Authorization': token}

    return requests.get(SERVER_HOST + '/environment/{0}/status'.format(uuid), headers=headers)

if __name__ == "__main__":
    while True:


        time.sleep(5)