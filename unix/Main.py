# Main.py
# Ashish D'Souza
# September 9th, 2018

from time import sleep
import os


while True:
    os.system("killall chromedriver")
    os.system("killall chrome")
    os.system("python3 Bot.py")
    sleep(15 * 60)