import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    # Set up the WebDriver instance (e.g., ChromeDriver)
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Optional: Perform any additional setup or configuration

    # Return the driver instance
    yield driver

    # Teardown: Quit the WebDriver instance
    driver.quit()
