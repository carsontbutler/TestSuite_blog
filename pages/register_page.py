from .base_page import BasePage
from selenium.webdriver.common.by import By

class RegisterPage(BasePage):
    
    #Properties
    page_title = 'Django Blog'
    slug = 'register'

    #Locators
    REGISTER_BTN = (By.XPATH, '//button[text()="Sign Up"]')
    USERNAME_FIELD = (By.ID, 'id_username')
    EMAIL_FIELD = (By.ID, 'id_email')
    PASSWORD1_FIELD = (By.ID, 'id_password1')
    PASSWORD2_FIELD = (By.ID, 'id_password2')
    USERNAME_ERROR_LOCATOR = (By.ID, 'error_1_id_username')
    EMAIL_ERROR_LOCATOR = (By.ID, 'error_1_id_email')

    #Expected outputs
    REGISTRATION_SUCCESS_TEXT = 'Your account has been created! You are now able to log in'
    BLANK_INPUT_ERROR = 'Please fill out this field.'
    INVALID_USERNAME_ERROR_1 = 'Enter a valid username.'
    INVALID_EMAIL_ERROR_1 = 'Enter a valid email address.'
    INVALID_EMAIL_ERROR_2 = "Please include an '@' in the email"
