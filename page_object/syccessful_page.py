from selenium.webdriver.common.by import By

from utilities.decorators import auto_steps
from utilities.web_ui.base_page import BasePage


@auto_steps
class SuccessfulPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __order_number = (By.XPATH, '//a[@class = "order-number"]')
    __navigate_button = (By.XPATH, '//div[contains(@class, "header")]//button[contains(@class , "switch")]')
    __dashboard = (By.XPATH, '//li[@class = "customer-welcome active"]//li[1]')

    def get_order_number(self):
        order_number = self._get_element_text(self.__order_number)
        return order_number

    def open_nav_menu(self):
        self._click(self.__navigate_button)
        return self

    def navigate_to_dashboard(self):
        self._click(self.__dashboard)
