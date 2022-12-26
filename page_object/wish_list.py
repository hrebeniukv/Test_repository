from selenium.webdriver.common.by import By

from utilities.decorators import auto_steps
from utilities.web_ui.base_page import BasePage


@auto_steps
class WishList(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __actual_wish_list_button = (By.XPATH, '//button[@class="action update"]')

    def is_visible_button(self):
        return self._is_visible(self.__actual_wish_list_button)
