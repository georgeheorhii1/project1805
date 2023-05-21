from selenium.webdriver import Chrome, Keys
import time


def test_01():
    driver = Chrome('PycharmProjects/chromedriver.exe')
    driver.get('https://www.google.com/')
    search_input_field_locator = "//textarea[@title='Пошук']"
    first_none_ID_link_locator = "//h3[contains(text(), 'Повернись живим – фонд компетентної допомоги армії ...')]/.."
    search_input_field = driver.find_element(by='xpath', value=search_input_field_locator)
    search_input_field.send_keys('повернись живим')
    search_input_field.send_keys(Keys.ENTER)
    first_none_ID_link = driver.find_element(by='xpath', value=first_none_ID_link_locator)
    first_none_ID_link.click()


    time.sleep(5)
    driver.quit()
