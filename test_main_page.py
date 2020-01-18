# Dependencies
import pytest
from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage

# Variables
main_page_link = "http://selenium1py.pythonanywhere.com/"
login_page_link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
basket_page_link = "http://selenium1py.pythonanywhere.com/en-gb/basket/"

# Tests
def test_should_be_correct_login_page_link(browser):
    page = MainPage(browser, main_page_link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_url()

def test_login_page_guest_should_see_login_form(browser):
    login_page = LoginPage(browser, login_page_link)
    login_page.open()
    login_page.should_be_login_form()

def test_login_page_guest_should_see_register_form(browser):
    login_page = LoginPage(browser, login_page_link)
    login_page.open()
    login_page.should_be_register_form()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    # 1. Гость открывает главную страницу
    page = MainPage(browser, main_page_link)
    page.open()
    # 2. Переходит в корзину по кнопке в шапке сайта
    page.go_to_basket_page()
    # 3. Ожидаем, что в корзине нет товаров
    basket_page = BasketPage(browser, basket_page_link)
    basket_page.should_be_empty_basket()
    # 4. Ожидаем, что есть текст о том что корзина пуста
    basket_page.should_be_empty_basket_message()

class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, main_page_link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, main_page_link)
        page.open()
        page.should_be_login_link()

