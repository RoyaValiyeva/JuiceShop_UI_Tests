from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
from playwright.sync_api import expect

def test_add_to_basket(page):
    # Login via POM
    home = HomePage(page)
    home.open()
    home.dismiss_popups()

    login = LoginPage(page)
    login.open()
    login.login("admin@juice-sh.op", "admin123")

    # Add an item
    page.goto("http://localhost:3000/#/search?q=apple")
    first_add = page.get_by_role("button", name="Add to Basket").first
    expect(first_add).to_be_visible(timeout=10000)
    first_add.click()

    # Verify basket by state (not snackbar)
    basket = BasketPage(page)
    basket.open()
    assert basket.line_item_count() > 0
    basket.expect_checkout_visible()
