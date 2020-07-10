from .base_page import BasePage
from .locators import BookPageLocators


class BookPage(BasePage):

    def add_in_bucket(self):
        element = self.browser.find_element(*BookPageLocators.ADD_IN_BUCKET_BUTTON)
        element.click()

    def find_book_name(self):
        return self.browser.find_element(*BookPageLocators.BOOK_NAME).text

    def find_book_name_after_added(self):
        return self.browser.find_element(*BookPageLocators.BOOK_NAME_AFTER_ADDED).text

    def verify_book_is_added(self):
        assert self.find_book_name() == self.find_book_name_after_added(), "Book was not added"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*BookPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_not_disappear_success_message(self):
        assert not self.is_disappeared(*BookPageLocators.SUCCESS_MESSAGE), \
            "Success message did not disappear"
