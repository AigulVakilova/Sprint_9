import os
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from pages.recipe_page import RecipePage
from test_data import EXISTING_USER

@pytest.fixture(scope="function")
def driver():
    """Инициализация драйвера — Selenoid в CI или локальный Chrome"""
    selenoid_url = os.getenv("SELENOID_URL")
 
    if selenoid_url:
        # CI/CD — запуск через Selenoid
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.set_capability("browserName", "chrome")
        chrome_options.set_capability("browserVersion", "128.0")
        chrome_options.set_capability(
            "selenoid:options",
            {"enableVNC": False, "enableVideo": False},
        )
        driver_instance = webdriver.Remote(
            command_executor=selenoid_url,
            options=chrome_options,
        )
    else:
        # Локальный запуск
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--window-size=1920,1080")
        driver_instance = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=chrome_options,
        )
 
    yield driver_instance
 
    driver_instance.quit()

@pytest.fixture(scope="function")
def main_page(driver):
    """Инициализация объекта класса MainPage"""
    return MainPage(driver)

@pytest.fixture(scope="function")
def login_page(driver):
    """Инициализация объекта класса LoginPage"""
    return LoginPage(driver)

@pytest.fixture(scope="function")
def registration_page(driver):
    """Инициализация объекта класса RegistrationPage"""
    return RegistrationPage(driver)

@pytest.fixture(scope="function")
def recipe_page(driver):
    """Инициализация объекта класса RecipePage"""
    return RecipePage(driver)

@pytest.fixture(scope="function")
def authorized_driver(driver, login_page):
    """Авторизация пользователя"""
    login_page.open()
    login_page.fill_email(EXISTING_USER["email"])
    login_page.fill_password(EXISTING_USER["password"])
    login_page.submit()
    login_page.wait_for_main_page()
    return driver

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    if rep.when == "call" and rep.failed:
        driver_instance = item.funcargs.get("driver")
        if driver_instance:
            allure.attach(
                driver_instance.get_screenshot_as_png(),
                name="скриншот_при_падении",
                attachment_type=allure.attachment_type.PNG,
            )
