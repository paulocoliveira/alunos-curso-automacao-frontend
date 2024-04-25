import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')

@pytest.fixture
def driver():
    browser_choice = config.get("default", "browser")
    if browser_choice == "chrome":
        driver = webdriver.Chrome()
    elif browser_choice == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError("Browser não configurado corretamente!")
    
    url_to_be_opened = config.get("default", "url")
    driver.get(url_to_be_opened)

    yield driver

    driver.quit()

def atest_print_title(driver):
    print(driver.title)
    sleep(10)