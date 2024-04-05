from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep

class Etapa1Page(BasePage):
    NOME = (By.ID, "nome")
    EMAIL = (By.ID, "email")
    IDADE = (By.ID, "idade")
    WHATSAPP = (By.ID, "whatsapp")
    CIDADE = (By.ID, "cidade")
    PROSSEGUIR = (By.XPATH, "//button[text()='Prosseguir']")
    
    def preencher_etapa1(self, nome, email, idade, whatsapp, cidade):
        self.wait_for_element(self.NOME).send_keys(nome)
        self.driver.find_element(*self.EMAIL).send_keys(email)
        self.driver.find_element(*self.IDADE).send_keys(idade)
        self.driver.find_element(*self.WHATSAPP).send_keys(whatsapp)
        self.driver.find_element(*self.CIDADE).send_keys(cidade)
        self.driver.find_element(*self.PROSSEGUIR).click()