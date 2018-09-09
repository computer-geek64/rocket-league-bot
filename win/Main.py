# Main.py
# Ashish D'Souza
# September 8th, 2018

from time import sleep
from Encryption import *
import os


password = ((open(os.getcwd().split("/win")[0] + "/password.txt", "r").readlines()[0].strip()) * 16)[:16]


def read():
    with open(os.getcwd().split("/win")[0] + "/settings.txt", "r") as file:
        lines = file.readlines()
        file.close()
    lines = list(map(lambda x: decrypt(x, password), lines))
    print(lines)
    return int(lines[0].strip())


while True:
    sleep(read() * 60)
    os.system("taskkill /IM chrome.exe /F")
    os.system("taskkill /IM chromedriver.exe /F")
    os.system("python Bot.py")
