import allure
from pages.base_page import BasePage
from locators.registration_page_locators import RegistrationPageLocators
from urls import SIGNUP, SIGNIN

class RegistrationPage(BasePage):

    def open(self) -> None:
        super().open(SIGNUP)

    @allure.step("Ввести имя: {value}")
    def fill_first_name(self, value: str) -> None:
        self._fill(RegistrationPageLocators.FIRST_NAME_INPUT, value)

    @allure.step("Ввести фамилию: {value}")
    def fill_last_name(self, value: str) -> None:
        self._fill(RegistrationPageLocators.LAST_NAME_INPUT, value)

    @allure.step("Ввести имя пользователя: {value}")
    def fill_username(self, value: str) -> None:
        self._fill(RegistrationPageLocators.USERNAME_INPUT, value)

    @allure.step("Ввести email: {value}")
    def fill_email(self, value: str) -> None:
        self._fill(RegistrationPageLocators.EMAIL_INPUT, value)

    @allure.step("Ввести пароль")
    def fill_password(self, value: str) -> None:
        self._fill(RegistrationPageLocators.PASSWORD_INPUT, value)

    @allure.step("Нажать кнопку «Создать аккаунт»")
    def submit(self) -> None:
        self._click(RegistrationPageLocators.SUBMIT_BUTTON)

    @allure.step("Проверить, что форма регистрации отображается")
    def is_form_visible(self) -> bool:
        return self._is_visible(RegistrationPageLocators.FORM)

    @allure.step("Дождаться перехода на страницу авторизации")
    def wait_for_redirect_to_signin(self) -> None:
        self.wait_for_url_contains(SIGNIN)
