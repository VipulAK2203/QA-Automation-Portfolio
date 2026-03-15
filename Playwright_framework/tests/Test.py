from playwright.sync_api import sync_playwright

def test_launch():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://www.google.com")
        print("Title:", page.title())
        page.wait_for_timeout(3000)
        browser.close()

test_launch()
