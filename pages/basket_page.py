from pages.base_page import BasePage
from pages.locators import BasketPageLocators

EMPTY_BASKET_MESSAGES = {
    "en": "Your basket is empty. Continue shopping",
    "ru": "Ваша корзина пуста Продолжить покупки",
    "fr": "Votre panier est vide. Continuer ses achats",
    "es": "Tu carrito esta vacío. Continuar sus compras",
}


class BasketPage(BasePage):

    def basket_should_be_empty(self, user_language):
        basket_massege = self.browser.find_element(*BasketPageLocators.BASKET_TEXT).text.strip()
        empty_message = EMPTY_BASKET_MESSAGES[user_language]
        assert basket_massege == empty_message, "Basket not empty"
