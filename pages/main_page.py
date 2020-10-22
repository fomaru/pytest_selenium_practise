from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage):

    BASE_URL = "http://localhost:8000/blog/"

    PAGE_CHECK_LOCATOR = (By.XPATH, "//div[contains(@class, 'blog-main')]")

