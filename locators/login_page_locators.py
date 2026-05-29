from selenium.webdriver.common.by import By

class LoginPageLocators:
    TITLE = (By.CSS_SELECTOR, "h1.styles_title__2fhty")
    FORM = (By.CSS_SELECTOR, "form.styles_form__2nwxz")
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button.style_button__1FFWl")
    