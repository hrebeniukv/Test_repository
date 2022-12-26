import pytest

from utilities.config_parser import ReadConfig
from utilities.feke_data import FakeData


@pytest.mark.sanity
def test_rigister_new_customer(open_register_page, config_data):
    localization = config_data.fake_data['localization']
    name = FakeData.get_name(localization)
    last_name = FakeData.get_last_name(localization)
    email = FakeData.get_email(name)
    password = FakeData.get_password()
    register_page = open_register_page
    dashboard_page = register_page.register_new(name, last_name, email, password)
    assert dashboard_page.is_visible_customer_information() is True, "The new account haven' beem created"


@pytest.mark.regresion
def test_protected_password_field(open_register_page, config_data):
    register_page = open_register_page
    fild_data = register_page.set_password(config_data.user_data['password']).get_data_password_field()
    assert fild_data is True, 'The password field has text format'


@pytest.mark.regresion
def test_protected_password_confirmation_field(open_register_page, config_data):
    register_page = open_register_page
    fild_data = register_page.set_password_confirmation(config_data.user_data['password']).get_data_password_field()
    assert fild_data is True, 'The password field has text format'


@pytest.mark.regresion
def test_show_password(open_register_page,config_data):
    register_page = open_register_page
    password_field = register_page.set_password(config_data.user_data['password']).show_password().get_data_password_field()
    assert password_field is False, 'Password is not visible after checking checkbox'


@pytest.mark.regresion
def test_visible_information_message(open_register_page):
    register_page = open_register_page
    is_message = register_page.show_info_message()
    assert is_message is True, 'The message hasn\'t appeared'
