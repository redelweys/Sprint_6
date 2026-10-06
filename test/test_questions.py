import allure
import pytest

from data import Urls, QuestionData
from pages.main_page import MainPage


class TestQuestions:

    @allure.title(
        'При раскрытии вопроса с индексом {question_index} '
        'отображается правильный ответ'
    )
    @pytest.mark.parametrize(
        'question_index, expected_answer',
        QuestionData.ANSWERS
    )
    def test_question_answer(self, questions_page, question_index, expected_answer):
        questions_page.open_question(question_index)

        assert questions_page.get_answer_text(question_index) == expected_answer