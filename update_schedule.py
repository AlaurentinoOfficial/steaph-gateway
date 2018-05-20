import time
import json
import paho.mqtt.client as mqtt
from database import database, saveDatabase

def on_connect(client, userdata, flags, rc):
    print("MQTT> Connected")
    client.subscribe("/steaph/things/" + database["public_key"] + "/environments", 1)

def on_message(client, userdata, msg):
    if msg.topic == "/steaph/things/" + database["public_key"] + "/environments":
        try:
            database["environments"] = json.load(msg.payload)
            saveDatabase()
            print("MQTT> Environments updated successfully!")
        except:
            print("MQTT> Invalid payload from " + msg.topic)

def update_schedules():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(database["mqtt_server"], database["mqtt_port"], 60)
    client.username_pw_set(database["mqtt_user"], database["mqtt_password"])

    client.loop_forever()