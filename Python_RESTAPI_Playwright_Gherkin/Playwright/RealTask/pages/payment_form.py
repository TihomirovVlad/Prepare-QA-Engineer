# pages/payment_form.py
from playwright.sync_api import Page
from typing import List


class PaymentForm:
    def __init__(self, page: Page):
        self.page = page
        self.customer_name = page.locator("[name='custname']")
        self.customer_phone = page.locator("[name='custtel']")
        self.customer_email = page.locator("[name='custemail']")
        self.submit_button = page.locator("text=Submit order")
        self.response_pre = page.locator("pre")

    def navigate_to_form(self) -> "PaymentForm":
        self.page.goto("https://httpbin.org/forms/post")
        return self

    def fill_customer_info(self, name: str, phone: str, email: str) -> "PaymentForm":
        self.customer_name.fill(name)
        self.customer_phone.fill(phone)
        self.customer_email.fill(email)
        return self

    def select_pizza_options(self, size: str = "large", toppings: List[str] = None) -> "PaymentForm":
        if toppings is None:
            toppings = ["bacon", "cheese"]

        self.page.check(f"input[value='{size}']")
        for topping in toppings:
            self.page.check(f"input[value='{topping}']")
        return self

    def submit_order(self) -> "PaymentForm":
        self.submit_button.click()
        self.page.wait_for_selector("pre")
        return self

    def get_response_text(self) -> str:
        return self.response_pre.text_content() or ""