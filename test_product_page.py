from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from mimesis import Person
import pytest


@pytest.mark.register_user
class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        register_page = LoginPage(browser, "http://selenium1py.pythonanywhere.com/ru/accounts/login/")
        register_page.open()
        email = Person().email()
        password = Person().password(length=10)
        register_page.register_new_user(email, password)

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.should_be_add_to_basket_btn()
        page.add_to_cart_button()
        page.success_message_product_to_name()
        page.total_should_be_equal_to_price()


@pytest.mark.need_review
@pytest.mark.parametrize('promo_offer', [pytest.param(num, marks=pytest.mark.xfail) for num in range(10)])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
    page = ProductPage(browser, link + f'{promo_offer}')
    page.open()
    page.should_be_add_to_basket_btn()
    page.add_to_cart_button()
    page.solve_quiz_and_get_code()
    page.success_message_product_to_name()
    page.total_should_be_equal_to_price()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser, user_language):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.click_basket_button()
    basket_form_page = BasketPage(browser, browser.current_url)
    basket_form_page.basket_should_be_empty(user_language)


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart_button()
    page.should_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.success_message_should_disappear()
