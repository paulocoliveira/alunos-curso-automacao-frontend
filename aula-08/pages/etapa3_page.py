from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage
from time import sleep

class Etapa3Page(BasePage):
    INTERESSE_MENTORIA = (By.ID, "interesseMentoria")
    DESCRICAO = (By.ID, "descricao")
    ENVIAR_BUTTON = (By.XPATH, "//button[text()='Enviar Inscrição']")

    def preencher_etapa3(self, interesse_mentoria, descricao):
        self.wait_for_element(self.INTERESSE_MENTORIA)
        select_interesse_mentoria = Select(self.driver.find_element(*self.INTERESSE_MENTORIA))
        select_interesse_mentoria.select_by_visible_text(interesse_mentoria)
        self.driver.find_element(*self.DESCRICAO).send_keys(descricao)
        self.driver.find_element(*self.ENVIAR_BUTTON).click()