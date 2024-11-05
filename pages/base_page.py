import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class BasePage():
    def __init__(self, browser, url):  # конструктор в качестве параметров передаем экземпляр драйвера и url адрес
        self.browser = browser
        self.url = url

    def open(self): # открыть ссылку в браузере
        self.browser.get(self.url)