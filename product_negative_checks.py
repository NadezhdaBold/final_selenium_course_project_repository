import pytest
from .pages.main_page import MainPage
from .pages.product_page import ProductPage
import time

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link="http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    product_page = ProductPage(browser, browser.current_url)
    product_page.add_to_basket()
    time.sleep(1)
    product_page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    product_page = ProductPage(browser, browser.current_url)
    time.sleep(1)
    product_page.should_not_be_success_message()
    time.sleep(6)

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link="http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    product_page = ProductPage(browser, browser.current_url)
    product_page.add_to_basket()
    time.sleep(1)
    product_page.should_be_disappeared_element()