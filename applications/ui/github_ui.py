from playwright.sync_api import Page

from applications.ui.base_page import BasePage


class GithubUI(BasePage):

    def __init__(self, base_url_ui, page: Page):
        super().__init__(page)

        self.base_url_ui = base_url_ui

        self.input_username = page.get_by_label("Username or email address")
        self.input_password = page.get_by_label("Password")
        self.submit_button = page.get_by_role("button", name="Sign in")

    def goto(self):
        self.page.goto(self.base_url_ui + "/login")
        return self

    def login(self, username, password):
        self.input_username.fill(username)
        self.input_password.fill(password)
        self.submit_button.click()
