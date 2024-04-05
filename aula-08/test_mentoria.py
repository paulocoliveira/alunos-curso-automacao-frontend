import pytest
from selenium import webdriver
from pages.base_page import BasePage
from pages.etapa1_page import Etapa1Page
from pages.etapa2_page import Etapa2Page
from pages.etapa3_page import Etapa3Page
from pages.final_page import FinalPage
from config.webdriver_singleton import WebDriverSingleton
from time import sleep

@pytest.fixture()
def driver():
    driver = WebDriverSingleton.get_instance()
    BasePage(driver).go_to_site()
    yield driver

@pytest.fixture(scope="session", autouse=True)
def close_browser():
    yield
    WebDriverSingleton.quit_instance()

def test_inscricao_completa_1(driver):
    etapa1 = Etapa1Page(driver)
    etapa1.preencher_etapa1("Sueber", "sueber@sueber.com", 18, "+35122336699", "Porto")

    etapa2 = Etapa2Page(driver)
    etapa2.preencher_etapa2("nao", "2", "Nenhuma")

    etapa3 = Etapa3Page(driver)
    etapa3.preencher_etapa3("Automação de testes", "Quero aprender a automatizar usando Python e Selenium")

    final = FinalPage(driver)
    message = final.obter_mensagem()

    assert message == "Obrigado pela sua inscrição!"

    sleep(1)

def test_inscricao_completa_2(driver):
    etapa1 = Etapa1Page(driver)
    etapa1.preencher_etapa1("Júlia", "julia@julia.com", 18, "+35111336699", "Castelo Branco")

    etapa2 = Etapa2Page(driver)
    etapa2.preencher_etapa2("nao", "2", "Nenhuma")

    etapa3 = Etapa3Page(driver)
    etapa3.preencher_etapa3("Automação de testes", "Quero aprender a automatizar usando Python e Selenium")

    final = FinalPage(driver)
    message = final.obter_mensagem()

    assert message == "Obrigado pela sua inscrição!"

    sleep(1)