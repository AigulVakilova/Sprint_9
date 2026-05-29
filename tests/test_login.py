import allure
from test_data import EXISTING_USER

@allure.feature("Авторизация")
class TestLogin:

    @allure.title("Переход на главную страницу и отображение кнопки «Выход»")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_login(self, main_page, login_page):
        main_page.open()
        main_page.click_signin_link()

        login_page.fill_email(EXISTING_USER["email"])
        login_page.fill_password(EXISTING_USER["password"])
        login_page.submit()

        login_page.wait_for_main_page()

        assert main_page.is_logout_button_visible(), (
            "Кнопка «Выход» должна отображаться после успешной авторизации"
        )
