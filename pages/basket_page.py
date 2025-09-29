from playwright.sync_api import expect

class BasketPage:
    def __init__(self, page):
        self.page = page
        self.basket_btn = "button[aria-label='Show the shopping cart']"
        self.checkout_btn_role = ("button", "Checkout")
        self.row_selector = "mat-row, .mat-row"

    def open(self):
        self.page.locator(self.basket_btn).click()
        self.page.wait_for_url("**/basket", timeout=10000)

    def line_item_count(self) -> int:
        return self.page.locator(self.row_selector).count()

    def expect_checkout_visible(self):
        btn = self.page.get_by_role(self.checkout_btn_role[0],
                                    name=self.checkout_btn_role[1])
        expect(btn).to_be_visible(timeout=10000)
