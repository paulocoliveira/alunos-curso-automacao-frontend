from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage
from time import sleep

class Etapa2Page(BasePage):
    TRABALHA_AREA = (By.ID, "trabalhaArea")
    EXPERIENCIA = (By.ID, "experiencia")
    EMPRESA = (By.ID, "empresa")
    PROSSEGUIR = (By.XPATH, "//button[text()='Prosseguir']")

    def preencher_etapa2(self, trabalha_area, experiencia, empresa):
        self.wait_for_element(self.TRABALHA_AREA)
        select_trabalha_area = Select(self.driver.find_element(*self.TRABALHA_AREA))
        select_trabalha_area.select_by_value(trabalha_area)
        self.driver.find_element(*self.EXPERIENCIA).send_keys(experiencia)
        self.driver.find_element(*self.EMPRESA).send_keys(empresa)
        self.driver.find_element(*self.PROSSEGUIR).click()