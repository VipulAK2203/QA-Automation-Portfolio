import time

def test_google_page(page):
    page.goto("https://google.com")
    time.sleep(2)
    assert "Google" in page.title()

def test_amazon_page(page):
    page.goto("https://amazon.in")
    page.wait_for_timeout(2000)
    assert "amazon.in" in page.url

def test_wikipedia_page(page):
    page.goto("https://wikipedia.org")
    time.sleep(2)
    assert "Wikipedia" in page.title()