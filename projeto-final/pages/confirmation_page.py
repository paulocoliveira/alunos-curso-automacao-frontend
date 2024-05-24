from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class ConfirmationPage(BasePage):
    CONFIRM_ORDER_BUTTON = (By.XPATH, "//button[@id='button-confirm']")
    
    def click_confirm_order_button(self):
        self.wait_for_element(self.CONFIRM_ORDER_BUTTON).click()

        try:
            WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            print("Alert found: " + alert.text)
            alert.accept()
        except:
            print("No alert found.")