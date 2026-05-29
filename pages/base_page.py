import re
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

TIMEOUT = 15

class BasePage:
    def __init__(self, driver):
        self._driver = driver
        self._wait = WebDriverWait(driver, TIMEOUT)

    def open(self, url: str) -> None:
        with allure.step(f"Открыть страницу: {url}"):
            self._driver.get(url)

    def get_current_url(self) -> str:
        return self._driver.current_url

    def wait_for_url_contains(self, url: str) -> None:
        with allure.step(f"Дождаться URL: {url}"):
            self._wait.until(EC.url_contains(url))

    def wait_for_url_matches(self, pattern: str) -> None:
        with allure.step(f"Дождаться URL по паттерну: {pattern}"):
            self._wait.until(lambda d: re.search(pattern, d.current_url))

    def get_alert_text_and_accept(self) -> str:
        alert = self._driver.switch_to.alert
        text = alert.text
        alert.accept()
        return text

    def _find_visible(self, locator: tuple):
        return self._wait.until(EC.visibility_of_element_located(locator))

    def _find_clickable(self, locator: tuple):
        return self._wait.until(EC.element_to_be_clickable(locator))

    def _find_present(self, locator: tuple):
        return self._wait.until(EC.presence_of_element_located(locator))

    def _find_all_visible(self, locator: tuple):
        return self._wait.until(EC.visibility_of_all_elements_located(locator))

    def _wait_invisible(self, locator: tuple) -> None:
        self._wait.until(EC.invisibility_of_element_located(locator))

    def _click(self, locator: tuple) -> None:
        self._find_clickable(locator).click()

    def _js_click(self, element) -> None:
        self._driver.execute_script("arguments[0].click();", element)

    def _fill(self, locator: tuple, value: str) -> None:
        field = self._find_visible(locator)
        field.clear()
        field.send_keys(value)

    def _send_keys(self, locator: tuple, value: str) -> None:
        self._find_visible(locator).send_keys(value)

    def _get_text(self, locator: tuple) -> str:
        return self._find_visible(locator).text

    def _is_visible(self, locator: tuple) -> bool:
        try:
            return self._find_visible(locator).is_displayed()
        except TimeoutException:
            return False

    def _is_button_enabled(self, locator: tuple) -> bool:
        return self._find_visible(locator).is_enabled()
    