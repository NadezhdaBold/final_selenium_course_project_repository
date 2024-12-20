import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import math
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators
from .locators import MainPageLocators


class BasePage():
    def __init__(self, browser, url, timeout=10):  # конструктор в качестве параметров передаем экземпляр драйвера и url адрес
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout) # добавим команду для неявного ожидания со значением по умолчанию в 10


    def open(self): # открыть ссылку в браузере
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def is_not_element_present(self, how, what, timeout=4): # проверяет, что элемент не появляется на странице в течение заданного времени (упадет, как только увидит искомый элемент)
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=4): #проверить, что элемент исчезает (будет ждать до тех пор, пока элемент не исчезнет)
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK_INVALID) #надо использовать LOGIN_LINK, чтоб не падал тест test_guest_can_go_to_login_page_from_product_page
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def go_to_basket_page(self): # (self) чтобы иметь доступ к атрибутам и методам класса
        basket_link = self.browser.find_element(*MainPageLocators.BASKET_LINK) # Так как браузер хранится как аргумент класса BasePage, обращаться к нему нужно с помощью self
        basket_link.click()

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"