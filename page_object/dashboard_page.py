from selenium.webdriver.common.by import By

from page_object.adress_data_page import AddressDataPage
from page_object.cart_page import CartPage
from page_object.order_details_page import OrderDetailsPage
from page_object.personal_data_page import PersonalDataPage
from utilities.decorators import auto_steps
from utilities.web_ui.base_page import BasePage


@auto_steps
class DashboardPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __contact_data = (By.XPATH, '//div[contains(@class, "box-information")]')
    __customer_name_last_name = (By.XPATH, '//div[contains(@class, "box-information")]//p[text()]')
    __change_information_data_button = (By.XPATH, '//div[contains(@class, "information")]//a/span')
    __reorder_button = (By.XPATH, '//a[@class ="action order"]/span')
    __change_address_data_button = (By.XPATH, '//div[contains(@class ,"shipping")]//div[@class = "box-actions"]/a')
    __billing_address = (By.XPATH, '//div[contains(@class, "billing")]/div')
    __last_order_number = (By.XPATH, '//tr[1]/td[1]')
    __show_order_button = (By.XPATH, '//table[contains(@class, "order")]//tr[1]//a[@class="action view"]')

    def is_visible_customer_information(self):
        return self._is_visible(self.__contact_data)

    def click_change_information_button(self):
        self._click(self.__change_information_data_button)
        return PersonalDataPage(self._driver)

    def get_customer_data(self):
        customer_name = self._get_element_text(self.__customer_name_last_name).split()
        return f'{customer_name[0]} {customer_name[1]}'

    def click_reorder_button(self):
        self._click(self.__reorder_button)
        return CartPage(self._driver)

    def click_change_address_data_button(self):
        self._click(self.__change_address_data_button)
        return AddressDataPage(self._driver)

    def get_billing_address(self):
        billing_address = self._get_element_text(self.__billing_address)
        return billing_address

    def get_last_order_number(self):
        last_order_number = self._get_element_text2(self.__last_order_number)
        return last_order_number

    def show_order_details_page(self):
        self._click(self.__show_order_button)
        return OrderDetailsPage(self._driver)

