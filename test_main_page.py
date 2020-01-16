# Dependencies
from pages.main_page import MainPage
from pages.login_page import LoginPage

# Variables
main_page_link = "http://selenium1py.pythonanywhere.com/"
login_page_link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"

# Tests
def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, main_page_link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_should_see_login_link(browser):
    page = MainPage(browser, main_page_link)
    page.open()
    page.should_be_login_link()

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
