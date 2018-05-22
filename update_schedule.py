import time
import json
import paho.mqtt.client as mqtt
from database import database, saveDatabase

# On connect with MQTT Server
def on_connect(client, userdata, flags, rc):
    print("MQTT> Connected")
    client.subscribe("/steaph/things/" + database["public_key"] + "/environments", 1)

# On subscribe some topic from MQTT Server
def on_message(client, userdata, msg):
    if msg.topic == "/steaph/things/" + database["public_key"] + "/environments":
        try:
            database["environments"] = json.loads(msg.payload)
            saveDatabase()
            print("MQTT> Environments updated successfully!")

            client.publish("/steaph/things/" + database["public_key"] + "/environments/status", payload=json.dumps(database["environments_status"]), qos=1)
        except Exception as e:
            print(e)
            print("MQTT> Invalid payload from " + msg.topic)

def update_schedules():
    # Create a new MQTT Client
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    # Put the credentials
    client.username_pw_set(database["mqtt_user"], database["mqtt_password"])
    
    # Create a connection
    client.connect(database["mqtt_server"], database["mqtt_port"], 60)

    # And ever update the subscriptions
    client.loop_forever()