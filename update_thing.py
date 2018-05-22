import time
import json
from datetime import datetime
from database import database
from nrf24 import EasyNRF24

baseTime = lambda time: datetime.now().replace(hour = time.hour, minute = time.minute, microsecond = 0)
str_2_date = lambda time: datetime.strptime(time, "%Y-%m-%dT%H:%M:%S.%fZ")

def update_things():
    radio = EasyNRF24(csn = 0, ce = 17)

    while 1:
        environments = database["environments"]

        if len(environments) > 0:
            for env in environments:
                status = False

                if len(env["schedule"]) > 0:
                    for schedule in env["schedule"]:
                        start = baseTime(str_2_date(schedule["start"]))
                        end = baseTime(str_2_date(schedule["end"]))
                        now = datetime.utcnow()

                        if now >= start and now < end and now.isoweekday() == schedule["day"]:
                            status = True
                            break

                status = radio.sendData(env['address'], json.dumps({'status': status}), max_time=EasyNRF24.MAX_RECEIVE_TIME_CONNECTION)
                print("Do something with this data: " + status)
        time.sleep(5)