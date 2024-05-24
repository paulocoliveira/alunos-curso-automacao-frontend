from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep

class FinalPage(BasePage):
    MESSAGE = (By.XPATH, "//div[@id='content']/h1")
    
    def get_message(self):
        return self.wait_for_element(self.MESSAGE).text