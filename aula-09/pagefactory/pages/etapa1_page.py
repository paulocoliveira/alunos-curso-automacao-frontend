from pages.base_page import BasePage
from seleniumpagefactory import PageFactory
from time import sleep

class Etapa1Page(BasePage, PageFactory):
    locators = {
        "nome": ("ID", "nome"),
        "email": ("ID", "email"),
        "idade": ("ID", "idade"),
        "whatsapp": ("ID", "whatsapp"),
        "cidade": ("ID", "cidade"),
        "prosseguir": ("XPATH", "//button[text()='Prosseguir']")
    }
    
    def preencher_etapa1(self, nome, email, idade, whatsapp, cidade):
        self.nome.set_text(nome)
        self.email.set_text(email)
        self.idade.set_text(idade)
        self.whatsapp.set_text(whatsapp)
        self.cidade.set_text(cidade)
        sleep(3)
        self.prosseguir.click_button()