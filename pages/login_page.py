# Dependencies
from .base_page import BasePage
from .locators import LoginPageLocators

# Login page methods
class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    # реализуйте проверку на корректный url адрес
    def should_be_login_url(self):
        actual_login_page_url = self.browser.current_url
        expected_login_page_suburl = "login"
        assert expected_login_page_suburl in actual_login_page_url, \
            f"Login page url [ {actual_login_page_url} ] didn't contain substring [ {expected_login_page_suburl} ]"

    # реализуйте проверку, что есть форма логина
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    # реализуйте проверку, что есть форма регистрации на странице
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
