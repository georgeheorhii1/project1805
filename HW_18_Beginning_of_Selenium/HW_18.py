from selenium.webdriver import Chrome, Keys
import time
from selenium.webdriver.common.by import By


def test_1():
    driver = Chrome('PycharmProjects/chromedriver.exe')
    driver.get('https://www.olx.ua/uk/')
    driver.maximize_window()
    search_field_xpath = '//*[@id="headerSearch"]'
    category_xpath = '//*[@id="mainContent"]/div[2]/form/div[3]/div[1]/div/div[1]/div/div/div[1]'
    price_from = '//*[@id="mainContent"]/div[2]/form/div[3]/div[1]/div/div[2]/div/div[1]/div/div[1]/div/input'
    price_to = '//*[@id="mainContent"]/div[2]/form/div[3]/div[1]/div/div[2]/div/div[2]/div/div/div/input'
    filters_down = '//*[@id="mainContent"]/div[2]/form/div[3]/div[2]/div/div/button'
    just_with_fotos = '//*[@id="photos"]'
    sales_and = '//*[@id="footerContent"]/div/div[1]/ul[2]/li[1]/a'
    search_field = driver.find_element(By.XPATH, value=search_field_xpath)
    search_field.send_keys('кедики')
    search_field.send_keys(Keys.ENTER)
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, value=price_from).send_keys('100')
    driver.find_element(By.XPATH, value=price_to).send_keys('1000')
    time.sleep(5)
    driver.save_screenshot('screen_1')
    driver.find_element(By.XPATH, value=just_with_fotos).click()
    driver.find_element(By.XPATH, value=filters_down).click()
    driver.quit()