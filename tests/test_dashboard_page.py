import pytest


@pytest.mark.sanity
def test_change_personal_data(login, config_data):
    localization = config_data.fake_data["localization"]
    dashboard_page = login
    personal_data_before_changes = dashboard_page.get_customer_data()
    personal_data_page = dashboard_page.click_change_information_button()
    personal_data_page.set_first_name(localization).set_last_name(localization).click_summit_button()
    personal_data_after_changes = dashboard_page.get_customer_data()
    assert personal_data_before_changes != personal_data_after_changes, 'The name and last name haven\'t been change'


@pytest.mark.sanity
def test_reorder_button(open_cart_page):
    cart_page = open_cart_page
    is_checkout_button = cart_page.is_checkout_button_clickable()
    cart_page.remove_first_product()
    assert is_checkout_button is True, 'The re-order button is not clickable'


@pytest.mark.sanity
def test_change_address(login, config_data):
    localization = config_data.fake_data["localization"]
    dashboard_page = login
    billing_address_before = dashboard_page.get_billing_address()
    dashboard_page.click_change_address_data_button().set_first_name(localization).set_last_name(
        localization).set_phone_number(localization).set_address_input(localization).select_country(
        localization).select_region(localization).set_city(localization).set_post_code(localization).click_save_button()
    billing_address_after = dashboard_page.get_billing_address()
    assert billing_address_after != billing_address_before, 'New address doesn\'t set'


@pytest.mark.regresion
def test_if_visible_last_number(login):
    dashboard_page = login
    cart_page = dashboard_page.click_reorder_button()
    checkout_delivery_page = cart_page.click_checkout_button()
    summary_order_page = checkout_delivery_page.check_payment().click_next_button()
    successful_page = summary_order_page.click_create_order_button()
    order_nuber_on_successful_page = successful_page.get_order_number()
    successful_page.open_nav_menu().navigate_to_dashboard()
    last_order_number_in_dashboard = dashboard_page.get_last_order_number()
    assert order_nuber_on_successful_page == last_order_number_in_dashboard, "Order number is\'t display in dashboard"


@pytest.mark.sanity
def test_show_order_data(login):
    dashboard_page = login
    order_number_dashboard = dashboard_page.get_last_order_number()
    order_details_page = login.show_order_details_page()
    order_number_on_detail_page = order_details_page.get_order_number()
    assert order_number_dashboard == order_number_on_detail_page, "Problem with redirection detail page"

