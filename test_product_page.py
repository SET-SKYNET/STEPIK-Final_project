# Dependencies
from pages.product_page import ProductPage
import pytest

# Variables
# product_page_link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
product_page_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

# Tests
# def test_should_be_correct_product_page_link(browser):
#     product_page = ProductPage(browser, product_page_link)
#     product_page.open()
#     product_page.should_be_correct_product_url()

# def test_guest_can_add_product_to_basket(browser):
#     product_page = ProductPage(browser, product_page_link)
#     product_page.open()
#     product_page.add_product_to_the_basket()
#     product_page.solve_quiz_and_get_code()
#     product_page.should_be_message_about_adding()
#     product_page.should_be_message_basket_total()

# @pytest.mark.parametrize('product_page_link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                      pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
# def test_guest_can_add_product_to_basket(browser, product_page_link):
#     # ваша реализация теста
#     product_page = ProductPage(browser, product_page_link)
#     product_page.open()
#     product_page.add_product_to_the_basket()
#     product_page.solve_quiz_and_get_code()
#     product_page.should_be_message_about_adding()
#     product_page.should_be_message_basket_total()
#     product_page.should_not_be_bug_in_message()

# @pytest.mark.xfail(reason="1st XFail test")
# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#     product_page = ProductPage(browser, product_page_link)
#     product_page.open()
#     product_page.add_product_to_the_basket()
#     product_page.should_not_be_success_message()

# def test_guest_cant_see_success_message(browser):
#     product_page = ProductPage(browser, product_page_link)
#     product_page.open()
#     product_page.should_not_be_success_message()

# @pytest.mark.xfail(reason="3rd XFail test")
# def test_message_disappeared_after_adding_product_to_basket(browser):
#     product_page = ProductPage(browser, product_page_link)
#     product_page.open()
#     product_page.add_product_to_the_basket()
#     product_page.should_be_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
