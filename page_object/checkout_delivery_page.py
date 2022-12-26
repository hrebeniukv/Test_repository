from selenium.webdriver.common.by import By

from page_object.summary_order_page import SummaryOrderPage
from utilities.decorators import auto_steps
from utilities.web_ui.base_page import BasePage


@auto_steps
class CheckoutDeliverPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    __next_button = (By.XPATH, '//button[contains(@class, "continue")]')
    __payment_checkbox = (By.XPATH, '//input[@value = "flatrate_flatrate"]')

    def click_next_button(self):
        self._click(self.__next_button)
        return SummaryOrderPage(self._driver)

    def check_payment(self):
        self._check_radio_button(self.__payment_checkbox)
        return self
