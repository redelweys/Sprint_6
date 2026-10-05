import allure
import pytest
from selenium import webdriver

from data import Urls, OrderData
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrder:

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()

        main_page = MainPage(cls.driver)
        main_page.open_page(Urls.MAIN_PAGE)
        main_page.accept_cookies()

    @allure.title(
        'Успешное оформление заказа через кнопку {button_position}'
    )
    @pytest.mark.parametrize(
        'button_position, order_data',
        OrderData.ORDERS,
        ids=['top_button', 'bottom_button']
    )
    def test_order_success(self, button_position, order_data):
        main_page = MainPage(self.driver)
        main_page.open_page(Urls.MAIN_PAGE)
        main_page.click_order_button(button_position)

        order_page = OrderPage(self.driver)
        order_page.fill_customer_data(order_data)
        order_page.fill_rental_data(order_data)
        order_page.submit_order()

        assert OrderData.SUCCESS_MESSAGE in order_page.get_success_message()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()