# Bot.py
# Ashish D'Souza
# September 9th, 2018

from selenium import webdriver
from time import sleep
import Git
from Encryption import *
import os


password = ((open(os.getcwd().split("win")[0] + "password.txt", "r").readlines()[0].strip()) * 16)[:16]


def read():
    with open(os.getcwd().split("win")[0] + "settings.txt", "r") as file:
        lines = file.readlines()
        file.close()
    lines = list(map(lambda x: decrypt(x, password), lines))
    delay = int(lines[0].strip())
    accounts = lines[1:]
    emails = []
    passwords = []
    for i in range(len(accounts)):
        if accounts[i][0] != "!":
            emails.append(accounts[i].strip().split(":")[0])
            passwords.append(accounts[i].strip().split(":")[1])
    return [delay, emails, passwords]

delay, emails, passwords = read()

while True:
    repository_name = os.getcwd().split("win")[0]
    Git.fetch(repository_name)
    if not Git.is_up_to_date(repository_name):
        Git.pull(repository_name)
        delay, emails, passwords = read()
    for account in range(len(emails)):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--headless")
        browser = webdriver.Chrome(chrome_options=chrome_options)
        browser.get("https://rocket-league.com")
        sleep(1)
        browser.find_element_by_id("acceptPrivacyPolicy").click()
        sleep(1)
        browser.find_element_by_name("email").send_keys(emails[account])
        browser.find_element_by_name("password").send_keys(passwords[account])
        browser.find_element_by_name("submit").click()
        sleep(1)
        username = browser.find_element_by_css_selector("a[href^=\"/trades/\"").get_attribute("href").split("/")[-1]
        browser.get("https://rocket-league.com/trades/" + username)
        sleep(1)
        trades = len(browser.find_elements_by_class_name("rlg-trade-display-container"))
        links = []
        for trade in range(trades):
            links.append(browser.find_elements_by_class_name("rlg-trade-display-container")[trade].find_element_by_css_selector("div.rlg-trade-display-header > a").get_attribute("href"))
            links[trade] = links[trade][:links[trade].index("trade/")] + "trade/edit?trade=" + links[trade].split("/")[-1]
        for trade in range(trades):
            browser.get(links[trade])
            sleep(1)
            browser.execute_script("document.getElementsByName('btnSubmit')[0].click()")
            sleep(10)
        browser.close()
    sleep(delay * 60)
