import time
import json
import paho.mqtt.client as mqtt
from database import database, saveDatabase
# from api import login, getEnvironments, getSchedulesByUUID

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

# def update_schedules():
#     token = login(database["email"], database["password"]).json()["token"]

#     while 1:
#         try:
#             environments = getEnvironments(token).json()

#             if type(environments) == type({"name": "name"}):
#                 if environments["code"] == 1:
#                     token = login(database["email"], database["password"]).json()["token"]
#                     environments = getEnvironments(token).json()

#             database["environments"] = []
#             if len(environments) > 0:
#                 for env in environments:
#                     schedule = getSchedulesByUUID(token, env["uuid"]).json()
#                     database["environments"].append({"uuid": env["uuid"], "schedule": schedule})
            
#             print("> Saved last schedules")
#             saveDatabase()
#             time.sleep(10)
#         except Exception as e:
#             print("\nConnetion Refused!\nWait 30 seconds\n")
#             time.sleep(30)