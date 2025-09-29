from pages.home_page import HomePage

def test_open_juice_shop(page):
    home = HomePage(page)
    home.open()
    assert "OWASP Juice Shop" in page.title()
