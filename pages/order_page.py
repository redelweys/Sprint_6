import allure

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step('Выбрать станцию метро: {station}')
    def select_metro(self, station):
        self.enter_text(OrderPageLocators.METRO, station)

        locator = (
            OrderPageLocators.METRO_OPTION[0],
            OrderPageLocators.METRO_OPTION[1].format(station)
        )
        self.click_element(locator)

    @allure.step('Заполнить данные получателя')
    def fill_customer_data(self, order_data):
        self.enter_text(OrderPageLocators.NAME, order_data['name'])
        self.enter_text(OrderPageLocators.SURNAME, order_data['surname'])
        self.enter_text(OrderPageLocators.ADDRESS, order_data['address'])
        self.select_metro(order_data['metro'])
        self.enter_text(OrderPageLocators.PHONE, order_data['phone'])
        self.click_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Указать дату доставки: {delivery_date}')
    def set_delivery_date(self, delivery_date):
        self.enter_text(OrderPageLocators.DELIVERY_DATE, delivery_date)
        self.click_element(OrderPageLocators.RENTAL_TITLE)

    @allure.step('Выбрать срок аренды: {period}')
    def select_rental_period(self, period):
        self.click_element(OrderPageLocators.RENTAL_PERIOD)

        locator = (
            OrderPageLocators.RENTAL_PERIOD_OPTION[0],
            OrderPageLocators.RENTAL_PERIOD_OPTION[1].format(period)
        )
        self.click_element(locator)

    @allure.step('Выбрать цвет самоката: {color}')
    def select_color(self, color):
        locator = (
            OrderPageLocators.COLOR[0],
            OrderPageLocators.COLOR[1].format(color)
        )
        self.click_element(locator)

    @allure.step('Заполнить параметры аренды')
    def fill_rental_data(self, order_data):
        self.set_delivery_date(order_data['delivery_date'])
        self.select_rental_period(order_data['rental_period'])
        self.select_color(order_data['color'])
        self.enter_text(OrderPageLocators.COMMENT, order_data['comment'])

    @allure.step('Оформить и подтвердить заказ')
    def submit_order(self):
        self.click_element(OrderPageLocators.ORDER_BUTTON)
        self.click_element(OrderPageLocators.CONFIRM_BUTTON)

    @allure.step('Получить сообщение об успешном оформлении заказа')
    def get_success_message(self):
        return self.get_element_text(OrderPageLocators.SUCCESS_TITLE)