from selenium.webdriver.common.by import By

class NavLocators:
    SIGNUP_LINK = (By.CSS_SELECTOR, "a[href='/signup']")
    SIGNIN_LINK = (By.CSS_SELECTOR, "a[href='/signin']")

class MainPageLocators:
    LOGOUT_BUTTON = (By.XPATH, "//a[contains(@class,'styles_menuLink') and text()='Выход']")
    CREATE_RECIPE_NAV_LINK = (By.CSS_SELECTOR, "a[href='/recipes/create']")
