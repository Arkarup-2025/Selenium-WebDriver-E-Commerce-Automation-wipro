# Selenium WebDriver E-Commerce Automation

An end-to-end Python/Selenium project for purchasing a product on the [TutorialsNinja demo store](https://tutorialsninja.com/demo/). It covers login, product search, cart updates and verification, screenshots, alert handling, Excel/JSON test data, and an HTML execution report.

## Prerequisites

- Python 3.10+
- Google Chrome (ChromeDriver is managed automatically by Selenium Manager)
- A valid TutorialsNinja demo-store account. Create one via **My Account > Register** if needed.
- Optional: VS Code or PyCharm for running the tests and reviewing HTML reports.

## Features

This automation framework includes:

- Login flow with real account credentials from environment variables
- Product search and selection from the demo storefront
- Cart validation for product name, price, subtotal, and quantity
- Screenshot capture at key stages for debugging and reporting
- JSON and Excel test-data support for parameterized scenarios
- HTML report generation using pytest for easy execution summaries

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
```

Then edit `.env` with your account credentials. The first test run automatically creates `data/test_data.xlsx` from the JSON seed data; this keeps the binary spreadsheet out of source control while still exercising Excel input.

Example `.env` values:

```env
USERNAME=your_email@example.com
PASSWORD=your_demo_password
```

## Run

```powershell
pytest
```

Outputs:

- `reports/execution_report.html` — self-contained pytest HTML report
- `screenshots/` — timestamped screenshots for key workflow stages and failures
- `data/test_data.xlsx` — generated Excel test-data source

## Project structure

```
pages/       Page Object Model classes
tests/       Selenium end-to-end test
utils/       configuration, Excel/JSON readers, screenshots, alert helper
data/        JSON seed and generated Excel test data
```

## Typical workflow

The test flow is designed to:

1. Log in to the storefront.
2. Search for a product using the configured data source.
3. Add the item to the cart.
4. Validate the cart details before the flow completes.
5. Capture screenshots and publish a detailed HTML test report.

## Troubleshooting

- If the site loads slowly or behaves inconsistently, re-run the test after refreshing the demo store state.
- If ChromeDriver is not found, ensure Chrome is installed and Selenium Manager can access it.
- If credentials fail, confirm the `.env` file is populated and saved correctly.
- If a test fails on the cart assertions, review the generated screenshots and HTML report for the exact mismatch.

## Notes

The demo site is public and can be reset or temporarily unavailable. Credentials are intentionally not committed. The test verifies the cart item name, unit price, line total calculation, and requested quantity before it ends; it does not place an irreversible order.
