from Playwright_framework.utils.logger import get_logger

class LoginPage:
    def __init__(self, page):
        self.page = page
        self.logger =get_logger()

        self.username = page.get_by_placeholder("Username")
        self.password = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")

    def open(self, url):
        self.logger.info(f"Opening {url}")
        self.page.goto(url)

    def login(self, user, pwd):
        self.logger.info(f"Logging in...")
        self.logger.info(f"Entered username: {self.username}")
        self.username.fill(user)
        self.logger.info(f"Entered password: {self.password}")
        self.password.fill(pwd)
        self.logger.info("Clicking login button...")
        self.login_button.click()

    def is_title_correct(self, title):
        return self.page.title() == title
