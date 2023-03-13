from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

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

    def clear(self, webelement):
        el = self._wait.until(EC.presence_of_element_located(webelement))
        el.clear()
    
    def get_element(self, webelement):
        el = self._wait.until(EC.presence_of_element_located(webelement))
        return el
    
    def check_for_element(self, webelement):
        try:
            el = self._driver.find_element(webelement)
            return True
        except:
            return False
