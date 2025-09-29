from pages.home_page import HomePage
from pages.login_page import LoginPage

def test_login_success(page):
    home = HomePage(page)
    home.open()
    home.dismiss_popups()

    login = LoginPage(page)
    login.open()
    login.login("admin@juice-sh.op", "admin123")


