# Dependencies
from .base_page import BasePage
from .locators import BasketPageLocators

# Login page methods
class BasketPage(BasePage):
        def should_be_empty_basket(self):
            # Verify, that element are on the page
            assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), (
                "Basket is not empty")
            # # Receiving element text, for verification
            # message = self.browser.find_element(*BasketPageLocators.BASKET_ITEMS).text
            # assert message == "Coders at Work has been added to your basket."

        def should_be_empty_basket_message(self):
            # Verify, that element are on the page
            assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), (
                "Message about adding is not presented")
            # Receiving element text, for verification
            actual_message = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text
            expected_message = "Your basket is empty."
            # Verification, that product name is present in succeed adding message
            assert expected_message in actual_message, \
                f"Actual basket message [ {actual_message} ] didn't include expected basket message [ {expected_message} ]"
        
        def should_be_not_empty_basket(self):
            # Verify, that element are on the page
            assert self.is_element_present(*BasketPageLocators.BASKET_ITEMS), (
                "Basket is empty")
            # # Receiving element text, for verification
            # message = self.browser.find_element(*BasketPageLocators.BASKET_ITEMS).text
            # assert message == "Coders at Work has been added to your basket."