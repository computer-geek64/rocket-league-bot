# Main.py
# Ashish D'Souza
# September 8th, 2018

from time import sleep
from Encryption import *
import os


def read():
    with open("/root/PycharmProjects/RocketLeague/git/rocket-league-bot/settings.txt", "r") as file:
        lines = file.readlines()
        file.close()
    lines = list(map(lambda x: decrypt(x, "Ljezzy00Ljezzy00"), lines))
    print(lines)
    return int(lines[0].strip())


while True:
    sleep(read() * 60)
    os.system("python3 Bot.py")
