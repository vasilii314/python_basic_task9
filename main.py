import threading
import time


def countdown(interval, name):
    for x in range(10, 0, -1):
        print(f"Thread {name}: {str(x)}\n")
        time.sleep(interval)
    print(f"Thread {name}: completed")


t1 = threading.Thread(target=countdown, args=(1, "t1"))
t2 = threading.Thread(target=countdown, args=(2, "t2"))

t1.start()
t2.start()
