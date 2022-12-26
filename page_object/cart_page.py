from random import randint

from selenium.webdriver.common.by import By

from page_object.checkout_delivery_page import CheckoutDeliverPage
from page_object.home_page import HomePage
from page_object.product_detais_page import PDP
from utilities.decorators import auto_steps
from utilities.web_ui.base_page import BasePage


@auto_steps
class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __checkout_button = (By.XPATH, '//li[@class = "item"]/button[contains(@class ,"checkout")]')
    __remove_product_button = (By.XPATH, '//a[@class ="action action-delete"]')
    __continue_shopping_button = (By.XPATH, '//div[@class = "cart-empty"]//p/a')
    __to_wishlist_button = (By.XPATH, '//form[contains(@class, "form form-cart")]//a[contains(@class,"towishlist")]')
    __change_parameters_button = (By.XPATH, '//a[contains(@class,"action-edit")]')
    __first_product_name = (By.XPATH, '//tr[1]//strong[contains(@class,"name")]')
    __item_price = (By.XPATH, '//tr[1]//td[2]//span[@class = "price"]')
    __qty_input = (By.XPATH, '//tr[1]//td[3]//input[contains(@class , "qty")]')
    __total_product_price = (By.XPATH, '//tr[1]//td[4]//span[@class = "price"]')
    __recalc_button = (By.XPATH, '//button[@type= "submit" and @class ="action update"]')
    __summary = (By.XPATH, '//tr[@class="grand totals"]')

    def is_checkout_button_clickable(self):
        return self._is_clikable(self.__checkout_button)

    def remove_first_product(self):
        self._click(self.__remove_product_button)
        return self

    def click_checkout_button(self):
        if self._is_visible(self.__summary):
            self._click(self.__checkout_button)
            return CheckoutDeliverPage(self._driver)

    def is_visible_continue_shopping_button(self):
        return self._is_visible(self.__continue_shopping_button)

    def click_continue_shopping_button(self):
        self._click(self.__continue_shopping_button)
        return HomePage(self._driver)

    def click_to_wishlist_button(self):
        self._click(self.__to_wishlist_button)
        return self

    def click_on_product_name(self):
        self._click(self.__first_product_name)
        return PDP(self._driver)

    def get_product_name(self):
        return self._get_element_text(self.__first_product_name)

    def get_item_price(self):
        price = self._get_element_text(self.__item_price)
        return float(price[:-3].replace(",", "."))

    def set_qty(self):
        self._send_keys(self.__qty_input, randint(2, 5))
        return self

    def get_qty(self):
        qty = self._get_field_value(self.__qty_input, 'value')
        return float(qty)

    def click_recalc_button(self):
        self._click(self.__recalc_button)
        return self

    def get_total_price_price(self):
        if self._is_visible(self.__summary):
            price = self._get_element_text(self.__total_product_price)
            return float(price[:-3].replace(",", "."))

    def is_correct_total_price(self, item_price, qty, total_price):

        if item_price * qty != total_price:
            return False
        else:
            return True
