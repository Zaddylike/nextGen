import pytest, logging
from playwright.sync_api import sync_playwright

def setup_logger():
    import logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s.%(msecs)03d [%(levelname)s] [%(name)s:%(lineno)d]  %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
@pytest.mark.smoke
@pytest.mark.parametrize("user_data", [
    {"username": "30100005", "password": "12345678"}
    ])
def test_login(logging_page, user_data):
    logging.info(user_data)
    page = logging_page

def test_goto_page(logging_page):
    page = logging_page