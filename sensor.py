'''
Author: www.github.com/JuanBindez
Description: loops in linux's sensors command for easy viewing
Python Version: 3.10
year: 2022
Local: Brazil
'''

import os
import time


def sensor():
    while 10 < 50:
        os.system("sensors")
        time.sleep(2)
        os.system("clear")

try:
    sensor()

except KeyboardInterrupt:
    print("você encerrou o programa")


