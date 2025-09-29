import pytest
import uuid
from playwright.sync_api import sync_playwright
from db.db import ensure_db   # ✅ import from your db.py

# Browsers to test on
browsers = ["chromium", "firefox", "webkit"]

# ------------------ Playwright Fixture ------------------
@pytest.fixture(params=browsers)
def page(request):
    """Provide a Playwright page object for each browser type."""
    with sync_playwright() as p:
        browser_type = getattr(p, request.param)
        browser = browser_type.launch(headless=True, slow_mo=300)
        page = browser.new_page()
        yield page
        browser.close()

# ------------------ Database Fixture ------------------
@pytest.fixture(scope="session")
def db_conn():
    """One SQLite connection for the whole test session."""
    conn = ensure_db()
    yield conn
    conn.close()

@pytest.fixture()
def test_run_id():
    """Unique id to tag rows written by this test."""
    return str(uuid.uuid4())[:8]
