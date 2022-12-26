from selenium.webdriver.common.by import By

from page_object.dashboard_page import DashboardPage
from utilities.decorators import auto_steps
from utilities.web_ui.base_page import BasePage


@auto_steps
class RegisterPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __submit_form_button = (By.XPATH, '//button[@type="submit"and contains(@class,"action submit primary")]')
    __name_input = (By.XPATH, '//div[@class="control"]/input[@name="firstname"]')
    __last_name_input = (By.XPATH, '//div[@class="control"]/input[@name="lastname"]')
    __email_input = (By.XPATH, '//div[@class="control"]/input[@name="email"]')
    __password_input = (By.XPATH, '//fieldset//input[@name="password"]')
    __password_confirmation_input = (By.XPATH, '//fieldset//input[@name="password_confirmation"]')
    __show_password_checkbox = (By.XPATH, '//fieldset//input[@name="show-password"]')
    __information_tooltip = (By.XPATH, '//span[contains(@class ,"field-tooltip-action")]')

    __name_error_message = (By.XPATH, '//div[@id="firstname-error"]')
    __last_name_error_message = (By.XPATH, '//div[@id="lastname-error"]')
    __email_error_message = (By.XPATH, '//div[@id="email_address-error"]')
    __password_error_message = (By.XPATH, '//div[@id="password-error"]')
    __password_confirmation_error_message = (By.XPATH, '//div[@id="password-confirmation-error"]')

    def is_visible_submit_button(self):
        return self._is_visible(self.__submit_form_button)

    def set_name(self, name):
        self._send_keys(self.__name_input, name)
        return self

    def set_last_name(self, last_name):
        self._send_keys(self.__last_name_input, last_name)
        return self

    def set_email(self, email):
        self._send_keys(self.__email_input, email)
        return self

    def set_password(self, password):
        self._send_keys(self.__password_input, password)
        return self

    def set_password_confirmation(self, password):
        self._send_keys(self.__password_confirmation_input, password)
        return self

    def click_submit_button(self):
        self._click(self.__submit_form_button)

    def register_new(self, name, last_name, email, password):
        self.set_name(name).set_last_name(last_name).set_email(email).set_password(password).set_password_confirmation(
            password).click_submit_button()
        return DashboardPage(self._driver)

    def get_data_password_field(self):
        type_field = self._get_field_value(self.__password_input, 'type')
        return True if type_field == 'password' else False

    def show_password(self):
        self._click(self.__show_password_checkbox)
        return self

    def show_info_message(self):
        self._click(self.__information_tooltip)
        is_visible_message = self._get_field_value(self.__information_tooltip, 'aria-expanded')
        return True if is_visible_message == 'true' else False
