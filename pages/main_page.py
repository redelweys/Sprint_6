import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Закрыть уведомление о cookies')
    def accept_cookies(self):
        self.click_element(MainPageLocators.COOKIE_BUTTON)

    @allure.step('Раскрыть вопрос с индексом {question_index}')
    def open_question(self, question_index):
        locator = (
            MainPageLocators.QUESTION[0],
            MainPageLocators.QUESTION[1].format(question_index)
        )
        self.scroll_to_element(locator)
        self.click_element(locator)

    @allure.step('Получить ответ на вопрос с индексом {question_index}')
    def get_answer_text(self, question_index):
        locator = (
            MainPageLocators.ANSWER[0],
            MainPageLocators.ANSWER[1].format(question_index)
        )
        return self.get_element_text(locator)

    @allure.step('Нажать кнопку заказа: {button_position}')
    def click_order_button(self, button_position):
        locator = MainPageLocators.ORDER_BUTTONS[button_position]
        self.scroll_to_element(locator)
        self.click_element(locator)