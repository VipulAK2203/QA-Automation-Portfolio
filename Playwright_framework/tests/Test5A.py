from playwright.sync_api import sync_playwright

def test5A_launch():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://demoqa.com/alerts")
        page.wait_for_timeout(3000)

        with page.expect_dialog() as dialog_info:
            page.get_by_text("Click me").first.click()

        dialog = dialog_info.value
        dialog.accept()

        with page.expect_dialog() as dialog_info:
            page.get_by_text("Click me").nth(2).click()
            page.wait_for_timeout(5000)

        dialog = dialog_info.value
        dialog.accept()