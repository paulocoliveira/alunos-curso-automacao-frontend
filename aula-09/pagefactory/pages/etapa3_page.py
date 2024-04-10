from pages.base_page import BasePage
from seleniumpagefactory import PageFactory
from time import sleep

class Etapa3Page(BasePage, PageFactory):
    locators = {
        "interesse_mentoria": ("ID", "interesseMentoria"),
        "descricao": ("ID", "descricao"),
        "enviar": ("XPATH", "//button[text()='Enviar Inscrição']")
    }

    def preencher_etapa3(self, interesse_mentoria, descricao):
        self.interesse_mentoria.set_text(interesse_mentoria)
        self.descricao.set_text(descricao)
        sleep(3)
        self.enviar.click_button()