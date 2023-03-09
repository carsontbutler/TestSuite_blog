from TestSuite.pages.base_page import BasePage
from selenium.webdriver.common.by import By

class ViewPostPage(BasePage):

    #Properties

    #Locators
    POST_TITLE = (By.CLASS_NAME, 'article-title')
    POST_CONTENT = (By.CLASS_NAME, 'article-content')
    UPDATE_BTN = (By.XPATH, '/html/body/main/div/div[1]/article/div/div/div/a[1]')

    #Expected outputs