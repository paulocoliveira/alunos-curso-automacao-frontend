import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

@pytest.fixture(params=["https://www.google.com", "https://www.uol.com.br"], scope="function")
def driver(request):
    driver = webdriver.Chrome()
    driver.get(request.param)    
    yield driver
    driver.quit()

def test_open_url(driver):
    print(driver.title)