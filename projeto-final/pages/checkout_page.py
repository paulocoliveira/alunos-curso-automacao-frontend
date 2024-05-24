from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from time import sleep

class CheckoutPage(BasePage):
    FIRST_NAME = (By.ID, "input-payment-firstname")
    LAST_NAME = (By.ID, "input-payment-lastname")
    EMAIL = (By.ID, "input-payment-email")
    TELEPHONE = (By.ID, "input-payment-telephone")
    PWD = (By.ID, "input-payment-password")
    CONFIRM_PWD = (By.ID, "input-payment-confirm")
    ADDRESS_1 = (By.ID, "input-payment-address-1")
    CITY = (By.ID, "input-payment-city")
    POSTAL_CODE = (By.ID, "input-payment-postcode")
    CONTINUE_BUTTON = (By.ID, "button-save")
    
    def check_terms(self):
        self.driver.execute_script("document.getElementById('input-account-agree').checked = true;")
        self.driver.execute_script("document.getElementById('input-agree').checked = true;")

    def click_continue_button(self):
        button = self.wait_for_element(self.CONTINUE_BUTTON)
        self.driver.execute_script("arguments[0].click()", button)
    
    def fill_payment_details(self, first_name, last_name, email, phone, pwd, address, city, code):
        self.wait_for_element(self.FIRST_NAME).send_keys(first_name)
        self.wait_for_element(self.LAST_NAME).send_keys(last_name)
        self.wait_for_element(self.EMAIL).send_keys(email)
        self.wait_for_element(self.TELEPHONE).send_keys(phone)
        self.wait_for_element(self.PWD).send_keys(pwd)
        self.wait_for_element(self.CONFIRM_PWD).send_keys(pwd)
        self.wait_for_element(self.ADDRESS_1).send_keys(address)
        self.wait_for_element(self.CITY).send_keys(city)
        self.wait_for_element(self.POSTAL_CODE).send_keys(code)