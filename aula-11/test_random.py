import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import random

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://paulocoliveira.github.io/mypages/plugins/index.html")
    driver.find_element(By.XPATH, "//button[text()='Random']").click()
    yield driver
    driver.quit()

def get_language_buttons(driver):
    return driver.find_elements(By.XPATH, "//div[@class='button-grid']/button")

def atest_random_click(driver):
    buttons = get_language_buttons(driver)
    for _ in range(5):
        index = int(random.random() * len(buttons))
        print(index)
        random_button = buttons[index]
        random_button.click()
        sleep(3)

def atest_random_int_click(driver):
    buttons = get_language_buttons(driver)
    for _ in range(5):
        index = random.randint(0, len(buttons)-1)
        print(index)
        random_button = buttons[index]
        random_button.click()
        sleep(3)

def atest_random_choice_click(driver):
    buttons = get_language_buttons(driver)
    for _ in range(5):
        random_button = random.choice(buttons)
        random_button.click()
        sleep(3)

def atest_random_shuffle_click(driver):
    buttons = get_language_buttons(driver)
    random.shuffle(buttons)
    for button in buttons[:5]:
        button.click()
        sleep(3)

def atest_random_sample_click(driver):
    buttons = get_language_buttons(driver)
    sampled_buttons = random.sample(buttons, 5)
    for button in sampled_buttons:
        button.click()
        sleep(3)
    
def atest_random_randrange_click(driver):
    buttons = get_language_buttons(driver)
    for _ in range(5):
        index = random.randrange(0, len(buttons))
        random_button = buttons[index]
        random_button.click()
        sleep(2)

def atest_random_uniform_click(driver):
    buttons = get_language_buttons(driver)
    for _ in range(5):
        index = int(random.uniform(0, len(buttons)))
        buttons[index].click()
        sleep(2)