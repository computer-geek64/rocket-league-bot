# Main.py
# Ashish D'Souza
# September 8th, 2018

from time import sleep
from Encryption import *
import os


def read():
    with open("/root/Documents/git/rocket-league-bot/settings.txt", "r") as file:
        lines = file.readlines()
        file.close()
    lines = list(map(lambda x: decrypt(x, "Ljezzy00Ljezzy00"), lines))
    print(lines)
    return int(lines[0].strip())


delay = read()
while True:
    sleep(delay * 60)
    os.system("taskkill /IM chrome.exe /F")
    os.system("taskkill /IM chromedriver.exe /F")
    os.system("python Bot.py")
