import pytest
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

csv_file_path = "users.csv"

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://paulocoliveira.github.io/mypages/plugins/index.html")
    driver.find_element(By.XPATH, "//button[text()='CSV']").click()
    yield driver
    driver.quit()

def load_user_data():
    with open("users.json") as jsonfile:
        return json.load(jsonfile)

@pytest.mark.parametrize("user", load_user_data())
def test_fill_form_from_json(driver, user):
    driver.find_element(By.ID, "nome").send_keys(user["Nome"])
    driver.find_element(By.ID, "sobrenome").send_keys(user["Sobrenome"])
    driver.find_element(By.ID, "email").send_keys(user["Email"])
    driver.find_element(By.XPATH, "//button[text()='Cadastrar']").click()
    sleep(1)
sleep(10)