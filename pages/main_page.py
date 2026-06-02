import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators, NavLocators
from urls import MAIN

class MainPage(BasePage):

    def open(self) -> None:
        super().open(MAIN)

    @allure.step("Нажать кнопку «Создать аккаунт» в навигации")
    def click_signup_link(self) -> None:
        self._click(NavLocators.SIGNUP_LINK)

    @allure.step("Нажать кнопку «Войти» в навигации")
    def click_signin_link(self) -> None:
        self._click(NavLocators.SIGNIN_LINK)

    @allure.step("Проверить отображение кнопки «Выход»")
    def is_logout_button_visible(self) -> bool:
        return self._is_visible(MainPageLocators.LOGOUT_BUTTON)

    @allure.step("Перейти на страницу создания рецепта через навигацию")
    def click_create_recipe_link(self) -> None:
        self._click(MainPageLocators.CREATE_RECIPE_NAV_LINK)
