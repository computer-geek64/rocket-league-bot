# Main.py
# Ashish D'Souza
# September 9th, 2018

from time import sleep
import os


while True:
    print("[-] Resetting")
    sleep(15 * 60)
    print("[+] Successfully reset.")
    print("[+] Running bot...")
    os.system("taskkill /IM chrome.exe /F")
    os.system("taskkill /IM chromedriver.exe /F")
    os.system("python Bot.py")
    print("[!] An error occurred.")
