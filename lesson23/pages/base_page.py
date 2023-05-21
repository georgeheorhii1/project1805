from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lesson23.core.locator import Locator


class BasePage:
    def __init__(self, driver):
        self._driver = driver
        self._web_driver_wait = WebDriverWait(self._driver, 5)

    def _wait_until_element_appears(self, locator: Locator):
        return self._web_driver_wait.until(EC.presence_of_element_located(locator.to_tuple()))

    def _click(self, locator: Locator):
        self._wait_until_element_appears(locator).click()
