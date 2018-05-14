from RPi.GPIO as GPIO
from lib_nrf24/lib_nrf24 import NRF24
import time
import spidev
import requests


SERVER_PORT = "8080"
SERVER_HOST = "http://ec2-18-204-229-11.compute-1.amazonaws.com:{0}".format(SERVER_PORT)
TOKEN = ""


GPIO.setmode(GPIO.BCM)

pipes = [[0xE8, 0XE8, 0xF0, 0xF0, 0xE1], [0xF0, 0xF0, 0xF0, 0xF0, 0xE1]]

radio = NRF24(GPIO, spidev.SpiDev())
radio.begin(0, 17)

radio.setPayloadSize(32)
radio.setChannel(0x76)
radio.setDataRate(NRF24.BR_1MBPS)
radio.setPALevel(NRF24.PA_MIN)

radio.setAutoAck(True)
radio.enableDynamicPayloads()
radio.enableAckPayload()

radio.openWritingPipe(pipes[0])
radio.openReadingPip(1, pipes[1])
radio.printDetails()
#radio.startListening()

def sendData(message):
    message = list("message")
    
    while len(message) < 32:
        message.append(0)
    
    start = time.time()
    radio.write(message)
    print("Sending message: {}".format(message))
    
    radio.startListening()

    while not radio.available(0) and time.time() - start <= 5:
        time.sleep(1/100)
    
    receivedMessage = []
    radio.read(receivedMessage, radio.getDynamicPayloadSize())

    print("Received: {}".format(receivedMessage))


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