from selenium.webdriver.common.by import By
from HW19.pages.product2 import Product2


def test_check_click(driver):
    driver.get('https://www.olx.ua/uk/')
    product = Product2(driver)

    element = product._wait_until_element_appears((By.XPATH, '//span[@class="cat-icon cat-icon-circle category-2 '
                                                             'cat-icon-promo"]'))
    assert element.is_displayed()
    element.click()
    assert element.is_enabled()


def test_check_velo(driver):
    driver.get('https://www.olx.ua/uk/')
    product = Product2(driver)

    search_input = product._wait_until_element_appears((By.XPATH, '//input[@id="headerSearch"]'))
    search_input.send_keys("velo")
    search_input.submit()

    results = driver.find_elements(By.XPATH, '//div[@class="search-results"]/div')
    assert len(results) >= 0


def test_main_is_present(driver):
    driver.get('https://www.olx.ua/uk/')
    product = Product2(driver)

    maincat = product._wait_until_element_appears((By.XPATH, '//div[@class="maincategories"]'))
    assert maincat.is_displayed()


def test_button_details_is_clickable(driver):
    driver.get('https://www.olx.ua/uk/')
    product = Product2(driver)

    button_details = product._wait_until_element_appears((By.XPATH, '//div[@class="footer-business-partner__action"]'))
    assert button_details.is_displayed()
    button_details.click()
    assert button_details.is_enabled()

