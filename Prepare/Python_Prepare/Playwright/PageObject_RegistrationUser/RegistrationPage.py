from playwright.sync_api import Page,expect

class RegistrationPage:

    def __init__(self, page: Page):
        self.page = page
        self.email_input = page.locator("#email")
        self.password_input = page.locator("#password")
        self.confirm_password_input = page.locator("#confirmPassword")
        self.phone_input = page.locator("#phone")
        self.submit_btn = page.locator("button[type='submit']")


    def fill_registration_data(self,email : str ,password : str ,confirm_password : str, phone : str) ->"RegistrationPage":

        if password!=confirm_password:
            raise ValueError("Passwords do not match")

        self.email_input.fill(email)
        self.password_input.fill(password)
        self.confirm_password_input.fill(confirm_password)
        self.phone_input.fill(phone)

        return self

    def submit(self) -> "RegistrationPage":
        self.submit_btn.click()
        return self

    def expect_success(self) -> None:
        expect(self.page).to_have_url("**/dashboard")
        expect(self.page.locator(".welcome-message")).to_be_visible()

    def expect_error(self, error_text : str) -> None:
        expect(self.page.locator(".error-message")).to_contain(error_text)
