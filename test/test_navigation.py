import allure
from selenium import webdriver

from data import Urls
from pages.header_page import HeaderPage


class TestNavigation:

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()

    @allure.title('Логотип Самоката возвращает на главную страницу')
    def test_scooter_logo_opens_main_page(self):
        header_page = HeaderPage(self.driver)
        header_page.open_page(Urls.ORDER_PAGE)

        header_page.click_scooter_logo()

        assert (
            header_page.get_url_after_redirect(Urls.MAIN_PAGE)
            == Urls.MAIN_PAGE
        )

    @allure.title('Логотип Яндекса открывает Дзен в новой вкладке')
    def test_yandex_logo_opens_dzen(self):
        header_page = HeaderPage(self.driver)
        header_page.open_page(Urls.ORDER_PAGE)

        header_page.click_yandex_logo_and_switch()

        assert (
            header_page.get_url_after_redirect(Urls.DZEN_PAGE).split('?')[0]
            == Urls.DZEN_PAGE
        )

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()