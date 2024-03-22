import pytest
from selenium import webdriver
from time import sleep

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.uol.com.br")
    driver.maximize_window()
    sleep(3)
    yield driver
    driver.quit()

def test_get_title(driver):
    title = driver.title
    assert title == "UOL - Seu universo online"

