from TestSuite.pages.base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):


    #Top Navigation
    LOGIN_LINK = (By.XPATH, '//*[@id="navbarToggle"]/div[2]/a[1]')
    REGISTER_LINK = (By.XPATH, '//*[@id="navbarToggle"]/div[2]/a[2]')
    ABOUT_LINK = (By.XPATH, '//*[@id="navbarToggle"]/div[1]/a[2]')
    LOGOUT_LINK = (By.XPATH, '//*[@id="navbarToggle"]/div[2]/a[3]')

    #Misc
    ALERT = (By.CLASS_NAME, 'alert')