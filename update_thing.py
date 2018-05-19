import time
import json
from datetime import datetime
from database import database
#from nrf24 import sendData

def baseTime(time):
    now = datetime.now()
    now = now.replace(hour = time.hour, minute = time.minute, microsecond = 0)

    return now

def update_things():
    while 1:
        environments = database["environments"]

        if len(environments) > 0:
            for env in environments:
                status = False

                if len(env["schedule"]) > 0:
                    for schedule in env["schedule"]:
                        start = baseTime(datetime.strptime(schedule["start"], "%Y-%m-%dT%H:%M:%S.%fZ"))
                        end = baseTime(datetime.strptime(schedule["end"], "%Y-%m-%dT%H:%M:%S.%fZ"))
                        now = datetime.utcnow()

                        if now >= start and now < end and now.isoweekday() == schedule["day"]:
                            status = True
                            break

                print("> Sended to " + env["uuid"] + " " + json.dumps({'status': status}))
                #sendData(json.dumps({'status': status}))
    
        time.sleep(5)