from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.GOODS_LIST), "Goods list is available"
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), "Empty message is not available"
