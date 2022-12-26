import random

from selenium.webdriver.common.by import By

from page_object.wish_list import WishList
from utilities.decorators import auto_steps
from utilities.web_ui.base_page import BasePage


@auto_steps
class PDP(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __product_name = (By.XPATH, '//span[@class="base"]')
    __l_size_button = (By.XPATH, '//div[@aria-label = "L"]')
    __selected_size = (By.XPATH, '//div[contains(@class, "size")]/span[@class = "swatch-attribute-selected-option"]')
    __blue_color_button = (By.XPATH, '//div[@class = "swatch-option color"][1]')
    __selected_color = (By.XPATH, '//div[contains(@class, "color")]/span[@class = "swatch-attribute-selected-option"]')
    __add_to_wishlist = (By.XPATH, '//a[contains(@class, "towishlist")]')
    __compare_button = (By.XPATH, '//a[contains(@class, "tocompare")]')
    __compare_product_link = (By.XPATH, '//li[contains(@class, "compare")]')
    __qty_input = (By.XPATH, '//div[@class="field qty"]//input[contains(@class, "qty")]')
    __add_to_cart_button = (By.XPATH, '//button[contains(@class, "tocart")]')
    __cart = (By.XPATH, '//span[@class = "counter-number"]')
    __product_count = (By.XPATH, '//span[@class = "count"]')

    def get_product_name(self):
        return self._get_element_text(self.__product_name)

    def go_back_to_cart(self):
        self.back_to_previously_page()

    def set_size(self):
        self._click(self.__l_size_button)
        return self._get_element_text(self.__l_size_button)

    def set_selected_size(self):
        return self._get_element_text(self.__selected_size)

    def is_match_selected_to_actual(self, expected, actual):
        if expected == actual:
            return True
        return False

    def set_color(self):
        color = self._get_field_value(self.__blue_color_button, 'aria-label')
        self._click(self.__blue_color_button)
        return color

    def get_selected_color(self):
        return self._get_element_text(self.__selected_color)

    def click_add_to_wishlist(self):
        self._click(self.__add_to_wishlist)
        return WishList(self._driver)

    def click_compare_button(self):
        self._click(self.__compare_button)
        return self

    def is_visible_compare_product_link(self):
        return self._is_visible(self.__compare_product_link)

    def set_qty(self):
        self._send_keys(self.__qty_input, random.randint(2, 5))
        return self

    def click_add_to_cart_button(self):
        self._click(self.__add_to_cart_button)
        return self

    def open_minicart(self):
        self._click(self.__cart)
        return self

    def get_set_qty(self):
        qty = self._get_field_value(self.__qty_input, 'value')
        return float(qty)

    def get_qty(self):
        qty = self._get_element_text(self.__product_count)
        return float(qty)

    def is_correct_qty(self, set_qty, qty_in_cart):
        if qty_in_cart >= set_qty:
            return True
        else:
            return False
