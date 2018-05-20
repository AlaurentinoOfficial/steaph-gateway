import time
from database import database, saveDatabase
from api import login, getEnvironments, getSchedulesByUUID

def update_schedules():
    token = login(database["email"], database["password"]).json()["token"]

    while 1:
        try:
            environments = getEnvironments(token).json()

            if type(environments) == type({"name": "name"}):
                if environments["code"] == 1:
                    token = login(database["email"], database["password"]).json()["token"]
                    environments = getEnvironments(token).json()

            database["environments"] = []
            if len(environments) > 0:
                for env in environments:
                    schedule = getSchedulesByUUID(token, env["uuid"]).json()
                    database["environments"].append({"uuid": env["uuid"], "schedule": schedule})
            
            print("> Saved last schedules")
            saveDatabase()
            time.sleep(10)
        except Exception as e:
            print("\nConnetion Refused!\nWait 30 seconds\n")
            time.sleep(30)