import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta
from time import sleep
import json
import os

def load_data():
    with open("environment.json") as jsonfile:
        return json.load(jsonfile)
    
@pytest.fixture(params=load_data(), scope="function")
def driver(request):
    env = request.param
    plataform = env["platform"]
    browser = env["browser"]

    if browser == "Chrome":
        web_driver = webdriver.ChromeOptions()
    elif browser == "Firefox":
        web_driver = webdriver.FirefoxOptions()
    elif browser == "MicrosoftEdge":
        web_driver = webdriver.EdgeOptions()
    elif browser == "Safari":
        web_driver = webdriver.SafariOptions()

    username = os.getenv("LT_USERNAME")
    accessToken = os.getenv("LT_KEY")
    gridUrl = "hub.lambdatest.com/wd/hub"

    lt_options = {
        "user": username,
        "accessKey": accessToken,
        "build": "Versão 1.0",
        "name": "Cross-browser testing",
        "platformName": plataform,
        "browserName": browser,
        "browserVersion": "latest",
        "selenium_version": "latest",
        "w3c": True,
        "visual": True
    }

    options = web_driver
    options.set_capability("LT:Options", lt_options)

    url = "https://" + username + ":" + accessToken + "@" + gridUrl

    driver = webdriver.Remote(
        command_executor=url,
        options=options
    )

    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://paulocoliveira.github.io/mypages/plugins/index.html")
    yield driver

    #checa o resultado do teste que foi executado 
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        driver.execute_script("lambda-status=failed")
    else:
        driver.execute_script("lambda-status=passed")

    driver.quit()

def test_datetime_manipulation1(driver):
    driver.find_element(By.XPATH, "//button[text()='DateTime']").click()
    current_time = datetime.now()
    driver.find_element(By.ID, "current_time").send_keys(str(current_time))
    formatted_1 = current_time.strftime('%d-%m-%y')
    driver.find_element(By.ID, "formatted_date1").send_keys(formatted_1)
    formatted_2 = current_time.strftime('%Y-%m-%d %H:%M:%S')
    driver.find_element(By.ID, "formatted_date2").send_keys(formatted_2)
    date_60 = current_time + timedelta(days=60)
    driver.find_element(By.ID, "date_in_60_days").send_keys(date_60.strftime('%d-%m-%y'))
    in_2099 = current_time.replace(year=2099)
    driver.find_element(By.ID, "year_2099").send_keys(in_2099.strftime('%d-%m-%Y'))
    driver.find_element(By.XPATH, "//button[text()='CONCLUIR']").click()
    sleep(1)

def test_datetime_manipulation2(driver):
    driver.find_element(By.XPATH, "//button[text()='DateTime']").click()
    current_time = datetime.now()
    driver.find_element(By.ID, "current_time").send_keys(str(current_time))
    formatted_1 = current_time.strftime('%d-%m-%y')
    driver.find_element(By.ID, "formatted_date1").send_keys(formatted_1)
    formatted_2 = current_time.strftime('%Y-%m-%d %H:%M:%S')
    driver.find_element(By.ID, "formatted_date2").send_keys(formatted_2)
    date_60 = current_time + timedelta(days=60)
    driver.find_element(By.ID, "date_in_60_days").send_keys(date_60.strftime('%d-%m-%y'))
    in_2099 = current_time.replace(year=2099)
    driver.find_element(By.ID, "year_2099").send_keys(in_2099.strftime('%d-%m-%Y'))
    driver.find_element(By.XPATH, "//button[text()='CONCLUIR']").click()
    sleep(1)

    
