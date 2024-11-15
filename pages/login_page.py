import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "'login' not in current url" # проверка, что есть в url есть слово login

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.FORM_LOGIN), "Login form is not presented" # проверка, что есть форма логина

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.FORM_REGISTRATION), "Registration form is not presented" # проверка, что есть форма регистрации

    def register_new_user(self, email, password):
        email_input=self.browser.find_element(*LoginPageLocators.EMAIL)
        email_input.send_keys(email)
        password_input=self.browser.find_element(*LoginPageLocators.PASSWORD)
        password_input.send_keys(password)
        password_input_repeat = self.browser.find_element(*LoginPageLocators.PASSWORD_REPEAT)
        password_input_repeat.send_keys(password)
        reg_button=self.browser.find_element(*LoginPageLocators.BUTTON_REGISTRATION)
        reg_button.click()


