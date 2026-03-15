from playwright.sync_api import sync_playwright
from playwright.sync_api import expect

def test3_launch():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://demoqa.com/buttons")
        page.wait_for_timeout(3000)

        page.get_by_text("Double Click Me").dblclick()
        page.wait_for_timeout(1000)
        expect(page.get_by_text("You have done a double click")).to_be_visible()

        page.get_by_text("Right Click Me").click(button='right')
        page.wait_for_timeout(1000)
        expect(page.get_by_text("You have done a right click")).to_be_visible()

        browser.close()