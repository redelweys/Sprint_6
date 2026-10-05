import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.header_locators import HeaderLocators
from pages.base_page import BasePage


class HeaderPage(BasePage):

    @allure.step('Нажать на логотип Самоката')
    def click_scooter_logo(self):
        self.click_element(HeaderLocators.SCOOTER_LOGO)

    @allure.step('Нажать на логотип Яндекса и перейти в новую вкладку')
    def click_yandex_logo_and_switch(self):
        old_windows = self.driver.window_handles

        self.click_element(HeaderLocators.YANDEX_LOGO)

        WebDriverWait(self.driver, 10).until(
            EC.new_window_is_opened(old_windows)
        )

        for window in self.driver.window_handles:
            if window not in old_windows:
                self.driver.switch_to.window(window)
                break