from selenium.webdriver.common.by import By

from page_object.dashboard_page import DashboardPage
from page_object.register_page import RegisterPage
from page_object.reset_password_page import ResetPasswordPage
from utilities.decorators import auto_steps
from utilities.web_ui.base_page import BasePage


@auto_steps
class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    __create_account_button = (By.XPATH, '//a[contains(@class, "action create primary")]')
    __reset_password_button = (By.XPATH, '//a[contains(@class, "action remind")]')
    __email_input = (By.XPATH, '//div[@class="control"]//input[@name="login[username]"]')
    __login_button = (By.XPATH, '//div[@class="primary"]/button[contains(@class,"login primary")]')
    __password_input = (By.XPATH, '//div[@class="control"]//input[@name="login[password]"]')
    __show_password_checkbox = (By.XPATH, '//div[@class="field choice"]//input[@type="checkbox"]')

    def click_create_account_button(self):
        self._click(self.__create_account_button)
        return RegisterPage(self._driver)

    def click_reset_password_button(self):
        self._click(self.__reset_password_button)
        return ResetPasswordPage(self._driver)

    def set_email(self, email):
        self._send_keys(self.__email_input, email)
        return self

    def set_password(self, password):
        self._send_keys(self.__password_input, password)
        return self

    def click_login_button(self):
        self._click(self.__login_button)

    def get_data_password_field(self):
        type_field = self._get_field_value(self.__password_input, 'type')
        return True if type_field == 'password' else False

    def show_password(self):
        self._click(self.__show_password_checkbox)
        return self

    def login(self, email, password):
        self.set_email(email).set_password(password).click_login_button()
        return DashboardPage(self._driver)
