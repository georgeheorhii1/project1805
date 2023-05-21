from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time


class mob_ru:
    @pytest.mark.testMphnua
    def run_mob_ru(self):
        driver = webdriver.Chrome()
        serie_12_locator = '//*[@id="maincontent"]/div[3]/div[1]/div[2]/div[2]/a'
        wave_locator = '//input[@id="m_vendor[13499]"]'
        grey_locator = '//input[@id="m_cvet_v_fil_trah[2469]"]'

        driver.get("https://mob.com.ua/rus/xiaomi.html")
        driver.maximize_window()
        driver.find_element(by=By.XPATH, value=serie_12_locator).click()
        driver.implicitly_wait(3)
        find_element_redmi = driver.find_element(by=By.XPATH, value=wave_locator)
        find_element_redmi.click()
        driver.save_screenshot('screen_1.png')
        find_element_gb_locator = driver.find_element(by=By.XPATH, value=grey_locator)
        find_element_gb_locator.click()
        driver.execute_script("window.scrollTo(0, 200)")
        time.sleep(2)
        driver.save_screenshot('screen_2.png')
