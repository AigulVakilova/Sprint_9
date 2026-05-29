from selenium.webdriver.common.by import By

class RegistrationPageLocators:
    TITLE = (By.CSS_SELECTOR, "h1.styles_title__2fhty")
    FORM = (By.CSS_SELECTOR, "form.styles_form__2nwxz")
    FIRST_NAME_INPUT = (By.NAME, "first_name")
    LAST_NAME_INPUT = (By.NAME, "last_name")
    USERNAME_INPUT = (By.NAME, "username")
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button.style_button__1FFWl")
    