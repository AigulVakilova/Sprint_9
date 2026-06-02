import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from urls import SIGNIN, RECIPES

class LoginPage(BasePage):

    def open(self) -> None:
        super().open(SIGNIN)

    @allure.step("Ввести email: {value}")
    def fill_email(self, value: str) -> None:
        self._fill(LoginPageLocators.EMAIL_INPUT, value)

    @allure.step("Ввести пароль")
    def fill_password(self, value: str) -> None:
        self._fill(LoginPageLocators.PASSWORD_INPUT, value)

    @allure.step("Нажать кнопку «Войти»")
    def submit(self) -> None:
        self._find_visible(LoginPageLocators.SUBMIT_BUTTON).click()
        try:
            alert = self._wait.until(EC.alert_is_present())
            message = alert.text
            alert.accept()
            raise AssertionError(f"Ошибка авторизации: {message}")
        except TimeoutException:
            pass

    @allure.step("Проверить, что форма авторизации отображается")
    def is_form_visible(self) -> bool:
        return self._is_visible(LoginPageLocators.FORM)

    @allure.step("Дождаться перехода на главную страницу")
    def wait_for_main_page(self) -> None:
        self.wait_for_url_contains(RECIPES)
