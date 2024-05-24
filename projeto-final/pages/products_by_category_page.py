from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep

class ProductsByCategoryPage(BasePage):
    PRODUCTS = {
        28: (By.XPATH, "//a[@id='mz-product-grid-image-28-212408']"),
        29: (By.XPATH, "//a[@id='mz-product-grid-image-29-212408']")
    }

    def get_availability_status(self):
        return self.wait_for_element(self.AVAILABILITY).text

    def click_on_product(self, product_id):
        product_element = self.PRODUCTS.get(product_id)
        self.wait_for_element(product_element).click()