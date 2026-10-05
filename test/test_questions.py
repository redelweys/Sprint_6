import allure
import pytest
from selenium import webdriver

from data import Urls, QuestionData
from pages.main_page import MainPage


class TestQuestions:

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()

        main_page = MainPage(cls.driver)
        main_page.open_page(Urls.MAIN_PAGE)
        main_page.accept_cookies()

    @allure.title(
        'При раскрытии вопроса с индексом {question_index} '
        'отображается правильный ответ'
    )
    @pytest.mark.parametrize(
        'question_index, expected_answer',
        QuestionData.ANSWERS
    )
    def test_question_answer(self, question_index, expected_answer):
        main_page = MainPage(self.driver)
        main_page.open_question(question_index)

        assert main_page.get_answer_text(question_index) == expected_answer

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()