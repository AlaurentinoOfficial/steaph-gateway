import time
from nrf24 import sendData
from requests import Login, GetStatus

SERVER_PORT = "8080"
SERVER_HOST = "http://ec2-18-204-229-11.compute-1.amazonaws.com:{0}".format(SERVER_PORT)
TOKEN = ""

uuids = ["SEe879qdBGh2MKadjcQUjm78a"]

login = Login("alaurentino.br@gmail.com", "1234567890n")
TOKEN = login["token"]

def loop():
    for uuid in uuids:
        status = GetStatus(token, uuid)

        sendData("{status: " + status["status"] + "}")

    time.sleep(5)

if __name__ == "__main__":
    while True:
        loop()