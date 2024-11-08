import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

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