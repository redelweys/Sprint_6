import pytest
from selenium import webdriver
from data import Urls
from pages.main_page import MainPage


@pytest.fixture(scope='class')
def questions_page(questions_driver):
    page = MainPage(questions_driver)
    page.open_page(Urls.MAIN_PAGE)
    page.accept_cookies()
    return page


@pytest.fixture
def driver(request):
    browser = webdriver.Firefox()
    request.addfinalizer(browser.quit)
    browser.maximize_window()

    return browser

@pytest.fixture(scope='class')
def questions_driver():
    browser = webdriver.Firefox()
    browser.maximize_window()
    yield browser
    browser.quit()

@pytest.fixture(scope='class')
def questions_page(questions_driver):
    page = MainPage(questions_driver)
    page.open_page(Urls.MAIN_PAGE)
    page.accept_cookies()
    return page