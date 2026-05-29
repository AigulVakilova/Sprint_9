import allure
from test_data import NEW_USER
from urls import SIGNIN

@allure.feature("Регистрация")
class TestRegistration:

    @allure.title("Создание аккаунта")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_account(self, main_page, registration_page, login_page):
        main_page.open()
        main_page.click_signup_link()

        registration_page.fill_first_name(NEW_USER["first_name"])
        registration_page.fill_last_name(NEW_USER["last_name"])
        registration_page.fill_username(NEW_USER["username"])
        registration_page.fill_email(NEW_USER["email"])
        registration_page.fill_password(NEW_USER["password"])
        registration_page.submit()

        registration_page.wait_for_redirect_to_signin()

        assert SIGNIN in registration_page.get_current_url(), (
            "После регистрации ожидался переход на /signin"
        )
        assert login_page.is_form_visible(), (
            "Форма авторизации должна отображаться после успешной регистрации"
        )
