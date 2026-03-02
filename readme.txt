# Automated-API-Testing-Framework-with-Pytest
This project is an Automated API Testing Framework built with Python and Pytest, designed to streamline the testing of RESTful APIs. The framework uses the publicly available API service at Reqres  to demonstrate end-to-end API automation, including test case execution, reporting, and result management.

Key Features:
Automated Test Execution: Supports running multiple API test cases in parallel or sequentially using pytest.
Comprehensive Test Reporting: Integrates with Allure to generate visually rich and interactive test reports.
Flexible Directory & Log Management: Automatically creates structured folders for test results, reports, and logs, each timestamped for traceability.
Error Handling & Logging: Robust logging system using Python’s logging module to capture test execution info, warnings, and errors.
Parameterized Tests: Supports reading test data from YAML/JSON files to easily manage multiple test scenarios.

Tech Stack:
Python 3.x
Pytest – Testing framework
Allure – Test report generation
YAML / JSON – Test data management
Subprocess & OS modules – Automation utilities

Usage:
Clone the repository.
Ensure all dependencies are installed (pip install -r requirements.txt).
Run python run.py to execute all API tests and generate reports automatically.
Reports are saved under reports/ with timestamped directories for easy reference.
Benefits:
Speeds up API testing workflows.
Provides detailed insights into test failures and system responses.
Can be used as a template for building larger-scale API automation frameworks.
