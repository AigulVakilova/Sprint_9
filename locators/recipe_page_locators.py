from selenium.webdriver.common.by import By

class RecipePageLocators:
    TITLE_INPUT = (By.CSS_SELECTOR, "div.styles_input__2Dg_j:first-child input[type='text']")
    DESCRIPTION_INPUT = (By.CSS_SELECTOR, "textarea.styles_textareaField__1wfhC")
    COOKING_TIME_INPUT = (By.CSS_SELECTOR, "div[class*='styles_ingredientsTimeInput'] input[type='text']")
    INGREDIENT_INPUT = (By.CSS_SELECTOR, "input.styles_ingredientsInput__1zzql")
    INGREDIENT_DROPDOWN_ITEM = (By.CSS_SELECTOR, "div.styles_container__3ukwm div")
    INGREDIENT_AMOUNT_INPUT = (By.CSS_SELECTOR, "input.styles_ingredientsAmountValue__2matT")
    ADD_INGREDIENT_BUTTON = (By.CSS_SELECTOR, "div.styles_ingredientAdd__3fc32")
    IMAGE_UPLOAD_INPUT = (By.CSS_SELECTOR, "input.styles_fileInput__3HjP3[type='file']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button.style_button__1FFWl")
    TAG_LUNCH = (By.XPATH, "//span[text()='Обед']/preceding-sibling::button")
    TAG_DINNER = (By.XPATH, "//span[text()='Ужин']/preceding-sibling::button")

class RecipeCardLocators:
    RECIPE_CARD  = (By.CSS_SELECTOR, "div[class*='styles_single-card']")
    RECIPE_CARD_TITLE = (By.CSS_SELECTOR, "h1[class*='styles_single-card__title']")
    