from .base_page import BasePage

from .locators import LogonPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url

    def should_be_login_form(self):
        assert self.is_element_present(*LogonPageLocators.LOGIN_EMAIL), 'Selectors for LOGIN_EMAIL is not prezent'
        assert self.is_element_present(*LogonPageLocators.LOGIN_PAROL), 'Selectors for LOGIN_PAROL is not prezent'

    def should_be_register_form(self):
        assert self.is_element_present(*LogonPageLocators.REGISTER_EMAIL), 'Selectors for REGISTER_EMAIL is not prezent'
        assert self.is_element_present(
            *LogonPageLocators.REGISTER_PAROL_1), 'Selectors for REGISTER_PAROL_1 is not prezent'
        assert self.is_element_present(
            *LogonPageLocators.REGISTER_PAROL_2), 'Selectors for REGISTER_PAROL_2 is not prezent'
