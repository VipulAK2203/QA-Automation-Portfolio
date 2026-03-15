from playwright.sync_api import sync_playwright
from playwright.sync_api import expect

def test4_launch():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://opensource-demo.orangehrmlive.com/")
        page.wait_for_timeout(3000)

        page.get_by_placeholder("Username").fill("Admin")
        page.get_by_placeholder("Password").fill("admin123")
        page.get_by_text("Login").last.click()
        page.wait_for_timeout(3000)

        expect(page).to_have_url(lambda url: "dashboard" in url)
        expect(page.get_by_text("Invalid credentials")).not_to_be_visible()
        browser.close()
