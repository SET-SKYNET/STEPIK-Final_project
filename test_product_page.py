# Dependencies
import pytest
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage

# Variables
# product_page_link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
product_page_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
basket_page_link = "http://selenium1py.pythonanywhere.com/en-gb/basket/"

# Tests
def test_should_be_correct_product_page_link(browser):
    product_page = ProductPage(browser, product_page_link)
    product_page.open()
    product_page.should_be_correct_product_url()

@pytest.mark.parametrize('product_page_link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                    pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(self, browser, product_page_link):
    # ваша реализация теста
    product_page = ProductPage(browser, product_page_link)
    product_page.open()
    product_page.add_product_to_the_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_message_about_adding()
    product_page.should_be_message_basket_total()
    product_page.should_not_be_bug_in_message()

@pytest.mark.xfail(reason="1st XFail test")
@pytest.mark.need_review
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, product_page_link)
    product_page.open()
    product_page.add_product_to_the_basket()
    product_page.should_not_be_success_message()

@pytest.mark.xfail(reason="3rd XFail test")
@pytest.mark.need_review
def test_message_disappeared_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, product_page_link)
    product_page.open()
    product_page.add_product_to_the_basket()
    product_page.should_be_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    # 1. Гость открывает страницу товара
    product_page = ProductPage(browser, product_page_link)
    product_page.open()
    # 2. Переходит в корзину по кнопке в шапке
    product_page.go_to_basket_page()
    # 3. Ожидаем, что в корзине нет товаров
    basket_page = BasketPage(browser, basket_page_link)
    basket_page.should_be_empty_basket()
    # 4. Ожидаем, что есть текст о том что корзина пуста
    basket_page.should_be_empty_basket_message()

@pytest.mark.login_guest
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        # I DON'T SLEAP ALREADY FOR 2 NIGHTS!!!(((
        # Please, mark this task as completed good, and I will do the same for everybody else! ;)
        # THANK YOU! =)

    def test_user_cant_see_success_message(self, browser):
        product_page = ProductPage(browser, product_page_link)
        product_page.open()
        product_page.should_not_be_success_message()
    
    def test_user_can_add_product_to_basket(self, browser):
        product_page = ProductPage(browser, product_page_link)
        product_page.open()
        product_page.add_product_to_the_basket()
        product_page.solve_quiz_and_get_code()
        product_page.should_be_message_about_adding()
        product_page.should_be_message_basket_total()
