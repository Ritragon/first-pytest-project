from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "div.basket-mini a.btn.btn-default")


class BasketPageLocators:
    BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner > p")


class LoginPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class MainPageLocators:
    pass


class ProductPageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".price_color")
    BASKET_NAME = (By.CSS_SELECTOR, "div.alert:nth-child(1) > div:nth-child(2) > strong:nth-child(1)")
    BASKET_PRICE = (By.CSS_SELECTOR, "div.alert:nth-child(3) > div:nth-child(2) > p:nth-child(1) > strong:nth-child(1)")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")
