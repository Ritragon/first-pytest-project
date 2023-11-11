from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart_button(self):
        basket = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket.click()
    def message_product_to_cart(self):
        assert self.is_element_present(*ProductPageLocators.)
