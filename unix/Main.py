# Main.py
# Ashish D'Souza
# September 9th, 2018

from time import sleep
import os


while True:
    sleep(15 * 60)
    os.system("killall chromedriver")
    os.system("killall chrome")
    os.system("python3 Bot.py")
