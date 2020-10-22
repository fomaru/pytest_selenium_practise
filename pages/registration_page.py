from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class RegistrationPage(BasePage):

    BASE_URL = "http://localhost:8000/accounts/signup/"

    PAGE_CHECK_LOCATOR = (By.XPATH, "//*[contains(text(),'Registration')]")
    FIRST_NAME_FIELD_LOCATOR = (By.XPATH, "//input[@name='first_name']")
    LAST_NAME_FIELD_LOCATOR = (By.XPATH, "//input[@name='second_name']")
    USERNAME_FIELD_LOCATOR = (By.XPATH, "//input[@name='username']")
    EMAIL_FIELD_LOCATOR = (By.XPATH, "//input[@name='email']")
    ADDRESS_FIELD_LOCATOR = (By.XPATH, "//input[@name='address']")
    AGE_FIELD_LOCATOR = (By.XPATH, "//input[@name='age']")
    PASSWORD_FIELD_LOCATOR = (By.XPATH, "//input[@name='password1']")
    CONFIRM_PASSWORD_FIELD_LOCATOR = (By.XPATH, "//input[@name='password2']")
    SUBMIT_BUTTON_LOCATOR = (By.XPATH, "//button[@type='submit']")

    def register(self, first_name, last_name, username,
                 email, address, age, password):
        self.find_element(self.FIRST_NAME_FIELD_LOCATOR).send_keys(first_name)
        self.find_element(self.LAST_NAME_FIELD_LOCATOR).send_keys(last_name)
        self.find_element(self.USERNAME_FIELD_LOCATOR).send_keys(username)
        self.find_element(self.EMAIL_FIELD_LOCATOR).send_keys(email)
        self.find_element(self.ADDRESS_FIELD_LOCATOR).send_keys(address)
        self.find_element(self.AGE_FIELD_LOCATOR).send_keys(age)
        self.find_element(self.PASSWORD_FIELD_LOCATOR).send_keys(password)
        self.find_element(self.CONFIRM_PASSWORD_FIELD_LOCATOR).send_keys(password)
        self.find_element(self.SUBMIT_BUTTON_LOCATOR).click()
