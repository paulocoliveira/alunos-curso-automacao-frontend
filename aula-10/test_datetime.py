import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta
from time import sleep

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://paulocoliveira.github.io/mypages/plugins/index.html")
    yield driver
    driver.quit()

def test_datetime_manipulation(driver):
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
    sleep(5)

    
