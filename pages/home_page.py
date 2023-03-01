from TestSuite.pages.base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):

    REGISTER_LINK = (By.XPATH, '//*[@id="navbarToggle"]/div[2]/a[2]')

    def click_register_link(self):
        self.click(self.REGISTER_LINK)