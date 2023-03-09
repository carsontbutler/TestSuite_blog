from TestSuite.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    
    # Properties
    slug = 'login'
    page_title = 'Django Blog'

    # Locators
    USERNAME_FIELD = (By.ID, 'id_username')
    PASSWORD_FIELD = (By.ID, 'id_password')
    LOGIN_BTN = (By.XPATH, '//button[text()="Login"]')
    FORGOT_PASSWORD_BTN = (By.XPATH, '//a[text()="Forgot password?"]')
    SIGN_UP_BTN = (By.XPATH, '//a[text()="Sign Up Now"]')

    # Expected outputs
    BLANK_INPUT_ERROR = 'Please fill out this field.'
    INVALID_CREDENTIALS_ERROR = 'Please enter a correct username and password.'
