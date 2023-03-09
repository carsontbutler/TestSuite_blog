from TestSuite.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LogoutPage(BasePage):
    
    #Properties
    slug = 'logout'

    #Locators
    LOGOUT_MESSAGE = (By.XPATH, '//h2[text()="You have been logged out"]')

    #Expected outputs
    LOGGED_OUT_TEXT = 'You have been logged out'