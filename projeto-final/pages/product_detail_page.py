from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep

class ProductPage(BasePage):
    AVAILABILITY = (By.XPATH, "//div[@id='entry_216826']//li[3]//span[2]")
    ADD_TO_CART = (By.XPATH, "//div[@id='entry_216842']/button")
    NOTIFICATION_CART_INFO = (By.XPATH, "//div[@id='notification-box-top']//span")
    NOTIFICATION_VIEW_CART = (By.XPATH, "//div[@class='form-row']/div[1]/a")
    PRODUCT_PRICE = (By.XPATH, "//h3[@data-update='price']")

    def get_availability_status(self):
        return self.wait_for_element(self.AVAILABILITY).text
    
    def click_add_cart_button(self):
        self.wait_for_element(self.ADD_TO_CART).click()
    
    def get_notification_cart_info_items(self):
        content = self.wait_for_element(self.NOTIFICATION_CART_INFO).text
        content = content.split(" ")
        return int(content[0])
    
    def get_notification_cart_info_amount(self):
        content = self.wait_for_element(self.NOTIFICATION_CART_INFO).text
        content = content.split(" ")
        return content[3]
    
    def click_view_cart_button(self):
        self.wait_for_element(self.NOTIFICATION_VIEW_CART).click()

    def get_product_price(self):
        return self.wait_for_element(self.PRODUCT_PRICE).text
    