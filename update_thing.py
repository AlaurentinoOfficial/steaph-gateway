import time
import json
from datetime import datetime
from database import database, saveDatabase
from nrf24 import EasyNRF24

# Lambda to equalify the the time paramters to now exept the hour and minute
baseTime = lambda time: datetime.now().replace(hour = time.hour, minute = time.minute, microsecond = 0)

# Lambda to convert Time ISO String to Pyhton datetime
str_2_date = lambda time: datetime.strptime(time, "%Y-%m-%dT%H:%M:%S.%fZ")

def update_things():
    radio = EasyNRF24(csn = 0, ce = 17)

    while 1:
        environments = database["environments"]

        # Verify if there is environments
        if len(environments) > 0:
            for env in environments:
                status = False

                # Pass by each schedule and analyse actul state
                if len(env["schedule"]) > 0:
                    for schedule in env["schedule"]:
                        start = baseTime(str_2_date(schedule["start"]))
                        end = baseTime(str_2_date(schedule["end"]))
                        now = datetime.utcnow()

                        # Check the schedule
                        if now >= start and now < end and now.isoweekday() == schedule["day"]:
                            status = True
                            break

                # Send the schedule by RF to End Points (Things)
                status = radio.sendData(env['address'], json.dumps({'status': status}), max_time=EasyNRF24.MAX_RECEIVE_TIME_CONNECTION)
                print("Do something with this data: " + status)

                # Try to save the response of End Point and save in Database
                try:
                    value = json.loads(status)

                    try:
                        database["environments_status"][env['address']].append(value)
                        
                    # Case the status of this env not alredy created
                    except:
                        database["environments_status"].append({env['address']: []})
                        database["environments_status"][env['address']].append(value)

                    saveDatabase()
                # Case the response can't be converted to JSON
                except:
                    pass

                time.sleep(1/2)
        time.sleep(5)