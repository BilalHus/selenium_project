from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_in_basket(self):
        element = self.browser.find_element(*ProductPageLocators.ADD_IN_BASKET_BUTTON)
        element.click()

    def find_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def find_product_name_after_added(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_AFTER_ADDED).text

    def verify_product_is_added(self):
        assert self.find_product_name() == self.find_product_name_after_added(), "Product was not added"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_not_disappear_success_message(self):
        assert not self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message did not disappear"
