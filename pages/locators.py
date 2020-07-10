from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.ID, "login_link")


class LoginPageLocators:
    LOGIN_BUTTON = (By.NAME, "login_submit")
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class BookPageLocators:
    ADD_IN_BUCKET_BUTTON = (By.CSS_SELECTOR, "[class='btn btn-lg btn-primary btn-add-to-basket']")
    BOOK_NAME = (By.XPATH, "//div[contains(@class, 'product_main')]/h1")
    BOOK_NAME_AFTER_ADDED = (By.XPATH, "//div[@id='messages']/div[1]/div/strong")

