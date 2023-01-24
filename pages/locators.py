from  selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LogonPageLocators:
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PAROL_1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_PAROL_2 = (By.CSS_SELECTOR, "#id_registration-password2")

    LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PAROL = (By.CSS_SELECTOR, "#id_login-password")

class ProductPageLocators:
    ADD_IN_BACKET = (By.XPATH, './/*[@value="Добавить в корзину"]')
    NAME_BEFORE_ADD = (By.XPATH, './/*[@class="col-sm-6 product_main"]/h1')
    NAME_AFTER_ADD = (By.XPATH, './/*[@class="alertinner "]/strong')
    PRICE_BEFORE_ADD = (By.XPATH, './/*[@class="price_color"]')
    PRICE_AFTER_ADD = (By.XPATH, './/*[@class="alertinner "]/p/strong')

