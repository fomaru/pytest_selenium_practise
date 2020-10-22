from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):

    BASE_URL = "http://localhost:8000/accounts/login/"

    PAGE_CHECK_LOCATOR = (By.XPATH, "//form[@class='form-signin']")
    USERNAME_FIELD_LOCATOR = (By.XPATH, "//input[@id='id_username']")
    PASSWORD_FIELD_LOCATOR = (By.XPATH, "//input[@id='id_password']")
    SUBMIT_BUTTON_LOCATOR = (By.XPATH, "//button[@type='submit']")

    def login(self, username: str, password: str):
        self.find_element(self.USERNAME_FIELD_LOCATOR).send_keys(username)
        self.find_element(self.PASSWORD_FIELD_LOCATOR).send_keys(password)
        self.find_element(self.SUBMIT_BUTTON_LOCATOR).click()