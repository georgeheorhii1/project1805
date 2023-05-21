from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time


class maifon_ua:
    @pytest.mark.testMphnua
    def run_ua(self):
        driver = webdriver.Chrome()
        xiomi_category_locator = '//img[@src="https://maifon.ua/media/catalog/category/Xiaomi_17.png"]'
        redmi9_locator = '//input[@id="m_category_ids[793]"]'
        gb_locator = '//div[@data-option-label="64 Гб"]'

        driver.get("https://maifon.ua/dlja-novogo-menju/xiaomi.html")
        driver.maximize_window()
        driver.find_element(by=By.XPATH, value=xiomi_category_locator).click()
        driver.implicitly_wait(3)
        find_element_redmi = driver.find_element(by=By.XPATH, value=redmi9_locator)
        find_element_redmi.click()
        driver.save_screenshot('screen_1.png')
        find_element_gb_locator = driver.find_element(by=By.XPATH, value=gb_locator)
        find_element_gb_locator.click()
        driver.execute_script("window.scrollTo(0, 200)")
        time.sleep(2)
        driver.save_screenshot('screen_2.png')
