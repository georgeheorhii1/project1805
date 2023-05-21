from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time


class maifon_ru:
    @pytest.mark.testMphnru
    def run_ru(self):
        driver = webdriver.Chrome()
        xiomi_category_locator = '//img[@src="https://maifon.ua/media/catalog/category/Xiaomi_17.png"]'
        redmi9_locator = '//*[@id="maincontent"]/div[3]/div[1]/div[2]/div[2]/a'
        gb_locator = '//div[@data-option-label="64 Гб"]'

        driver.get("https://maifon.ua/ru/dlja-novogo-menju/xiaomi.html")
        driver.maximize_window()
        driver.find_element(by=By.XPATH, value=xiomi_category_locator).click()
        driver.implicitly_wait(3)
        find_element_redmi = driver.find_element(by=By.XPATH, value=redmi9_locator)
        find_element_redmi.click()
        driver.save_screenshot('screen_1ru.png')
        find_element_gb_locator = driver.find_element(by=By.XPATH, value=gb_locator)
        find_element_gb_locator.click()
        driver.execute_script("window.scrollTo(0, 200)")
        time.sleep(2)
        driver.save_screenshot('screen_2ru.png')