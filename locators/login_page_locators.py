from selenium.webdriver.common.by import By

class LoginPageLocators:
    TITLE = (By.XPATH, "//h1[text()='Войти на сайт']")
    FORM = (By.CSS_SELECTOR, "form.styles_form__2nwxz")
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    SUBMIT_BUTTON = (By.XPATH, "//button[text()='Войти']")
    