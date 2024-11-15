import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
import time

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
@pytest.mark.xfail #используется локатор LOGIN_LINK_INVALID, чтоб отработал в go_to_login_page() поменять локатор на LOGIN_LINK в base_page.py
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser): #перейти в корзину и проверить что она пустая
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_empty()
    basket_page.should_be_text_basket_is_empty()

@pytest.mark.need_review
@pytest.mark.parametrize('promo_offer', [0,1,2,3,4,5,6,pytest.param(7, marks=pytest.mark.xfail),8,9])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link=f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    product_page = ProductPage(browser, browser.current_url)
    product_page.add_to_basket()
    time.sleep(1)
    product_page.solve_quiz_and_get_code()
    product_page.should_be_product_basket_add(link)
    product_page.should_be_product_name()
    product_page.should_be_product_price()


class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup (self,browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page=LoginPage(browser, link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = "ASW456789"
        page.register_new_user(email, password)
        time.sleep(2)
        page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page = MainPage(browser,
                        link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        product_page = ProductPage(browser, browser.current_url)
        product_page.add_to_basket()
        time.sleep(1)
        product_page.solve_quiz_and_get_code()
        product_page.should_be_product_basket_add(link)
        product_page.should_be_product_name()
        product_page.should_be_product_price()
        time.sleep(3)

    def test_user_cant_see_success_message(self,browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        product_page = ProductPage(browser, browser.current_url)
        time.sleep(1)
        product_page.should_not_be_success_message()

