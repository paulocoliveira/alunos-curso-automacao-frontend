import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import os

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    #driver.implicitly_wait(10)
    driver.get("https://paulocoliveira.github.io/mypages/waits/index.html")
    yield driver
    driver.quit()

def test_implicity_wait(driver):
    driver.find_element(By.XPATH, "//section[@id='conditional-element-section']/button").click()
    driver.find_element(By.ID, "hidden-button").click()
    sleep(8)

def test_file_upload(driver):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(current_dir, "qrcode.png")
    
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "file-upload"))
    )

    driver.find_element(By.ID, "file-upload").send_keys(image_path)

    driver.find_element(By.XPATH, "//button[contains(text(), 'Enviar Arquivo')]").click()

    message_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "file-upload-status"))
    )

    assert message_element.text == "Arquivo enviado"

    sleep(10)

def test_email_sending(driver):
    send_email_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'Enviar Email')]"))
    )

    send_email_button.click()

    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.ID, "email-status"), "Email enviado com sucesso")
    )

    WebDriverWait(driver, 10).until(
        EC.title_contains("sucesso")
    )

    WebDriverWait(driver, 10).until(
        EC.title_is("Email enviado com sucesso")
    )

    sleep(8)

def test_conditional_element(driver):
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(driver.find_element(By.XPATH, "//section[@id='conditional-element-section']/button"))
    )

    driver.find_element(By.XPATH, "//section[@id='conditional-element-section']/button").click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of(driver.find_element(By.ID, "hidden-button"))
    )

    driver.find_element(By.ID, "hidden-button").click()

    message = driver.find_element(By.ID, "message").text
    assert message == "Você interagiu com o elemento oculto!"

    sleep(8)

def test_url_change(driver):
    current_url = driver.current_url

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(driver.find_element(By.XPATH, "//section[@id='url-change-section']/button"))
    )

    driver.find_element(By.XPATH, "//section[@id='url-change-section']/button").click()

    WebDriverWait(driver, 10).until(
        EC.url_changes(current_url)
    )

    WebDriverWait(driver, 10).until(
        EC.url_contains("language=python")
    )

    WebDriverWait(driver, 10).until(
        EC.url_matches(r".*?language=python&framework=selenium$")
    )

    sleep(3)

def test_terms_of_service(driver):
    agree_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "agree-button"))
    )

    agree_button.click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_selected(driver.find_element(By.ID, "agree-terms"))
    )

    driver.find_element(By.ID, "confirm-button").click()

    message = driver.find_element(By.ID, "terms-message").text

    assert message == "Você concordou com os termos com sucesso."