import pytest


@pytest.mark.regresion
def test_select_size(open_pdp):
    pdp = open_pdp
    expected_size = pdp.set_size()
    actual_size = pdp.set_selected_size()
    assert pdp.is_match_selected_to_actual(expected_size, actual_size) is True, 'Expected size is not selected'


@pytest.mark.regresion
def test_select_color(open_pdp):
    pdp = open_pdp
    expected_color = pdp.set_color()
    actual_color = pdp.get_selected_color()
    assert pdp.is_match_selected_to_actual(expected_color, actual_color) is True, 'Expected size is not selected'


@pytest.mark.sanity
def test_add_to_wishlist(open_pdp):
    pdp = open_pdp
    wish_list = pdp.click_add_to_wishlist()
    assert wish_list.is_visible_button() is True, "You aren't redirectedto the wish list page"


@pytest.mark.sanity
def test_add_to_compare(open_pdp):
    pdp = open_pdp
    pdp.click_compare_button()
    assert pdp.is_visible_compare_product_link() is True, 'The compare products link is not visible'


# @pytest.mark.sanity
# def test_add_to_cart(open_pdp):
#     pdp = open_pdp
#     pdp.set_size()
#     pdp.set_color()
#     pdp.set_qty().click_add_to_cart_button()
#     actual_qty = pdp.open_minicart().get_qty()
#     set_qty = pdp.get_set_qty()
#     assert pdp.is_correct_qty(set_qty, actual_qty) is True, 'The product hasn\'t been added to the cart'
