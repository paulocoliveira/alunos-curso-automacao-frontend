import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import re

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://paulocoliveira.github.io/mypages/text/index.html")
    return driver

def atest_interactions(driver):
    
    input_element = driver.find_element(By.ID, "inputText")
    add_button = driver.find_element(By.XPATH, "//button[text()='Adicionar']")

    text_data = """  
        Transaction Code: VJFI-674623, Phone: (59) 66301406
        Transaction Code: EIMZ-898724, Email: ybejhfyq@example.com
        Transaction Code: TSFW-655188, Email: wgvpeypbp@demo.net
        Transaction Code: UTNS-044799, Email: wvoav@test.org, Phone: (77) 84962052
        Transaction Code: HHMV-273514
        Transaction Code: KEMB-337781, Email: wrlvrzppvk@sample.edu, Phone: (42) 26467422
        Transaction Code: ZTWI-206815, Email: lrmqo@example.com, Phone: (76) 52291804
        """
    
    if re.match(r'Transaction Code: \w+-\d+', text_data.strip()):
        print("O texto começa com um código de transação válida!")
    else:
        print("O texto NÃO começa com um código de transação válida!")
    
    phone = re.search(r'\(\d{2}\) \d{8}', text_data)

    if phone:
        input_element.send_keys(phone.group())
        add_button.click()
    
    transaction_codes = re.findall(r'Transaction Code: (\w+-\d+)', text_data)

    for code in transaction_codes:
        input_element.send_keys(code)
        add_button.click()

    transaction_codes_pattern = re.compile(r'Transaction Code: (\w+-\d+)')
    codes = transaction_codes_pattern.findall(text_data)

    for code in codes:
        input_element.send_keys(code)
        add_button.click()

    sleep(20)

