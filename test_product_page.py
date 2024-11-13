import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
import time

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
    time.sleep(3)



