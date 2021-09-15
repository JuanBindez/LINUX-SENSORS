#python3 sensor.py

import os
import time


def sensor():
    while 10 < 50:
        os.system("sensors")
        time.sleep(2)
        os.system("clear")

sensor()


