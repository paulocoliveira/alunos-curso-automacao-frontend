import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def load_config():
    print("\nCarregando configuração global para todos os testes.")
    config = {
        "url": "https://www.google.com", 
        "db": "test_db"
    }
    return config

@pytest.fixture(scope="module")
def browser(load_config):
    print("\nIniciando o navegador para os testes do módulo.")
    driver = webdriver.Chrome()
    driver.get(load_config["url"])
    yield driver
    print("\nFechando o navegador.")
    driver.quit()

@pytest.fixture(scope="class")
def database(load_config):
    print("\nConectando ao banco de dados para os testes da classe.")
    db_connection = load_config["db"]
    yield db_connection
    print("\nDesconectando do banco de dados.")

@pytest.fixture(scope="function")
def clean_data():
    print("\nResetando os dados para o teste.")
    data = {"users": []}
    return data

@pytest.mark.usefixtures("database")
class TestWebApp:
    def test_one(self, browser):
        print("\nExecutando test_one.")
    
    def test_two(self, browser):
        print("\nExecutando test_two")

def test_data_handling(clean_data):
    print("\nTestando manipulação de dados.")
    clean_data["users"].append("user1")

def test_data_cleaning(clean_data):
    print("\nTestando limpeza de dados.")