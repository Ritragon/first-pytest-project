from pages.product_page import ProductPage
import pytest


@pytest.mark.parametrize('promo_offer', [pytest.param(num, marks=pytest.mark.xfail)for num in range(10)])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket_btn()
    page.add_to_cart_button()
    page.solve_quiz_and_get_code()
    page.message_product_to_name()
    page.message_product_to_price()
