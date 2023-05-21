from selenium.webdriver.common.by import By
from HW20.pages.base_page import Base
from HW20.pages.page1 import first_page
from HW20.pages.page2 import second_page
import time


def test_search_field(driver):
    driver.get('https://www.olx.ua/uk/')
    base = Base(driver)

    element = base._wait_until_element_appears((By.XPATH, first_page.element_1_search_field_locator))
    assert element.is_displayed()
    element.click()
    assert element.is_enabled()
    driver.find_element(By.XPATH, value=first_page.element_1_search_field_locator).send_keys('keds')
    driver.save_screenshot('keds.img')


# перенести отдельные елементы ч паты итд в файл с соответствующей страчикой.все елементы с главной странички ОЛИкКСа на page1 со страницы товара на пейдж 2

def test_check_product_page(driver):
    driver.get('https://www.olx.ua/d/uk/obyavlenie/prodam-opel-vectra-c-1-9-dizel-IDRYjYb.html')
    base = Base(driver)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    element = base._wait_until_element_appears((By.XPATH, second_page.product_page_show_number_locator))
    assert element.is_displayed
    element.click()
    assert element.is_enabled



