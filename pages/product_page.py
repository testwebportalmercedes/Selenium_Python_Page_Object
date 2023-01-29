from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_in_backet(self):
        backet = self.browser.find_element(*ProductPageLocators.ADD_IN_BACKET).click()


    def should_be_name_book(self):
        assert self.is_element_present(*ProductPageLocators.NAME_BEFORE_ADD)

    def should_be_name_book_after_add_to_backet(self):
        name_before = self.browser.find_element(*ProductPageLocators.NAME_BEFORE_ADD).text
        name_after = self.browser.find_element(*ProductPageLocators.NAME_AFTER_ADD).text
        assert name_before == name_after

    def should_be_price_book_after_add_to_backet(self):
        price_before = self.browser.find_element(*ProductPageLocators.PRICE_BEFORE_ADD).text
        price_after = self.browser.find_element(*ProductPageLocators.PRICE_AFTER_ADD).text

        assert price_before == price_after

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.NAME_AFTER_ADD), \
            "Success message is presented, but should not be"