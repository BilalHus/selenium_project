import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: ru or en")


@pytest.fixture(scope="function")
def browser(request):
    lang = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': "en" if lang is None else lang})
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()
