from playwright.sync_api import expect

class LoginPage:
    def __init__(self, page):
        self.page = page
        self.email = "#email"
        self.password = "#password"
        self.login_btn = "#loginButton"
        self.basket_btn = "button[aria-label='Show the shopping cart']"

    def open(self):
        self.page.goto("http://localhost:3000/#/login")
        self.page.wait_for_url("**/login", timeout=10000)

    def login(self, email: str, password: str):
        self.page.fill(self.email, email)
        self.page.fill(self.password, password)
        self.page.click(self.login_btn)
        expect(self.page.locator(self.basket_btn)).to_be_visible(timeout=10000)
