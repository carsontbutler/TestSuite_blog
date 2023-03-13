from TestSuite.pages.base_page import BasePage
from selenium.webdriver.common.by import By

class DeletePostPage(BasePage):

    #Properties

    #Locators
    CONFIRM_MSG_LOCATOR = (By.XPATH, '/html/body/main/div/div[1]/div/form/fieldset/h2')
    DELETE_BTN = (By.XPATH, '//button[text()="Yes, Delete"]')
    CANCEL_BTN = (By.XPATH, '//a[text()="Cancel"]')

    #Expected outputs