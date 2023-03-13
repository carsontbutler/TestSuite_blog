from TestSuite.pages.base_page import BasePage
from selenium.webdriver.common.by import By

class ViewPostPage(BasePage):

    #Properties

    #Locators
    POST_TITLE = (By.CLASS_NAME, 'article-title')
    POST_CONTENT = (By.CLASS_NAME, 'article-content')
    UPDATE_BTN = (By.XPATH, '//a[contains(@href, "update")]')
    DELETE_BTN = (By.XPATH, '//a[text()="Delete"]')

    #Expected outputs