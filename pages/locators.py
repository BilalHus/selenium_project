from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class LoginPageLocators:
    LOGIN_BUTTON = (By.NAME, "login_submit")
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class BookPageLocators:
    ADD_IN_BUCKET_BUTTON = (By.CSS_SELECTOR, "[class='btn btn-lg btn-primary btn-add-to-basket']")
    BOOK_NAME = (By.XPATH, "//div[contains(@class, 'product_main')]/h1")
    BOOK_NAME_AFTER_ADDED = (By.XPATH, "//div[@id='messages']/div[1]/div/strong")
    SUCCESS_MESSAGE = (By.XPATH, "//div[@id='messages']/div[1]/div/strong")

