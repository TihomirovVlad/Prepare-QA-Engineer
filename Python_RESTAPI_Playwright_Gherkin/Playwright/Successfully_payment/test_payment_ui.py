from playwright.sync_api import sync_playwright


def test_can_fill_submit_payment_form():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        page.goto("https://httpbin.org/forms/post")

        page.fill("[name='custname']", "Иван Иванов")
        page.fill("[name='custtel']", "+7123456790")
        page.fill("[name='custemail']", "ivan@bank.com")

        page.check("#large")
        page.check("#bacon")
        page.check("#cheese")

        page.click("text=Submit order")

        page.wait_for_selector("pre")

        response_text = page.text_content("pre")

        assert "Иван Иванов" in response_text
        assert "ivan@bank.com" in response_text
        assert "bacon" in response_text
        assert "cheese" in response_text

        browser.close()