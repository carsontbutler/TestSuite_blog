import pytest
from .base_page import BasePage
from selenium.webdriver.common.by import By

class RegisterPage(BasePage):

    register_page_btn = (By.XPATH, '//*[@id="navbarToggle"]/div[2]/a[2]')
    register_btn = (By.XPATH, '/html/body/main/div/div[1]/div/form/div/button')

    page_title = 'Django Blog'
    slug = 'register'
    
