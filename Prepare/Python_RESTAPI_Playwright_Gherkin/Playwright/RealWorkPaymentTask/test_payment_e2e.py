from playwright.sync_api import sync_playwright

BASE_URL = "https://httpbin.org/forms/post"


def test_with_text_selectors():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(BASE_URL)

        # Заполняем форму
        page.fill("[name='custname']", "Иван Петров")
        page.fill("[name='custtel']", "+79991234567")
        page.fill("[name='custemail']", "ivan.petrov@bank.com")

        # Кликаем по label с текстом (более надежно)
        page.click("label:has-text('Large')")
        page.click("label:has-text('Bacon')")
        page.click("label:has-text('Cheese')")

        # Или находим чекбокс рядом с текстом
        # page.check("input:right-of(:text('Large'))")

        page.click("text=Submit order")
        page.wait_for_selector("pre")

        browser.close()


def test_invalid_email_rejected():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(BASE_URL)
        page.fill("[name='custname']", "Иван Петров")
        page.fill("[name='custtel']", "+79991234567")
        page.fill("[name='custemail']", "ivan@")
        #page.click("input[type='submit']")
        page.click("text = Submit order")
        page.wait_for_selector("pre")
        response_text = page.text_content("pre")

        assert "ivan@" in response_text
        browser.close()
