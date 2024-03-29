import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://paulocoliveira.github.io/mypages/waits/index.html")
    yield driver
    driver.quit()

def test_implicity_wait(driver):
    driver.find_element(By.XPATH, "//section[@id='conditional-element-section']/button").click()
    driver.find_element(By.ID, "hidden-button").click()
    sleep(8)