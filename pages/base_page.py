from selenium.common.exceptions import NoSuchElementException
from .locators import ProductPageLocators
from .locators import BasePageLocator
from .locators import BasketPageLocator
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    # //////////////////////////////////////// Переход на главную страницу с любой страницы
    def go_login_page(self):
        login_link = self.browser.find_element(*BasePageLocator.LOGIN_LINK)
        login_link.click()

    # ///////////////////////////////////////////////////  Переход в корзину с любой страницы
    def go_to_backet(self):
        go_to_backet = self.browser.find_element(*BasketPageLocator.GO_TO_BACKET)
        go_to_backet.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocator.LOGIN_LINK)

    # //////////////////////////////////////////////// Проверка что элемент присутствует
    def is_element_present(self, how, what):

        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    # //////////////////////////////////////////////// Проверка что элемент отсутствует
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    # //////////////////////////////////////////////// Проверка что элемент исчезает
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True


