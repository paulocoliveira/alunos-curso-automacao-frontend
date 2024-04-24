import csv
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

csv_file_path = "users.csv"

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://paulocoliveira.github.io/mypages/plugins/index.html")
    yield driver
    driver.quit()

def test_fill_form_from_csv(driver):
    driver.find_element(By.XPATH, "//button[text()='CSV']").click()

    with open(csv_file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for nome, sobrenome, email in reader:
            driver.find_element(By.ID, "nome").send_keys(nome)
            driver.find_element(By.ID, "sobrenome").send_keys(sobrenome)
            driver.find_element(By.ID, "email").send_keys(email)
            driver.find_element(By.XPATH, "//button[text()='Cadastrar']").click()
            sleep(1)
        sleep(20)