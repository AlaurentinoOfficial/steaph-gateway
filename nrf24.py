import time, spidev
import RPi.GPIO as GPIO
from lib_nrf24 import NRF24

class EasyNRF24:
    MAX_RECEIVE_TIME_CONNECTION = 5

    def __init__(csn=0, ce=17, debug=False):
        # RPi configs
        GPIO.setwarmings(False)
        GPIO.setmode(GPIO.BCM)

        # Radio setup
        radio = NRF24(GPIO, spidev.SpiDev())
        radio.begin(csn, ce)

        # Set the data stream configs
        radio.serPayloadSize(32)
        radio.setChannel(0x76)
        radio.setDataRate(NRF24.BR_2MBPS)
        radio.setPALevel(NRF24.PA_MAX)

        # Use dynamic payloads and use Ack
        radio.setAutoAck(True)
        radio.enableDynamicPayloads()
        radio.enableAckPayload()

        if debug:
            radio.printDetails()

    def sendData(address, payload, max_time=EasyNRF24.MAX_RECEIVE_TIME_CONNECTION):
        # Configure the connection
        radio.openReadingPipe(1, address)
        radio.openWritingPipe(address)

        # Convert in valid payload
        payload = list(payload)
        while len(payload) < 32:
            payload.append(0)

        # Send the converted payload
        print('NRF24> Sending to ' + address)
        radio.write(payload)


        # Start to receive
        radio.startListening()
        start = time.time()

        # Wait by connection
        while not radio.available():
            time.sleep(1/100)

            if time.time() - start > max_time:
                print("NRF24> Receive connection time out!")
                return ""
        
        print("NRF24> Message received from " + address)
        
        # Read the received message
        received_msg = []
        radio.read(received_msg, radio.getDynamicPayloadSize())

        # Convert bytes to string
        translated = ""
        for n in received_msg:
            if n >= 32 and n <= 126:
                string += chr(n)

        # Stop to receive
        radio.stopListening()

        return translated