
from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_basket_empty(self): # метод, проверяющий наличие ссылки
        assert self.is_not_element_present(*BasketPageLocators.EMPTY_BASKET), "Basket is empty"

    def should_be_text_basket_is_empty(self):
        basket_text=self.browser.find_element(*BasketPageLocators.BASKET_TEXT).text
        assert "корзина пуста" in basket_text, "'корзина пуста' not in {basket_text}"

