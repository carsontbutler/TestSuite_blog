from TestSuite.pages.base_page import BasePage
from selenium.webdriver.common.by import By

class ProfilePage(BasePage):
    
    #Properties
    slug = 'profile'
    page_title = 'Django Blog'

    #Locators
    PROFILE_NAME = (By.CLASS_NAME, 'account-heading')
    USERNAME_FIELD = (By.ID, 'id_username')
    EMAIL_FIELD = (By.ID, 'id_email')
    IMAGE_TITLE = (By.XPATH, '/html/body/main/div/div[1]/div/form/fieldset/a')
    IMAGE_FIELD = (By.ID, 'id_image')
    UPDATE_BTN = (By.XPATH, '/html/body/main/div/div[1]/div/form/div/button')
    ALERT = (By.XPATH, '/html/body/main/div/div[1]/div[1]')

    #Expected outputs
    UPDATE_SUCCESS_TEXT = 'Your account has been updated!'