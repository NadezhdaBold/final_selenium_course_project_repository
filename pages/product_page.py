import pytest
from selenium import webdriver
from .base_page import BasePage
from .locators import ProductPageLocators
from .login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class ProductPage(BasePage):
    def should_be_product_basket_add(self, link):
            assert "был добавлен в вашу корзину" in self.browser.find_element(*ProductPageLocators.ALERT_BASKET_ADD).text, "'был добавлен в вашу корзину' not in current alert"

    def should_be_product_name(self):
        pname=self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        pbasket_name=self.browser.find_element(*ProductPageLocators.ALERT_NAME).text
        assert pname==pbasket_name, "{pbasket_name} не соответствует {pname}" # проверка, имени продукта в корзине

    def should_be_product_price(self):
        pprice = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        pbasket_price = self.browser.find_element(*ProductPageLocators.ALERT_PRICE).text
        assert pprice == pbasket_price, "{pbasket_price} не соответствует {pprice}"  # проверка, имени продукта в корзине

    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.BASKET_BUTTON).click()
