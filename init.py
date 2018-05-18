import time
from nrf24 import sendData
from api import login, getEnvironments, getEnvironmentByUUID

email = "alaurentino.br@gmail.com"
password = "1234567890n"
uuids = ["SEe879qdBGh2MKadjcQUjm78a"]

def loop():
    token = login("alaurentino.br@gmail.com", "1234567890n")["token"]
    environments = getEnvironments(token)

    for env in environments:
        sendData("true" if env["status"] else "false")

    time.sleep(5)

if __name__ == "__main__":
    while True:
        loop()
