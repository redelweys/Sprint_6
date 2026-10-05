from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)

    def find_element_with_wait(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )

    def click_element(self, locator):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        ).click()

    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )

    def get_element_text(self, locator):
        return self.find_element_with_wait(locator).text

    def enter_text(self, locator, text):
        element = self.find_element_with_wait(locator)
        element.clear()
        element.send_keys(text)

    def get_url_after_redirect(self, expected_url):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.url_contains(expected_url)
            )
        except TimeoutException:
            raise AssertionError(
                f'Ожидался переход на {expected_url}, '
                f'но текущий адрес: {self.driver.current_url}'
            )

        return self.driver.current_url