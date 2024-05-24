import pytest
import random
import string
from selenium import webdriver
from time import sleep
from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.product_detail_page import ProductPage
from pages.products_by_category_page import ProductsByCategoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.confirmation_page import ConfirmationPage
from pages.final_page import FinalPage

def generate_random_email():
    letter = string.ascii_letters
    random_string = ""

    for i in range(10):
        random_letter = random.choice(letter)
        random_string += random_letter
    
    email = f"paulocol+{random_string}@gmail.com"
    return email

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    BasePage(driver).go_to_site()
    yield driver
    driver.quit()

def atest_out_of_stock(driver):
    main = MainPage(driver)
    main.click_active_banner()

    product_detail = ProductPage(driver)
    status = product_detail.get_availability_status()

    expected_status = "Out Of Stock"

    assert status == expected_status

    sleep(5)

def atest_item_after_scrolling(driver):
    main = MainPage(driver)
    BasePage(driver).scroll_all_page()
    
    main.click_entry_product()

    product_detail = ProductPage(driver)
    status = product_detail.get_availability_status()
    
    expected_status = "2-3 Days"

    assert status == expected_status

    sleep(5)

def test_buy_from_category(driver):
    main = MainPage(driver)
    main.click_category_menu()
    main.click_submenu_camera()

    products_by_category = ProductsByCategoryPage(driver)
    products_by_category.click_on_product(28)

    product_detail = ProductPage(driver)
    product_detail.click_add_cart_button()

    expected_items = 1
    expected_ammount = product_detail.get_product_price()

    items = product_detail.get_notification_cart_info_items()
    assert items == expected_items

    ammount = product_detail.get_notification_cart_info_amount()
    assert ammount == expected_ammount

    product_detail.click_view_cart_button()

    cart = CartPage(driver)
    cart.change_product_quantity(10)
    cart.click_checkout_button()

    checkout = CheckoutPage(driver)
    checkout.fill_payment_details("Paulo", "Oliveira", generate_random_email(), "+351936889403", "123456", "Rua ABC", "Porto", "4000")
    checkout.check_terms()
    checkout.click_continue_button()

    confirm_order = ConfirmationPage(driver)
    confirm_order.click_confirm_order_button()

    sleep(5)

    #Neste momento, o site está mostrando um alert quando clica no botão e não consigo avançar para a próxima tela
    #O código abaixo não é executado enquanto o problema está acontecendo.

    expected_suceess_message = "Your order has been placed!"
    final = FinalPage(driver)
    message = final.get_message()

    assert message == expected_suceess_message

    sleep(5)