from TestSuite.pages.base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):


    #Top Navigation
    LOGIN_LINK = (By.XPATH, '//*[@id="navbarToggle"]/div[2]/a[1]')
    REGISTER_LINK = (By.XPATH, '//*[@id="navbarToggle"]/div[2]/a[2]')

    #Misc
    ALERT = (By.CLASS_NAME, 'alert')


    def click_register_link(self):
        self.click(self.REGISTER_LINK)

    def click_login_link(self):
        self.click(self.LOGIN_LINK)