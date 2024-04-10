from pages.base_page import BasePage
from seleniumpagefactory import PageFactory
from time import sleep

class Etapa2Page(BasePage, PageFactory):
    locators = {
        "trabalha_area": ("ID", "trabalhaArea"),
        "experiencia": ("ID", "experiencia"),
        "empresa": ("ID", "empresa"),
        "prosseguir": ("XPATH", "//button[text()='Prosseguir']"),
    }

    def preencher_etapa2(self, trabalha_area, experiencia, empresa):
        self.trabalha_area.set_text(trabalha_area)
        self.experiencia.set_text(experiencia)
        self.empresa.set_text(empresa)
        sleep(3)
        self.prosseguir.click_button()