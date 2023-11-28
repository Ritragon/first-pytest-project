from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.basket_page import EMPTY_CART_MESSAGES
import pytest

# link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
# link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"


@pytest.mark.parametrize('promo_offer', [pytest.param(num, marks=pytest.mark.xfail) for num in range(10)])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    page = ProductPage(browser, link + f'{promo_offer}')
    page.open()
    page.should_be_add_to_basket_btn()
    page.add_to_cart_button()
    page.solve_quiz_and_get_code()
    page.message_product_to_name()
    page.message_product_to_price()
    page.should_not_be_success_message()
    page.success_message_should_disappear()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser, user_language):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.click_basket_button()
    basket_form_page = BasketPage(browser, browser.current_url)
    expected_message = EMPTY_CART_MESSAGES[user_language]
    basket_form_page.basket_should_be_empty(expected_message)


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart_button()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.is_disappeared()
