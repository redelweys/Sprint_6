from selenium.webdriver.common.by import By


class HeaderLocators:
    SCOOTER_LOGO = (
        By.XPATH,
        '//a[.//img[@alt="Scooter"]]'
    )
    YANDEX_LOGO = (
        By.XPATH,
        '//a[.//img[@alt="Yandex"]]'
    )