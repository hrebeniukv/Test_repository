from selenium.webdriver.common.by import By

from utilities.decorators import auto_steps
from utilities.web_ui.base_page import BasePage


@auto_steps
class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __promo_section = (By.XPATH, '//div[@class = "blocks-promo"]')
    __product_in_carousel = (By.XPATH, '//ol/li[1]//a')

    def is_visible_promo_section(self):
        return self._is_visible(self.__promo_section)

    def go_to_pdp(self):
        self._click(self.__product_in_carousel)
