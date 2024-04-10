from strategies.regular_user_test_strategy import RegularUserTestStrategy
from strategies.admin_user_test_strategy import AdminUserTestStrategy
from strategies.super_admin_user_test_strategy import SuperAdminUserTestStrategy
import pytest
from selenium import webdriver

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://paulocoliveira.github.io/mypages/login/index.html")
    yield driver
    driver.quit()

def test_regular_user_behaviour(driver):
    strategy = RegularUserTestStrategy(driver)
    strategy.execute_test()

def test_admin_user_behaviour(driver):
    strategy = AdminUserTestStrategy(driver)
    strategy.execute_test()

def test_super_admin_user_behaviour(driver):
    strategy = SuperAdminUserTestStrategy(driver)
    strategy.execute_test()

def test_users_behaviour(driver):
    strategy = AdminUserTestStrategy(driver)
    strategy.execute_test()

    strategy = SuperAdminUserTestStrategy(driver)
    strategy.execute_test()

    strategy = RegularUserTestStrategy(driver)
    strategy.execute_test()