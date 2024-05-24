from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()
        self.base_url = "https://ecommerce-playground.lambdatest.io/"
    
    def go_to_site(self):
        self.driver.get(self.base_url)
    
    def wait_for_element(self, locator, timeout = 10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((locator))
        )
    
    def scroll_all_page(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
