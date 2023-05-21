from selenium import webdriver
from selenium.webdriver.common.by import By


class Cookies:
    def __init__(self, driver):
        self.driver = driver

    def store_cookie(self, name, value):
        self.driver.get("https://rozetka.com.ua/")  # Open the desired URL
        self.driver.add_cookie({"name": name, "value": value})  # Store the cookie

    def get_cookie(self, name):
        self.driver.get("https://rozetka.com.ua/")  # Open the desired URL
        cookies = self.driver.get_cookies()
        for cookie in cookies:
            if cookie["name"] == name:
                return cookie["value"]
        return None


class LocalStorage:
    def __init__(self, driver):
        self.driver = driver

    def store_argument(self, key, value):
        self.driver.get("https://britvamag.com.ua/")  # Open the desired URL
        self.driver.execute_script(f"localStorage.setItem('{key}', '{value}');")

    def get_argument(self, key):
        self.driver.get("https://britvamag.com.ua/ua/login/")  # Open the desired URL
        return self.driver.execute_script(f"return localStorage.getItem('{key}');")


class BasePage:
    def __init__(self):
        self.driver = webdriver.Chrome()  # Initialize your desired web driver
        self.cookies = Cookies(self.driver)
        self.local_storage = LocalStorage(self.driver)

    def login(self, username, password):
        self.driver.get("https://britvamag.com.ua/ua/login/")  # Open the login page
        # Add code to locate and interact with the login elements
        # For example:
        username_input = self.driver.find_element(By.XPATH, value='//input[@name="email"]')
        password_input = self.driver.find_element(By.XPATH, value='//input[@name="password"]')
        login_button = self.driver.find_element(By.XPATH, value='//input[@class="btn btn-primary"]')
        username_input.send_keys('George')
        password_input.send_keys('George')
        login_button.click()

        self.driver.get("https://rozetka.com.ua/")  # Return to the main page after login

    def close(self):
        self.driver.quit()


# Usage example:
base_page = BasePage()
base_page.login("George", "George")

# Now you are logged in and on the main page

base_page.close()
