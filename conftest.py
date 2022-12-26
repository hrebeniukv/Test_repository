import json
from contextlib import suppress

import allure
import pytest

from CONSTANS import ROOT_DIR
from page_object.home_page import HomePage
from page_object.login_page import LoginPage
from page_object.product_detais_page import PDP
from page_object.register_page import RegisterPage
from utilities.configuration import Configuration
from utilities.driver_factory import DriverFactory


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture()
def create_driver(config_data, request):
    driver = DriverFactory.create_driver(driver_id=config_data.browser_data['browser_id'])
    driver.maximize_window()
    yield driver
    if request.node.rep_call.failed:
        with suppress(Exception):
            allure.attach(driver.get_screenshot_as_png(), name=request.function.__name__,
                          attachment_type=allure.attachment_type.PNG)
    driver.quit()


@pytest.fixture(scope='session')
def config_data():
    with open(f'{ROOT_DIR}/configurations/configuration.json') as f:
        data = f.read()
        json_to_dict = json.loads(data)
    config = Configuration(**json_to_dict)
    return config


@pytest.fixture()
def open_login_page(create_driver, config_data: Configuration):
    create_driver.get(f"{config_data.app_info['base_url']}{config_data.app_info['login_page_endpoint']}")
    return LoginPage(create_driver)


@pytest.fixture()
def open_register_page(create_driver, config_data):
    create_driver.get(f"{config_data.app_info['base_url']}{config_data.app_info['register_page_endpoint']}")
    return RegisterPage(create_driver)


@pytest.fixture()
def login(open_login_page, config_data):
    return open_login_page.login(config_data.user_data['email'], config_data.user_data['password'])


@pytest.fixture()
def open_cart_page(login):
    dashboard_page = login
    return dashboard_page.click_reorder_button()


@pytest.fixture()
def open_pdp(login, create_driver, config_data):
    create_driver.get(config_data.app_info['base_url'])
    HomePage(create_driver).go_to_pdp()
    return PDP(create_driver)