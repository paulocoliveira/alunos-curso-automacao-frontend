import locale
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://paulocoliveira.github.io/mypages/plugins/index.html")
    yield driver
    driver.quit()

def test_locale_manipulation(driver):
    driver.find_element(By.XPATH, "//button[text()='Locale']").click()

    current_locale = locale.getlocale()
    driver.find_element(By.ID, "current_locale").send_keys(str(current_locale))

    new_locale = "pt_pt.UTF-8"
    locale.setlocale(locale.LC_ALL, new_locale)
    updated_locale = locale.getlocale()
    driver.find_element(By.ID, "new_locale").send_keys(str(updated_locale))

    formatted_currency = locale.currency(123456789, symbol=True, grouping=True)
    driver.find_element(By.ID, "formatted_number").send_keys(str(formatted_currency))

    sleep(15)
