from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self._driver = driver
        self._wait = WebDriverWait(self._driver, 5)

    def click(self, webelement):
        el = self._wait.until(EC.element_to_be_clickable(webelement))
        el.click()

    def send_keys(self, webelement, text):
        el = self._wait.until(EC.element_to_be_clickable(webelement))
        el.clear()
        el.send_keys(text)
    
    def get_element(self, webelement):
        el = self._wait.until(EC.presence_of_element_located(webelement))
        return el