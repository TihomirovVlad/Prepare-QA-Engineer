# tests/test_payment_flow.py
import pytest
import sys
import os
import json

# Исправляем импорт
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from pages.payment_form import PaymentForm
from playwright.sync_api import Page


@pytest.fixture
def page():
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        yield page
        browser.close()


class TestPaymentFlow:

    def test_complete_payment_flow(self, page: Page):
        payment_form = PaymentForm(page)

        response_text = (payment_form
                         .navigate_to_form()
                         .fill_customer_info("Иван Петров", "+79991234567", "ivan@bank.com")
                         .select_pizza_options("large", ["bacon", "cheese"])
                         .submit_order()
                         .get_response_text())

        # Парсим JSON ответ
        response_data = json.loads(response_text)

        # Проверяем данные в form секции
        assert response_data["form"]["custname"] == "Иван Петров"
        assert response_data["form"]["custemail"] == "ivan@bank.com"
        assert response_data["form"]["size"] == "large"
        assert "bacon" in response_data["form"]["topping"]
        assert "cheese" in response_data["form"]["topping"]

        print("✅ Все проверки пройдены!")
