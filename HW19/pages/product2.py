from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Product2:
    driver = None

    def __init__(self, driver):
        self._driver = driver
        self._web_driver_wait = WebDriverWait(self._driver, 5)

    def _wait_until_element_appears(self, locator):
        return self._web_driver_wait.until(
            EC.presence_of_element_located(locator)

        )


