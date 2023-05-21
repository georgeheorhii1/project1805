from selenium.webdriver import Chrome, Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_01():
    driver = Chrome('lesson23/drivers/chromedriver.exe')
    driver.get('https://google.com')
    # driver.implicitly_wait(5)
    web_driver_wait = WebDriverWait(driver, 10)
    search_input_field_locator = '//textarea[@title="Пошук"]'
    first_non_ad_link_locator = "//h3[contains(text(), 'Повернись живим – фонд компетентної допомоги армії ...')]/.."
    search_input_field = web_driver_wait.until(EC.presence_of_element_located(('xpath', '//textarea['
                                                                                                  '@title="Пошук"]')))
#    search_input_field = driver.find_element(by='xpath', value=search_input_field_locator)
    search_input_field.send_keys('Повернись живим')
    search_input_field.send_keys(Keys.ENTER)
    first_non_ad_link = driver.find_element(by='xpath', value=first_non_ad_link_locator)
    first_non_ad_link.click()
    driver.quit()
