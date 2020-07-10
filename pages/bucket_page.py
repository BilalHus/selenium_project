from .base_page import BasePage
from .locators import BucketPageLocators


class BucketPage(BasePage):

    def bucket_is_empty(self):
        assert self.is_not_element_present(*BucketPageLocators.GOODS_LIST), "Goods list is available"
        assert self.is_element_present(*BucketPageLocators.EMPTY_BUCKET_MESSAGE), "Empty message is not available"
