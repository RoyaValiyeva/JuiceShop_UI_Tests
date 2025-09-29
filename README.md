# 🛡️ Juice Shop QA Automation Project

This project is a **QA Automation Framework** for [OWASP Juice Shop](https://owasp.org/www-project-juice-shop/), built to showcase **end-to-end testing skills** across API, UI, database, performance, and security.

It demonstrates practices expected from a **mid-to-senior QA engineer**:  
- ✅ Page Object Model (POM) with Playwright (UI tests)  
- ✅ Pytest with fixtures & structured test suites  
- ✅ API testing (Postman + Python requests)  
- ✅ Extendable for SQL validation, JMeter performance, ZAP security  
- ✅ CI/CD-ready (GitHub Actions or Jenkins)

---

## Project Structure

JuiceShop_UI_Tests/
├── pages/                # Page Object Model classes
│   ├── home_page.py
│   ├── login_page.py
│   └── basket_page.py
├── tests/                # Test cases
│   ├── test_homepage.py
│   ├── test_login.py
│   └── test_basket.py
├── conftest.py           # Pytest fixture (browser setup/teardown)
├── requirements.txt      # Project dependencies
├── .gitignore            # Files ignored by Git
└── README.md             # Project documentation

---

## Installation & Setup

1. Clone the repository  
git clone https://github.com/
<your-username>/JuiceShop_UI_Tests.git
cd JuiceShop_UI_Tests

2. (Optional) Create & activate a virtual environment  
python -m venv venv
venv\Scripts\activate # Windows
source venv/bin/activate # macOS/Linux

3. Install dependencies  
pip install -r requirements.txt

4. Run OWASP Juice Shop locally (Docker required) 
docker run --rm -p 3000:3000 bkimminich/juice-shop
App will be available at [http://localhost:3000](http://localhost:3000).

---

## Running Tests

Run all tests:  
pytest -v
Run a specific test:  
pytest -v tests/test_login.py::test_login_success
Run with debug output:  
pytest -v -s

---

## Example Tests

### UI Tests (Playwright + POM)
- Homepage: Verify site opens and title contains *OWASP Juice Shop*  
- Login: Login with valid credentials and assert basket is visible  
- Basket: Add product to basket and verify checkout available  

### API Tests (Postman / Python requests)
- Verify CRUD operations on `/api/Products`  
- Validate login token response & error handling  

---

## Future Enhancements
- Add SQL validation after UI/API actions  
- Integrate JMeter performance tests (load test login & search)  
- Run OWASP ZAP baseline scan and attach security report  
- Add GitHub Actions for CI/CD (run tests on push/pull request)  
- Export test results to TestRail/Zephyr (API integration)

---

## Author
**Roya Valiyeva** – QA Automation Engineer, a portfolio of real-world test frameworks.
