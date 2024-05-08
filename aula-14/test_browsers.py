import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

@pytest.fixture(params=["chrome", "firefox", "edge"], scope="function")
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError("Browser não configurado corretamente!")
    
    yield driver
    driver.quit()

def test_open_google(driver):
    driver.get("https://www.google.com")
    assert driver.title == "Google"
    sleep(5)

def test_open_uol(driver):
    driver.get("https://www.uol.com.br")
    assert driver.title == "UOL - Seu universo online"
    sleep(5)