from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import argparse

parse = argparse.ArgumentParser(description="Selenium Test Script Configuration")
parse.add_argument("--url", required=True, help="URL for testing")
parse.add_argument("--browser", required=True, help="Browser for testing")

args = parse.parse_args()

url = args.url
browser = args.browser

if browser == "chrome":
    driver = webdriver.Chrome()
elif browser == "firefox":
    driver = webdriver.Firefox()
else:
    raise ValueError("Browser não configurado corretamente!")
    
driver.get(url)

print(driver.title)

sleep(5)

driver.quit()