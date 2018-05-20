import threading
from update_thing import update_things
from update_schedule import update_schedules
import sys, os

def wait_key():
    result = None
    if os.name == 'nt':
        import msvcrt
        result = msvcrt.getch()
    else:
        import termios
        fd = sys.stdin.fileno()

        oldterm = termios.tcgetattr(fd)
        newattr = termios.tcgetattr(fd)
        newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
        termios.tcsetattr(fd, termios.TCSANOW, newattr)

        try:
            result = sys.stdin.read(1)
        except IOError:
            pass
        finally:
            termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)

    return result

if __name__ == "__main__":
    updateSchedules = threading.Thread(target=update_schedules)
    updateThings = threading.Thread(target=update_things)

    updateSchedules.start()
    updateThings.start()

    updateSchedules.join()
    updateThings.join()