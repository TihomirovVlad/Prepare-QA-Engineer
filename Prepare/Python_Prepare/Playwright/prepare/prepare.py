from playwright.sync_api import Page,expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.submit_btn = page.locator("button[type='submit']")
        self.error_msg = page.locator(".error-message")

    def login(self, username: str, password: str) -> "LoginPage":
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.submit_btn.click()
        return self  # ← Fluent interface

    def expect_success_login(self) -> None:
        expect(self.page).to_have_url("**/dashboard")
