from pages.base_page import BasePage
from seleniumpagefactory import PageFactory

class FinalPage(BasePage, PageFactory):
    locators = {
        "message": ("CSS", ".final-message h2")
    }

    def obter_mensagem(self):
        return self.message.get_text()