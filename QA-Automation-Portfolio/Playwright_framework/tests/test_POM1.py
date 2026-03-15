from Playwright_framework.pages.login_page import LoginPage
from Playwright_framework.pages.dashboard_page import DashboardPage
import time
from Playwright_framework.test_data.login_data import LOGIN_DATA
import pytest

def test_login(page, app_url):
    login = LoginPage(page)
    dashboard = DashboardPage(page)

    login.open(app_url)
    time.sleep(5)
    assert login.is_title_correct("OrangeHRM")
    login.login("Admin", "admin123")
    time.sleep(5)
    assert dashboard.is_search_box_visible()

@pytest.mark.parametrize("username, password, expected", LOGIN_DATA)
def test_login_check(page, app_url, username, password, expected):
    login = LoginPage(page)
    login.open(app_url)
    time.sleep(5)
    login.login(username, password)
    if expected:
        assert login.is_title_correct(expected)


