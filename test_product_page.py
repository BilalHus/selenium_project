import pytest

from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage

links = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param(
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                      marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"]


@pytest.mark.need_review
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_in_basket()
    page.verify_product_is_added()


@pytest.mark.need_review
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"])
def test_user_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_in_basket()
    page.verify_product_is_added()


@pytest.mark.need_review
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"])
def test_guest_can_go_to_login_page_from_product_page(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"])
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.is_empty()


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_in_basket()
    page.should_not_be_success_message()


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])
def test_guest_cant_see_success_message(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_in_basket()
    page.should_not_disappear_success_message()


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"])
def test_guest_should_see_login_link_on_product_page(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
