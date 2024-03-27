import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    sleep(3)
    yield driver
    driver.quit()

def test_mandatory_scenario(driver):
    username = driver.find_element(By.NAME, "user-name")
    username.send_keys("standard_user")

    password = driver.find_element(By.NAME, "password")
    password.send_keys("secret_sauce")

    button = driver.find_element(By.ID, "login-button")
    button.click()

    products = driver.find_elements(By.XPATH, "//button[contains(@data-test, 'add-to-cart-')]")
   
    for product in products:
        product.click()
    
    badge = driver.find_element(By.CSS_SELECTOR, ".shopping_cart_badge").text
    assert badge == "6"

    cart = driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link")
    cart.click()

    product_to_remove = driver.find_element(By.ID, "remove-sauce-labs-bike-light")
    product_to_remove.click()

    badge = driver.find_element(By.CSS_SELECTOR, ".shopping_cart_badge").text
    assert badge == "5"

    checkout_button = driver.find_element(By.NAME, "checkout")
    checkout_button.click()

    first_name = driver.find_element(By.NAME, "firstName")
    first_name.send_keys("Paulo")

    last_name = driver.find_element(By.NAME, "lastName")
    last_name.send_keys("Oliveira")

    postal_code = driver.find_element(By.NAME, "postalCode")
    postal_code.send_keys("4000-000")

    continue_button = driver.find_element(By.CLASS_NAME, "submit-button")
    continue_button.click()

    finish_button = driver.find_element(By.CSS_SELECTOR, "#finish")
    finish_button.click()

    confirmation_message = driver.find_element(By.CLASS_NAME, "complete-header").text
    assert confirmation_message == "Thank you for your order!"

    sleep(3)

def test_sorting(driver):
    username = driver.find_element(By.NAME, "user-name")
    username.send_keys("standard_user")

    password = driver.find_element(By.NAME, "password")
    password.send_keys("secret_sauce")

    button = driver.find_element(By.ID, "login-button")
    button.click()

    Select(driver.find_element(By.CLASS_NAME, "product_sort_container")).select_by_visible_text("Price (low to high)")

    sleep(5)

    products = driver.find_elements(By.CLASS_NAME, "inventory_item_price")

    prices = []

    for product in products:
        price = product.text
        price = price.replace("$", "")
        prices.append(float(price))
    
    sorted_prices = sorted(prices)

    assert prices == sorted_prices

def test_locked_user(driver):
    username = driver.find_element(By.NAME, "user-name")
    username.send_keys("locked_out_user")

    password = driver.find_element(By.NAME, "password")
    password.send_keys("secret_sauce")

    button = driver.find_element(By.ID, "login-button")
    button.click()

    sleep(3)

    error_message = driver.find_element(By.XPATH, "//h3[@data-test='error']")
    assert error_message.text == "Epic sadface: Sorry, this user has been locked out."