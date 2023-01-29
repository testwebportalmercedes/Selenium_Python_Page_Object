from .base_page import BasePage
from .locators import BasketPageLocator


class BasketPage(BasePage):
    # ///////////////////////////////////////////////////////// Проверка что нет товара в корзине
    def should_be_no_message_about_the_product_availability(self):
        assert self.is_not_element_present(*BasketPageLocator.PRICE_IN_BACKET), \
                'A message about the availability of the product in the cart is displayed, but it should not be'

    # ///////////////////////////////////////////////////////// Проверка что есть сообщение о том что корзина пуста
    def should_be_message_about_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocator.BASKET_IS_EMPTY), \
                'Your shopping cart is not empty'

