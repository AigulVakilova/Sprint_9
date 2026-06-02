import allure
from pathlib import Path
from pages.base_page import BasePage
from locators.recipe_page_locators import RecipePageLocators, RecipeCardLocators
from urls import CREATE_RECIPE

class RecipePage(BasePage):

    def open(self) -> None:
        super().open(CREATE_RECIPE)

    @allure.step("Ввести название рецепта: {value}")
    def fill_title(self, value: str) -> None:
        self._fill(RecipePageLocators.TITLE_INPUT, value)

    @allure.step("Ввести описание рецепта")
    def fill_description(self, value: str) -> None:
        self._fill(RecipePageLocators.DESCRIPTION_INPUT, value)

    @allure.step("Ввести время приготовления: {minutes} мин")
    def fill_cooking_time(self, minutes: int) -> None:
        self._fill(RecipePageLocators.COOKING_TIME_INPUT, str(minutes))

    @allure.step("Снять теги «Обед» и «Ужин», оставить только «Завтрак»")
    def deselect_lunch_and_dinner_tags(self) -> None:
        self._click(RecipePageLocators.TAG_LUNCH)
        self._click(RecipePageLocators.TAG_DINNER)

    @allure.step("Добавить ингредиент: {ingredient_name}, количество: {amount}")
    def add_ingredient_from_dropdown(self, ingredient_name: str, amount: str) -> None:
        self._send_keys(RecipePageLocators.INGREDIENT_INPUT, ingredient_name)
        first_item = self._find_present(RecipePageLocators.INGREDIENT_DROPDOWN_ITEM)
        self._js_click(first_item)
        self._wait_invisible(RecipePageLocators.INGREDIENT_DROPDOWN_ITEM)
        self._fill(RecipePageLocators.INGREDIENT_AMOUNT_INPUT, amount)
        self._click(RecipePageLocators.ADD_INGREDIENT_BUTTON)

    @allure.step("Загрузить изображение рецепта")
    def upload_image(self, image_path: Path) -> None:
        upload_input = self._find_present(RecipePageLocators.IMAGE_UPLOAD_INPUT)
        upload_input.send_keys(str(image_path.resolve()))

    @allure.step("Нажать кнопку «Создать рецепт»")
    def submit(self) -> None:
        self._click(RecipePageLocators.SUBMIT_BUTTON)

    @allure.step("Дождаться перехода на страницу созданного рецепта")
    def wait_for_recipe_page(self) -> None:
        # После создания URL меняется на /recipes/{id} где id — число
        self.wait_for_url_matches(r"/recipes/\d+")

    @allure.step("Проверить, что карточка рецепта отображается")
    def is_recipe_card_visible(self) -> bool:
        return self._is_visible(RecipeCardLocators.RECIPE_CARD)

    @allure.step("Получить название рецепта из карточки")
    def get_recipe_card_title(self) -> str:
        return self._get_text(RecipeCardLocators.RECIPE_CARD_TITLE)
    