class BasePage:

    BASE_URL = None
    PAGE_CHECK_LOCATOR = None

    def __init__(self, driver):
        self.driver = driver
        if self.BASE_URL:
            self.driver.get(self.BASE_URL)
        if self.PAGE_CHECK_LOCATOR:
            self.driver.find_element(*self.PAGE_CHECK_LOCATOR)

    def find_element(self, locator):
        return self.driver.find_element(*locator)
