from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK =(By.XPATH, '//a[@class="btn btn-default"]')

class LoginPageLocators():
    FORM_LOGIN=(By.XPATH, '//form[@id="login_form"]')
    FORM_REGISTRATION = (By.XPATH, '//form[@id="register_form"]')
    EMAIL=(By.XPATH, '//input[@name="registration-email"]')
    PASSWORD=(By.XPATH, '//input[@name="registration-password1"]')
    PASSWORD_REPEAT=(By.XPATH, '//input[@name="registration-password2"]')
    BUTTON_REGISTRATION=(By.XPATH, '//button[@name="registration_submit"]')

class ProductPageLocators():
    BASKET_BUTTON=(By.XPATH, '//button[@class="btn btn-lg btn-primary btn-add-to-basket"]')
    PRODUCT_NAME=(By.XPATH, '//div[@class="col-sm-6 product_main"]/h1')
    PRODUCT_PRICE=(By.XPATH, '//div[@class="col-sm-6 product_main"]/p[@class="price_color"]')
    ALERT_NAME=(By.XPATH,'//*[@id="messages"]/div[1]/div/strong')
    ALERT_PRICE=(By.XPATH,'//div[@class="alert alert-safe alert-noicon alert-info  fade in"]/div/p[1]/strong')
    ALERT_BASKET_ADD=(By.XPATH,'//div[@id="messages"]')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.XPATH, '//i[@class="icon-user"]')

class BasketPageLocators():
    EMPTY_BASKET=(By.XPATH, '//form[@id="basket_formset"]')
    BASKET_TEXT=(By.XPATH, '//div[@id="content_inner"]/p')


