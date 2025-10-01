from playwright.sync_api import sync_playwright

def test_can_add_todo():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://demo.playwright.dev/todomvc")
        page.fill(".new-todo", "Протестировать платёж")
        page.press(".new-todo", "Enter")
        page.wait_for_selector("text=Протестировать платёж")
        browser.close()