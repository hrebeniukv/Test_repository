from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select


class BasePage:
    def __init__(self, driver):
        self._driver = driver
        self.__waiter = WebDriverWait(driver, 10)

    def __wait_until_element_clikable(self, locator):
        return self.__waiter.until(EC.element_to_be_clickable(locator))

    def __wait_until_element_visible(self, locator):
        return self.__waiter.until(EC.visibility_of_element_located(locator))

    def __wait_until_element_located(self, locator):
        return self.__waiter.until(EC.presence_of_element_located(locator))

    def _click(self, locator):
        element = self.__wait_until_element_clikable(locator)
        element.click()

    def _is_visible(self, locator):
        try:
            self.__wait_until_element_visible(locator)
            return True
        except TimeoutException:
            return False

    def _is_clikable(self, locator):
        try:
            self.__wait_until_element_clikable(locator)
            return True
        except TimeoutException:
            return False

    def _send_keys(self, locator, value):
        element = self.__wait_until_element_located(locator)
        element.clear()
        element.send_keys(value)

    def _get_field_value(self, locator, value):
        element = self.__wait_until_element_located(locator)
        return element.get_attribute(value)

    def _get_element_text(self, locator):
        element = self.__wait_until_element_visible(locator)
        return element.text

    def _get_element_text2(self, locator):
        element = self.__wait_until_element_located(locator)
        return element.text

    def _select_element_by_value(self, locator, value):
        element = self.__wait_until_element_visible(locator)
        selector = Select(element)
        selector.select_by_value(value)

    def back_to_previously_page(self):
        return self._driver.back()

    def _select_element_by_text(self, locator, text):
        element = self.__wait_until_element_visible(locator)
        selector = Select(element)
        selector.select_by_visible_text(text)

    def _check_radio_button(self, locator):
        radio_button = self.__wait_until_element_visible(locator)
        if not radio_button.is_selected():
            radio_button.click()
