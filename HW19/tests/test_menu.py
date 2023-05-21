
from selenium.webdriver.common.by import By
from HW19.pages.product2 import Product2


def test_check_click(driver):
    driver.get('https://www.olx.ua/uk/')

    element = driver.find_element(By.XPATH, '//span[@class="cat-icon cat-icon-circle category-2 cat-icon-promo"]')
    assert element.is_displayed()
    element.click()
    assert element.is_enabled()


def test_check_velo(driver):
    driver.get('https://www.olx.ua/uk/')

    search_input = driver.find_element(By.XPATH, '//input[@id="headerSearch"]')
    search_input.send_keys("velo")
    search_input.submit()

    results = driver.find_elements(By.XPATH, '//div[@class="search-results"]/div')
    assert len(results) >= 0


def test_main_is_present(driver):
    maincat = driver.find_element(By.XPATH, '//div[@class="maincategories"]')
    assert maincat.is_displayed()


def test_button_details_is_clickable(driver):
    product = Product2(driver)
    button_details = product._wait_until_element_appears((By.XPATH, '//a[@href="https://business.olx.ua"]'))
    assert button_details.is_displayed()


def test_flag_is_present(driver):
    product = Product2(driver)
    flag = product._wait_until_element_appears((By.XPATH, '//span[@class="icon fleft flag olxpl"]'))
    assert flag.is_displayed()
