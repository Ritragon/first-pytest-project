from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import time


# link = "http://selenium1py.pythonanywhere.com/"
link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/"


def test_guest_should_see_login_link(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_should_see_login_form(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_form_page = LoginPage(browser, browser.current_url)
    login_form_page.should_be_login_form()


def test_guest_should_see_register_form(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    register_form_page = LoginPage(browser, browser.current_url)
    register_form_page.should_be_register_form()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser, user_language):
    page = MainPage(browser, link)
    page.open()
    page.click_basket_button()
    basket_form_page = BasketPage(browser, browser.current_url)
    basket_form_page.basket_should_be_empty(user_language)

