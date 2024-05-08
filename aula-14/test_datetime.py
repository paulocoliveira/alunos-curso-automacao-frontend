import pytest
import logging
import functools
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta
from time import sleep
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions

logger = logging.getLogger(__name__)

@pytest.fixture()
def driver():
    options = ChromeOptions()
    options.set_capability('goog:loggingPrefs', {'browser': 'ALL', 'driver': 'ALL'})
    service = ChromeService()
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://paulocoliveira.github.io/mypages/plugins/index.html")
    yield driver
    logs = driver.get_log("browser")
    for entry in logs:
        logger.info("Log do Navegador: %s", entry)
    driver.quit()

def log_exception(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error("Erro durante o teste: %s", e, exc_info=True)
            raise
    return wrapper

@log_exception
def test_datetime_manipulation_1(driver):
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
    sleep(3)

@log_exception
def test_datetime_manipulation_2(driver):
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
    driver.find_element(By.XPATH, "//button[text()='FINALIZAR']").click()
    sleep(3)