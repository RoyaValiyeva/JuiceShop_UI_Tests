class HomePage:
    def __init__(self, page):
        self.page = page
        self.close_welcome = "button[aria-label='Close Welcome Banner']"
        self.dismiss_cookie = "button[aria-label='Dismiss Cookie Message']"

    def open(self):
        self.page.goto("http://localhost:3000")

    def dismiss_popups(self):
        for css in [self.close_welcome, self.dismiss_cookie]:
            try:
                self.page.click(css, timeout=1200)
            except:
                pass
