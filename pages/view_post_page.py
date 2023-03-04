from TestSuite.pages.base_page import BasePage
from selenium.webdriver.common.by import By

class ViewPostPage(BasePage):

    #Properties

    #Locators
    POST_TITLE = (By.CLASS_NAME, 'article-title')
    POST_CONTENT = (By.CLASS_NAME, 'article-content')

    #Expected outputs