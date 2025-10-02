import pytest
from playwright.async_api import Page
from playwright.sync_api import sync_playwright
from Prepare.Python_Prepare.Playwright.PageObject_RegistrationUser import RegistrationPage


@pytest.fixture

def page():
    """Фикстура для создания браузера и страницы"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        yield page
        browser.close()

class TestRegistration:
    @pytest.mark.smoke
    @pytest.mark.parametrize("email,password,phone",[
        ("test1@mail.com", "password123", "+79991112233"),
        ("user@domain.com", "qwerty", "+79994445566")
    ])

    def test_successful_registration(self, page : Page, email : str, password : str, phone : str):
        registration = RegistrationPage(page)

        (registration
         .fill_registration_data(email, password, password, phone)
         .submit()
         .expect_success())

    @pytest.mark.regression
    def test_password_mismatch_error(self,page : Page):
        registration = RegistrationPage(page)

        with pytest.raises(ValueError, match= "Passwords do not match"):
            registration.fill_registration_data(
                "test@mail.com",
                "password123",
                "different",  # пароли не совпадают
                "+79991112233"
            )

    @pytest.mark.regression
    def test_invalid_email_error(self, page: Page):
        registration = RegistrationPage(page)

        # Здесь зависит от реализации - либо исключение, либо UI ошибка
        # Предположим что валидация на стороне UI
        (registration
         .fill_registration_data(
            "invalid-email",  # нет @
            "password123",
            "password123",
            "+79991112233"
        )
         .submit()
         .expect_error("Invalid email format"))

