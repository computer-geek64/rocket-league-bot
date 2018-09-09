# Main.py
# Ashish D'Souza
# September 9th, 2018

from time import sleep
import os


while True:
    sleep(15 * 60)
    os.system("taskkill /IM chrome.exe /F")
    os.system("taskkill /IM chromedriver.exe /F")
    os.system("python Bot.py")
