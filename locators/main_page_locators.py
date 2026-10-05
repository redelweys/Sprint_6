from selenium.webdriver.common.by import By


class MainPageLocators:
    COOKIE_BUTTON = (By.ID, 'rcc-confirm-button')
    QUESTION = (By.ID, 'accordion__heading-{}')
    ANSWER = (By.ID, 'accordion__panel-{}')

    ORDER_BUTTONS = {
        'top': (
            By.XPATH,
            '//div[contains(@class, "Header_Nav")]//button[text()="Заказать"]'
        ),
        'bottom': (
            By.XPATH,
            '//div[contains(@class, "Home_FinishButton")]//button[text()="Заказать"]'
        )
    }