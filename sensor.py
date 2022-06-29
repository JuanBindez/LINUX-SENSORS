'''
Autor: www.github.com/JuanBindez
Descrição: faz um loop no comando sensors do linux para facilitar a visualização.
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


