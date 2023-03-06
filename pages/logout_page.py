from TestSuite.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LogoutPage(BasePage):
    #Properties
    slug = 'logout'

    #Locators
    LOGOUT_MESSAGE = (By.XPATH, '/html/body/main/div/div[1]/h2')

    #Expected outputs
    LOGGED_OUT_TEXT = 'You have been logged out'
    