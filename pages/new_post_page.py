from TestSuite.pages.base_page import BasePage
from selenium.webdriver.common.by import By

class NewPostPage(BasePage):
    
    #Properties
    slug = 'post/new'

    #Locators
    PAGE_HEADER = (By.XPATH, '/html/body/main/div/div[1]/div/form/fieldset/legend')
    TITLE_FIELD = (By.ID, 'id_title')
    CONTENT_FIELD = (By.ID, 'id_content')
    POST_BTN = (By.XPATH, '/html/body/main/div/div[1]/div/form/div/button')

    #Expected outputs
    PAGE_HEADER_TEXT = 'Blog Post'
    BLANK_INPUT_ERROR = 'Please fill out this field.'
    