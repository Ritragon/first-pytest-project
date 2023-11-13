from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_add_to_basket_btn(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_BUTTON), "Add to basket button isn't presented"
    def add_to_cart_button(self):
        basket = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket.click()
    def message_product_to_name(self):
        name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        basket_name = self.browser.find_element(*ProductPageLocators.BASKET_NAME).text
        assert name == basket_name, "Product name not found on message"
    def message_product_to_price(self):
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_NAME).text
        assert price == basket_price, "Product price not found on message"