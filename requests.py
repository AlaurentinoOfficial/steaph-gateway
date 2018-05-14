import requests

def Login(email, password):
    payload = {'email': email, 'password': password}
    headers = {'content-type': 'application/json'}

    return requests.post(SERVER_HOST + '/login', data=json.dumps(payload), headers=headers).json()

def GetStatus(token, uuid):
    headers = {'Authorization': token}

    return requests.get(SERVER_HOST + '/environment/{0}/status'.format(uuid), headers=headers).json()