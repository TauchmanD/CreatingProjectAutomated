import sys
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

USERNAME = ""
PASSWORD = ""

browser = webdriver.Chrome("chromedriver.exe")
browser.get("https://github.com/new")
path = ""
folder_name = sys.argv[1]
os.mkdir(f"{path}\\{folder_name}")
input = browser.find_element_by_xpath('//*[@id="login_field"]')
input.send_keys(USERNAME)
input = browser.find_element_by_xpath('//*[@id="password"]')
input.send_keys(PASSWORD)
input = browser.find_element_by_xpath('//*[@id="login"]/div[4]/form/div/input[12]')
input.click()
input = browser.find_element_by_xpath('//*[@id="repository_name"]')
input.send_keys(folder_name)
input = browser.find_element_by_css_selector('button.first-in-line')
input.submit()