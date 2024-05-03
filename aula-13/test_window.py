import pytest
from selenium import webdriver
from time import sleep
import os

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    sleep(3)
    yield driver
    driver.quit()

def test_open_new_tab_and_switch(driver):
    driver.get("https://www.google.com")
    original_tab = driver.current_window_handle
    driver.execute_script("window.open('https://www.uol.com.br', '_blank');")
    new_tab =None
    for tab in driver.window_handles:
        if tab != original_tab:
            new_tab = tab
            break
    driver.switch_to.window(new_tab)
    driver.switch_to.window(original_tab)

def test_close_window(driver):
    driver.get("https://www.google.com")
    original_tab = driver.current_window_handle
    driver.execute_script("window.open('https://www.uol.com.br', '_blank');")
    new_tab =None
    for tab in driver.window_handles:
        if tab != original_tab:
            new_tab = tab
            break
    driver.switch_to.window(new_tab)
    driver.close()
    driver.switch_to.window(original_tab)

def test_window_manipulation(driver):
    driver.get("https://www.google.com")
    driver.set_window_size(800, 600)
    driver.set_window_position(500, 500)

def test_screenshot(driver):
    driver.get("https://www.google.com")
    driver.save_screenshot("google_screenshot.png")
    assert os.path.exists("google_screenshot.png")
    sleep(3)