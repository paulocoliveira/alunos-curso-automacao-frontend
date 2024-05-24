from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep

class MainPage(BasePage):
    BANNER = (By.CSS_SELECTOR, "div.carousel-item.active > a")
    ENTRY_PRODUCT = (By.XPATH, "//a[@id='mz-product-listing-image-81213270-0-1']")
    MENU_CATEGORY = (By.XPATH, "//div[@id='entry_217832']/a")
    SUBMENU_CAMERA = (By.XPATH, "//div[@id='entry_217841']//li[2]/a")

    def click_active_banner(self):
        self.wait_for_element(self.BANNER).click()
    
    def click_entry_product(self):
        self.wait_for_element(self.ENTRY_PRODUCT).click()
    
    def click_category_menu(self):
        self.wait_for_element(self.MENU_CATEGORY).click()
    
    def click_submenu_camera(self):
        sleep(1)
        self.wait_for_element(self.SUBMENU_CAMERA).click()