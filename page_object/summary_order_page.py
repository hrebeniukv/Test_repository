from selenium.webdriver.common.by import By

from page_object.syccessful_page import SuccessfulPage
from utilities.decorators import auto_steps
from utilities.web_ui.base_page import BasePage


@auto_steps
class SummaryOrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __create_order_button = (By.XPATH, '//button[contains(@class, "checkout")]')

    def click_create_order_button(self):
        self._click(self.__create_order_button)
        return SuccessfulPage(self._driver)
