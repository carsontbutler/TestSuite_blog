from TestSuite.pages.base_page import BasePage
from selenium.webdriver.common.by import By

class AboutPage(BasePage):

    #Properties
    slug = 'about'

    #Locators
    PAGE_HEADER = (By.XPATH, '//h1[text()="About this website"]')

    #Expected outputs
    PAGE_HEADER_TEXT = 'About this website'