from selenium.webdriver.common.by import By

from utilities.decorators import auto_steps
from utilities.feke_data import FakeData
from utilities.web_ui.base_page import BasePage


@auto_steps
class PersonalDataPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __first_name_input = (By.XPATH, '//input[@name="firstname"]')
    __last_name_input = (By.XPATH, '//input[@name="lastname"]')
    __submit_button = (By.XPATH, '//button[contains(@class,"save")]')

    def set_first_name(self, localization):
        self._send_keys(self.__first_name_input, FakeData.get_name(localization))
        return self

    def set_last_name(self, localization):
        self._send_keys(self.__last_name_input, FakeData.get_last_name(localization))
        return self

    def click_summit_button(self):
        self._click(self.__submit_button)
