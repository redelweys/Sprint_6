import allure

from locators.header_locators import HeaderLocators
from pages.base_page import BasePage


class HeaderPage(BasePage):

    @allure.step('Нажать на логотип Самоката')
    def click_scooter_logo(self):
        self.click_element(HeaderLocators.SCOOTER_LOGO)

    @allure.step('Нажать на логотип Яндекса и перейти в новую вкладку')
    def click_yandex_logo_and_switch(self):
        old_windows = self.get_window_handles()

        self.click_element(HeaderLocators.YANDEX_LOGO)
        self.wait_for_new_window(old_windows)

        for window in self.get_window_handles():
            if window not in old_windows:
                self.switch_to_window(window)
                break