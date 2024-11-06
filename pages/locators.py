from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    FORM_LOGIN=(By.XPATH, '//form[@id="login_form"]')
    FORM_REGISTRATION = (By.XPATH, '//form[@id="register_form"]')

