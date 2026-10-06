import allure
import pytest

from data import Urls, OrderData
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrder:

    @allure.title(
        'Успешное оформление заказа через кнопку {button_position}'
    )
    @pytest.mark.parametrize(
        'button_position, order_data',
        OrderData.ORDERS,
        ids=['top_button', 'bottom_button']
    )
    def test_order_success(self, driver, button_position, order_data):
        main_page = MainPage(driver)
        main_page.open_page(Urls.MAIN_PAGE)
        main_page.accept_cookies()
        main_page.click_order_button(button_position)

        order_page = OrderPage(driver)
        order_page.fill_customer_data(order_data)
        order_page.fill_rental_data(order_data)
        order_page.submit_order()

        assert OrderData.SUCCESS_MESSAGE in order_page.get_success_message()