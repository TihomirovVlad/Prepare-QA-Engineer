import pytest
from playwright.sync_api import sync_playwright

# 1. ФИКСТУРЫ - переиспользуемые setup/teardown
@pytest.fixture

def page():
    """Фикстура для создания браузера и страницы"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        yield page
        browser.close()

# 2 . МАРКЕРЫ - категоризация тестов
@pytest.mark.regression
@pytest.mark.smoke
def test_critical_functionality():
    pass

# 3. ПАРАМЕТРИЗАЦИЯ - один тест, много сценариев

'''
@pytest.mark.parametrize("username,password,expected", [
    ("admin", "123456", True),
    ("user", "wrongpass", False),
    ("", "", False)
])
'''

