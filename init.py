import threading
from update_thing import update_things
from update_schedule import update_schedules

if __name__ == "__main__":
    # Create some threads
    updateSchedules = threading.Thread(target=update_schedules)
    updateThings = threading.Thread(target=update_things)

    # Start these threads
    updateSchedules.start()
    updateThings.start()

    # Join in these threads
    updateSchedules.join()
    updateThings.join()