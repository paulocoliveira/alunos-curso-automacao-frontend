from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

#Accessing site 1
browser.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/login")

browser.maximize_window()

sleep(3)

#By ID
email = browser.find_element(By.ID, "input-email")

#By NAME
pwd = browser.find_element(By.NAME, "password")

#Accessing site 2
browser.get("https://www.lambdatest.com/selenium-playground/ajax-form-submit-demo")

browser.maximize_window()

sleep(3)

#By CLASS_NAME
browser.find_element(By.CLASS_NAME, "btn-dark")

#Accessing site 3
browser.get("https://www.lambdatest.com/selenium-playground/")

browser.maximize_window()

sleep(3)

#By LINK_TEXT
browser.find_element(By.LINK_TEXT, "Ajax Form Submit")

#By PARTIAL_LINK_TEXT
browser.find_element(By.PARTIAL_LINK_TEXT, "Codes")

#By TAG_NAME
browser.find_elements(By.TAG_NAME, "a")

title = browser.title

print(title)

browser.quit()