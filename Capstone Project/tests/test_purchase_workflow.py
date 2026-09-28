# Runs the complete customer journey: login, search, add to cart, update quantity, and verify details. (main execution file)
import pytest

from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.search_page import SearchPage
from utils.config import settings
from utils.data_reader import read_excel, read_json
from utils.helpers import accept_alert_if_present, capture_screenshot


@pytest.mark.e2e
def test_customer_can_search_add_and_update_cart(driver): #Pytest starts from this test function
    json_data = read_json()
    excel_data = read_excel()
    assert json_data["product"] == excel_data["product"], "JSON and Excel product data differ"
    # Credentials: prefer environment variables, fall back to JSON seed account
    email = settings.email or json_data.get("account", {}).get("email")
    password = settings.password or json_data.get("account", {}).get("password")
    assert email and password, "No credentials found; set DEMO_EMAIL/DEMO_PASSWORD or add account to data/test_data.json"

    home = HomePage(driver, settings.timeout)
    home.open(settings.base_url)
    home.go_to_login()
    LoginPage(driver, settings.timeout).login(email, password)
    capture_screenshot(driver, "logged_in")

    home.search(excel_data["product"])
    search = SearchPage(driver, settings.timeout)
    search.add_first_result_to_cart()
    accept_alert_if_present(driver)
    capture_screenshot(driver, "product_added")

    search.open_cart()
    cart = CartPage(driver, settings.timeout)
    cart.update_quantity(excel_data["quantity"])
    accept_alert_if_present(driver)
    details = cart.details()
    capture_screenshot(driver, "cart_verified")

    assert excel_data["product"].lower() in details["name"].lower()
    assert details["quantity"] == excel_data["quantity"]
    assert details["line_total"] == details["unit_price"] * details["quantity"]
