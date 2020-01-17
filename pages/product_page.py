# Dependencies
from .base_page import BasePage
from .locators import ProductPageLocators

# Login page methods
class ProductPage(BasePage):
    def should_be_correct_product_url(self):
        actual_product_page_url = self.browser.current_url
        expected_product_page_suburl = "coders-at-work_207"
        assert expected_product_page_suburl in actual_product_page_url, \
            f"Product page url [ {actual_product_page_url} ] didn't contain substring [ {expected_product_page_suburl} ]"

    def add_product_to_the_basket(self):
        # Verify, that elements are on the page
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "'Add to basket' button is not presented"
        # Click 'Add to basket' button
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()
    
    def should_be_message_about_adding(self):
        # Verify, that elements are on the page
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), (
            "Product name is not presented")
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), (
            "Message about adding is not presented")
        # Receiving elements text, for verification
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        # Verification, that product name is present in succeed adding message
        assert product_name in message, "No product name in the message"

    def should_be_message_basket_total(self):
        # Verify, that elements are on the page
        assert self.is_element_present(*ProductPageLocators.MESSAGE_BASKET_TOTAL), (
            "Message basket total is not presented")
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), (
            "Product price is not presented")
        # Receiving elements text, for verification
        message_basket_total = self.browser.find_element(*ProductPageLocators.MESSAGE_BASKET_TOTAL).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        # Verification, that product price is present in basket cost message
        assert product_price in message_basket_total, "No product price in the message"

    def should_not_be_bug_in_message(self):
        # Verify, that element are on the page
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), (
            "Message about adding is not presented")
        # Receiving element text, for verification
        message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        assert message == "Coders at Work has been added to your basket."

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not presented, but should be"
