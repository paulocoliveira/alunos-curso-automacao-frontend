import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://paulocoliveira.github.io/mypages/validation/index.html")
    sleep(3)
    yield driver
    driver.quit()

def test_get_attribute(driver):
    title = driver.find_element(By.ID, "title")
    value = title.get_attribute("data-test")
    assert value == "testValue"

def test_is_displayed(driver):
    driver.find_element(By.ID, "toggleButton").click()
    hidden_message = driver.find_element(By.ID, "hiddenMessage")
    assert hidden_message.is_displayed()

def test_is_enabled(driver):
    input_field = driver.find_element(By.ID, "inputField")
    assert input_field.is_enabled()

def test_get_property(driver):
    checkbox = driver.find_element(By.ID, "testCheckbox")
    assert checkbox.get_property("checked") == True
    checkbox.click()
    assert checkbox.get_property("checked") == False

def test_is_selected(driver):
    checkbox = driver.find_element(By.ID, "testCheckbox")
    assert checkbox.is_selected() == True
    checkbox.click()
    assert checkbox.is_selected() == False, "Checkbox should be selected"

def test_value_of_css_property(driver):
    button = driver.find_element(By.ID, "toggleButton")
    assert button.value_of_css_property("color") == "rgba(255, 255, 255, 1)"

def test_get_size(driver):
    button = driver.find_element(By.ID, "testButton")
    size = button.size
    assert size["width"] == 2504 and size["height"] == 38, "Button size is not 2504 x 38"

def test_get_location(driver):
    button = driver.find_element(By.ID, "testButton")
    location = button.location
    assert location["x"] == 28 and location["y"] == 286, "Button location is not x = 28 and y = 286"

def test_tag_name(driver):
    button = driver.find_element(By.ID, "testButton")
    assert button.tag_name == "button"