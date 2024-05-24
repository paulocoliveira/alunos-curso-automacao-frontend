from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from time import sleep

class CartPage(BasePage):
    QUANTITY = (By.XPATH, "//div[@class='table-responsive']//input")
    CHECKOUT_BUTTON = (By.XPATH, "//div[@id='content']/div[last()]/a[2]")

    def change_product_quantity(self, qty):
        quantity = self.wait_for_element(self.QUANTITY)
        quantity.clear()
        quantity.send_keys(qty)
        quantity.send_keys(Keys.ENTER)
    
    def click_checkout_button(self):
        self.wait_for_element(self.CHECKOUT_BUTTON).click()