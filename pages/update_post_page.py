from TestSuite.pages.base_page import BasePage
from selenium.webdriver.common.by import By

class UpdatePostPage(BasePage):
    
    #Properties


    #Locators
    TITLE_FIELD = (By.ID, 'id_title')
    CONTENT_FIELD = (By.ID, 'id_content')
    POST_BTN = (By.XPATH, '//button[text()="Post"]')

    #Expected outputs
    BLANK_INPUT_ERROR = 'Please fill out this field.'