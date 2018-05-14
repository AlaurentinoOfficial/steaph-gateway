import time
from nrf24 import sendData
from api import login, getEnvironment

uuids = ["SEe879qdBGh2MKadjcQUjm78a"]

def loop():
    token = login("alaurentino.br@gmail.com", "1234567890n")["token"]

    for uuid in uuids:
        status = getEnvironment(token, uuid)["status"]
        sendData("{status: " + status["status"] + "}")

    time.sleep(5)

if __name__ == "__main__":
    while True:
        loop()