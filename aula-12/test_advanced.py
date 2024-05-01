import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://paulocoliveira.github.io/mypages/advanced/index.html")
    yield driver
    driver.quit()

def test_slider_interaction(driver):
    slider = driver.find_element(By.ID, "range-slider")
    slider_value = driver.find_element(By.ID, "slider-value")
    slider_size = slider.size["width"]

    target_value = 75
    current_value = int(slider.get_attribute("value"))
    offset = slider_size * (target_value - current_value)/99

    actions = ActionChains(driver)
    actions.move_to_element_with_offset(slider, 0, 0)
    actions.click_and_hold()
    actions.move_by_offset(offset, 0)
    actions.release()
    actions.perform()

    final_value = int(slider_value.text)

    assert target_value-1 <= final_value <= target_value+1

    sleep(10)

def test_switch_interaction(driver):
    switch = driver.find_element(By.ID, "switch")
    button = driver.find_element(By.ID, "toggle-button")

    assert not button.is_enabled()

    driver.execute_script("arguments[0].click()", switch)

    assert button.is_enabled()

    sleep(10)

def test_dynamic_dropdown_interaction(driver):
    primary = Select(driver.find_element(By.ID, "primary-select"))
    secondary = Select(driver.find_element(By.ID, "secondary-select"))

    primary.select_by_value("opcao2")
    WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.ID, "secondary-select"), "Subopção 2.2"))
    secondary.select_by_visible_text("Subopção 2.2")

    sleep(10)

def test_modal_interaction(driver):
    open_modal_button = driver.find_element(By.ID, "open-modal")
    open_modal_button.click()

    modal = driver.find_element(By.ID, "modal")

    assert modal.is_displayed()

    name = modal.find_element(By.ID, "name-input")
    name.send_keys("Magda")

    submit_button = modal.find_element(By.ID, "submit-name")
    submit_button.click()

    message = modal.find_element(By.ID, "success-message")

    assert message.text == "Sucesso! Olá, Magda!"

    sleep(10)

def test_iframe_interaction(driver):
    my_frame = driver.find_element(By.ID, "example-frame")

    driver.switch_to.frame(my_frame)

    nickname = driver.find_element(By.ID, "nickname")
    confirm_button = driver.find_element(By.ID, "confirm-button")
    nickname.send_keys("Magda Little")
    confirm_button.click()
    message = driver.find_element(By.ID, "confirmation-message")
    assert message.text == "Pronto! Deu tudo certo, Magda Little!"

    driver.switch_to.default_content()

    final_button = driver.find_element(By.ID, "final-button")
    final_button.click()
    final_message = driver.find_element(By.ID, "final-message")
    assert final_message.text == "A aula acabou!"

    driver.switch_to.frame(my_frame)

    nickname.clear()
    nickname.send_keys("Magda Little 2")
    confirm_button.click()
    message = driver.find_element(By.ID, "confirmation-message")
    assert message.text == "Pronto! Deu tudo certo, Magda Little 2!"

    driver.switch_to.default_content()

    sleep(10)