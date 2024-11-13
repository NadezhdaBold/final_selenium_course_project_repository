import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from  .base_page import BasePage
from .locators import MainPageLocators
from .login_page import LoginPage

class MainPage(BasePage): # добавляем класс MainPage, который наследует все методы и атрибуты предка BasePage
    def go_to_login_page(self): # (self) чтобы иметь доступ к атрибутам и методам класса
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK) # Так как браузер хранится как аргумент класса BasePage, обращаться к нему нужно с помощью self
        login_link.click()
        alert = self.browser.switch_to.alert
        alert.accept()

    def should_be_login_link(self): # метод, проверяющий наличие ссылки
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs) #super вызывает конструктор класса предка и передает ему все те аргументы, которые мы передали в конструктор MainPage
