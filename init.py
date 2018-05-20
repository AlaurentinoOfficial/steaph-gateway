import threading
from update_thing import update_things
from update_schedule import update_schedules

if __name__ == "__main__":
    updateSchedules = threading.Thread(target=update_schedules)
    updateThings = threading.Thread(target=update_things)

    updateSchedules.start()
    updateThings.start()

    updateSchedules.join()
    updateThings.join()