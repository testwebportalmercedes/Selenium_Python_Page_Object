import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.main_page import MainPage
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import time



def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)                        #Для инициализации драйвера к адресу
    page.open()                                           #Для открытия страницы
    page.go_login_page()                                  #Для перехода к логину
    time.sleep(5)
    login_page = LoginPage(browser, browser.current_url)  #Для инициализации драйвера к новому адресу
    login_page.should_be_login_page()                     #Проверка на другой страницы


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

# //////////////////////////////////// Переход с главной в корзину и проверка
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_backet()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_no_message_about_the_product_availability()
    basket_page.should_be_message_about_basket_is_empty()
