import pytest
from playwright.sync_api import sync_playwright

browsers = ["chromium", "firefox", "webkit"]

@pytest.fixture(params=browsers)
def page(request):
    with sync_playwright() as p:
        browser_type = getattr(p, request.param)
        browser = browser_type.launch(headless=True, slow_mo=300)
        page = browser.new_page()
        yield page
        browser.close()
