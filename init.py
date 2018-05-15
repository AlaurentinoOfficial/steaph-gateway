import time
from nrf24 import sendData
from api import login, getEnvironment

email = "alaurentino.br@gmail.com"
password = "1234567890n"
uuids = ["SEe879qdBGh2MKadjcQUjm78a"]

def loop():
    token = login(email, password)["token"]

    for uuid in uuids:
        status = getEnvironment(token, uuid)["status"]
        
        sendData("true" if status else "false")

    time.sleep(5)

if __name__ == "__main__":
    while True:
        loop()
