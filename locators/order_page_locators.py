from selenium.webdriver.common.by import By


class OrderPageLocators:
    NAME = (By.XPATH, '//input[@placeholder="* Имя"]')
    SURNAME = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    ADDRESS = (
        By.XPATH,
        '//input[@placeholder="* Адрес: куда привезти заказ"]'
    )
    METRO = (By.XPATH, '//input[@placeholder="* Станция метро"]')
    METRO_OPTION = (
        By.XPATH,
        '//button[contains(@class, "select-search__option")]'
        '[.//div[text()="{}"]]'
    )
    PHONE = (
        By.XPATH,
        '//input[@placeholder="* Телефон: на него позвонит курьер"]'
    )
    NEXT_BUTTON = (By.XPATH, '//button[text()="Далее"]')

    RENTAL_TITLE = (By.XPATH, '//div[text()="Про аренду"]')
    DELIVERY_DATE = (
        By.XPATH,
        '//input[@placeholder="* Когда привезти самокат"]'
    )
    RENTAL_PERIOD = (By.CLASS_NAME, 'Dropdown-control')
    RENTAL_PERIOD_OPTION = (
        By.XPATH,
        '//div[@class="Dropdown-option" and text()="{}"]'
    )
    COLOR = (By.ID, '{}')
    COMMENT = (
        By.XPATH,
        '//input[@placeholder="Комментарий для курьера"]'
    )
    ORDER_BUTTON = (
        By.XPATH,
        '//div[contains(@class, "Order_Buttons")]'
        '//button[text()="Заказать"]'
    )
    CONFIRM_BUTTON = (By.XPATH, '//button[text()="Да"]')
    SUCCESS_TITLE = (
        By.XPATH,
        '//div[contains(@class, "Order_ModalHeader")'
        ' and contains(., "Заказ оформлен")]'
    )