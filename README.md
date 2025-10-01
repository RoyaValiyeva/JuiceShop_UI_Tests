# JuiceShop UI & QA Automation Project

This project is a complete QA automation suite built around the **OWASP Juice Shop** demo application.  
It demonstrates **mid-to-senior level QA Automation skills**, covering:

- **UI Automation** with [Playwright](https://playwright.dev/) + Pytest  
- **Cross-browser testing** (Chromium, Firefox, WebKit)  
- **Database Validation** with SQLite (ensuring test results persist)  
- **API / Security Testing** with OWASP ZAP (automated vulnerability scan)  
- **Performance Testing** with Apache JMeter (load simulation & HTML reports)  
- **CI/CD** with GitHub Actions (automated test pipeline on every push)

---

## Project Structure
JuiceShop_UI_Tests/
│
├── pages/ # Page Object Model (POM) classes
│ ├── login_page.py
│ ├── home_page.py
│ └── basket_page.py
│
├── tests/ # Test cases
│ ├── test_login.py
│ ├── test_homepage.py
│ ├── test_basket.py
│ └── test_db_validation.py
│
├── db/ # SQLite database setup
│ └── db.py
│
├── reports/ # Reports (excluded from git)
│ ├── zap/ (OWASP ZAP results)
│ └── jmeter/ (Performance results)
│
├── .github/workflows/ # GitHub Actions CI pipeline
│ └── ci.yml
│
├── requirements.txt # Python dependencies
├── README.md # Documentation
└── .gitignore

---

## 🚀 How to Run

1. Install dependencies
pip install -r requirements.txt

2. Install Playwright browsers
python -m playwright install --with-deps

3. Run tests
pytest -v -s

4. Generate HTML report
pytest -v --html=report.html --self-contained-html

5. Run JMeter liad test
jmeter -n -t reports/jmeter/juice_shop_load_test.jmx -l reports/jmeter/results.jtl -e -o reports/jmeter/dashboard

6. Run OWASP ZAP scan
zap-cli quick-scan http://localhost:3000

## Reports

Playwright UI reports → report.html
JMeter dashboard → reports/jmeter/dashboard/index.html
ZAP security report → reports/zap/zap_report.html


## Future Enhancements

Integrate with TestRail for Test Case Management
Add API tests with Postman collections
Integrate with Docker for containerized test runs
Expand JMeter scenarios for advanced performance metrics


## Author

Roya Valiyeva
QA Automation Engineer
