import pytest
from playwright.sync_api import sync_playwright
from data.default_parameter import DEFAULT_DOMAIN

    # 1. logging

@pytest.fixture
def user_data():
    return{
        "username": "30100005",
        "password": "12345678",
    }

@pytest.fixture
def logging_page(user_data):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(DEFAULT_DOMAIN)
        page.fill("#UID", user_data["username"])
        page.fill("#KEY", user_data["password"])
        page.click("#btnLogin")
        yield page
        browser.close()

    # 2. user active

