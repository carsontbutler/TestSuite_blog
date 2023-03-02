import pytest
from .base_page import BasePage
from selenium.webdriver.common.by import By

class RegisterPage(BasePage):
    #Properties
    page_title = 'Django Blog'
    slug = 'register'

    #Locators
    REGISTER_BTN = (By.XPATH, '/html/body/main/div/div[1]/div/form/div/button')
    USERNAME_FIELD = (By.ID, 'id_username')
    EMAIL_FIELD = (By.ID, 'id_email')
    PASSWORD1_FIELD = (By.ID, 'id_password1')
    PASSWORD2_FIELD = (By.ID, 'id_password2')

    #Expected results
    REGISTRATION_SUCCESS_TEXT = 'Your account has been created! You are now able to log in'
