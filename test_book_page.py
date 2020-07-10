import time

from .pages.book_page import BookPage

#link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"


def test_book_should_be_added_to_bucket(browser):
    page = BookPage(browser, link)
    page.open()
    page.add_in_bucket()
    page.solve_quiz_and_get_code()
    page.verify_book_is_added()

