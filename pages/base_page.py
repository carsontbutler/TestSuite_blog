class BasePage:
    def __init__(self, driver):
        self._driver = driver

    def check_page_title(self):
        return self._driver.title

