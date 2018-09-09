# Main.py
# Ashish D'Souza
# September 8th, 2018

from time import sleep
from Encryption import *
import os


password = ((open(os.getcwd().split("/unix")[0] + "/password.txt", "r").readlines()[0].strip()) * 16)[:16]


def read():
    with open("/root/PycharmProjects/RocketLeague/git/rocket-league-bot/settings.txt", "r") as file:
        lines = file.readlines()
        file.close()
    lines = list(map(lambda x: decrypt(x, password), lines))
    print(lines)
    return int(lines[0].strip())


while True:
    sleep(read() * 60)
    os.system("python3 Bot.py")
