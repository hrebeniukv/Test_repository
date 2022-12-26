import pytest


@pytest.mark.sanity
def test_remove_product(open_cart_page):
    cart_page = open_cart_page
    cart_page.remove_first_product()
    assert cart_page.is_visible_continue_shopping_button() is True, 'Product hasn\'t been removed'


@pytest.mark.regresion
def test_continue_shopping(open_cart_page):
    cart_page = open_cart_page
    home_page = cart_page.remove_first_product().click_continue_shopping_button()
    assert home_page.is_visible_promo_section() is True, 'The button doesn\'t redirect to theHome page'


@pytest.mark.sanity
def test_move_product_to_wishlist(open_cart_page):
    cart_page = open_cart_page
    cart_page.click_to_wishlist_button()
    assert cart_page.is_visible_continue_shopping_button() is True, 'The product hanb\' remow=ve from the cart after move to wihlist'


@pytest.mark.sanity
def test_redirection_to_pdp(open_cart_page):
    cart_page = open_cart_page
    product_name_on_cart = cart_page.get_product_name()
    product_details_page = cart_page.click_on_product_name()
    product_name_on_pdp = product_details_page.get_product_name()
    product_details_page.go_back_to_cart()
    cart_page.remove_first_product()
    assert product_name_on_cart == product_name_on_pdp, "Redirect to the wrong page"


@pytest.mark.regresion
def test_change_product_qty(open_cart_page):
    cart_page = open_cart_page
    item_price = cart_page.get_item_price()
    product_qty = cart_page.set_qty().click_recalc_button().get_qty()
    total_product_price = cart_page.get_total_price_price()
    cart_page.remove_first_product()
    assert cart_page.is_correct_total_price(item_price, product_qty, total_product_price) is True, 'Wtrong total price'
