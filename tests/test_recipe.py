import allure
from test_data import NEW_RECIPE, TEST_IMAGE

@allure.feature("Рецепты")
class TestRecipeCreation:

    @allure.title("Создание рецепта")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_recipe(self, authorized_driver, main_page, recipe_page):
        main_page.click_create_recipe_link()

        recipe_page.fill_title(NEW_RECIPE["title"])
        recipe_page.deselect_lunch_and_dinner_tags()
        recipe_page.fill_description(NEW_RECIPE["description"])
        recipe_page.fill_cooking_time(NEW_RECIPE["cooking_time"])

        for ingredient in NEW_RECIPE["ingredients"]:
            recipe_page.add_ingredient_from_dropdown(
                ingredient["name"],
                ingredient["amount"],
            )

        recipe_page.upload_image(TEST_IMAGE)
        recipe_page.submit()

        recipe_page.wait_for_recipe_page()

        assert recipe_page.is_recipe_card_visible(), (
            "Карточка созданного рецепта должна отображаться после сохранения"
        )
        assert recipe_page.get_recipe_card_title() == NEW_RECIPE["title"], (
            "Название в карточке рецепта должно совпадать с введённым при создании"
        )
