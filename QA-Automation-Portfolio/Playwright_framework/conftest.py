import pytest
import pytest_metadata
import os
import pytest_html
import time
from playwright.sync_api import sync_playwright

def pytest_addoption(parser):
    parser.addoption("--Browser",
                    action="store",
                    default="chromium",
                    help="Browser to run tests")

    parser.addoption("--env",
                    action="store",
                    default="qa",
                    help="Staging directory")

@pytest.fixture
def app_url(request):
    from Playwright_framework.config.env_config import ENVIRONMENTS
    env = request.config.getoption("--env")
    return ENVIRONMENTS[env]

@pytest.fixture(scope="session")
def browser(request):
    browser_name = request.config.getoption("--Browser")
    with sync_playwright() as p:

        if browser_name == "chromium":
            browser = p.chromium.launch(headless=True)

        elif browser_name == "firefox":
            browser = p.firefox.launch(headless=True)

        elif browser_name == "webkit":
            browser = p.webkit.launch(headless=True)

        yield browser
        browser.close()

@pytest.fixture(scope="function")
def context(browser):
    context = browser.new_context()
    yield context
    context.close()

@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    yield page
    page.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        page = item.funcargs.get("page")

        if page:

            os.makedirs("screenshots", exist_ok=True)

            screenshot_name = f"screenshots/{item.name}_{int(time.time())}.png"

            try:
                page.screenshot(path=screenshot_name)

                extra = getattr(report, "extra", [])
                extra.append(pytest_html.extras.image(screenshot_name))
                report.extra = extra

            except Exception as e:
                print(e)

@pytest.hookimpl(optionalhook=True)
def pytest_configure(config):
    config._metadata = getattr(config, "_metadata", {})
    config._metadata["Project Name"] = "Playwright Framework"
    config._metadata["Tester"] = "Lord Vipul"
    config._metadata["Browser"] = "Chromium"