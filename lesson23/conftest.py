from selenium.webdriver import Chrome
from lesson23.pages.dashboard_page import Dashboard
import pytest


@pytest.fixture(scope="session")
def driver():
    driver = Chrome('lesson23/drivers/chromedriver.exe')

    driver.get("https://epicentrk.ua/")
    driver.set_window_size(100, 100)
    # for cookie in driver.get_cookies():
    #    print(cookie)
    # print(driver.get_cookie('EPIC_LANG'))
    token_xsrf = 'XSRF-TOKEN'
    driver.add_cookie({'name': 'test', 'value': 'test_value'})
    driver.get_cookie('test')

    yield driver

    driver.quit()


@pytest.fixture
def dashboard(driver):
    yield Dashboard(driver)
