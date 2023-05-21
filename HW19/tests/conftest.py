import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()
    driver.get('https://www.olx.ua/uk/')
    driver.maximize_window()

    yield driver

    driver.quit()
