import time, spidev
import RPi.GPIO as GPIO
from lib_nrf24 import NRF24

class EasyNRF24:
    MAX_RECEIVE_TIME_CONNECTION = 5

    def __init__(self, csn=0, ce=17, debug=False):
        # RPi configs
        GPIO.setwarmings(False)
        GPIO.setmode(GPIO.BCM)

        # Radio setup
        self.radio = NRF24(GPIO, spidev.SpiDev())
        self.radio.begin(csn, ce)

        # Set the data stream configs
        self.radio.serPayloadSize(32)
        self.radio.setChannel(0x76)
        self.radio.setDataRate(NRF24.BR_2MBPS)
        self.radio.setPALevel(NRF24.PA_MAX)

        # Use dynamic payloads and use Ack
        self.radio.setAutoAck(True)
        self.radio.enableDynamicPayloads()
        self.radio.enableAckPayload()

        if debug:
            self.radio.printDetails()

    def sendData(self, address, payload, max_time=EasyNRF24.MAX_RECEIVE_TIME_CONNECTION):
        # Configure the connection
        self.radio.openReadingPipe(1, address)
        self.radio.openWritingPipe(address)

        # Convert in valid payload
        payload = list(payload)
        while len(payload) < 32:
            payload.append(0)

        # Send the converted payload
        print('NRF24> Sending to ' + address)
        self.radio.write(payload)


        # Start to receive
        self.radio.startListening()
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
        self.radio.read(received_msg, radio.getDynamicPayloadSize())

        # Convert bytes to string
        translated = ""
        for n in received_msg:
            if n >= 32 and n <= 126:
                string += chr(n)

        # Stop to receive
        self.radio.stopListening()

        return translated
