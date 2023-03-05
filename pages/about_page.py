from TestSuite.pages.base_page import BasePage
from selenium.webdriver.common.by import By

class AboutPage(BasePage):

    #Properties
    slug = 'about'

    #Locators
    PAGE_HEADER = (By.XPATH, '/html/body/main/div/div[1]/h1')

    #Expected outputs
    PAGE_HEADER_TEXT = 'About this website'