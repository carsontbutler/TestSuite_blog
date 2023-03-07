from TestSuite.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ProfilePage(BasePage):

    # Properties
    slug = 'profile'
    page_title = 'Django Blog'

    # Locators
    PROFILE_NAME = (By.CLASS_NAME, 'account-heading')
    USERNAME_FIELD = (By.ID, 'id_username')
    EMAIL_FIELD = (By.ID, 'id_email')
    IMAGE_TITLE = (By.XPATH, '//*[@id="div_id_image"]/div[1]/div/span/a')
    IMAGE_FIELD = (By.ID, 'id_image')
    UPDATE_BTN = (By.XPATH, '/html/body/main/div/div[1]/div/form/div/button')
    ALERT = (By.XPATH, '/html/body/main/div/div[1]/div[1]')
    USERNAME_ERROR_LOCATOR = (By.ID, 'error_1_id_username')
    EMAIL_ERROR_LOCATOR = (By.ID, 'error_1_id_email')
    FILE_ERROR_LOCATOR = (By.ID, 'error_1_id_image')

    # Expected outputs
    UPDATE_SUCCESS_TEXT = 'Your account has been updated!'
    INVALID_USERNAME_ERROR_1 = 'Enter a valid username. This value may contain only letters, numbers, and @/./+/-/_ characters.'
    USERNAME_EXISTS_ERROR = 'A user with that username already exists.'
    INVALID_EMAIL_ERROR_1 = 'Enter a valid email address.'
    INVALID_FILE_ERROR_1 = 'Upload a valid image. The file you uploaded was either not an image or a corrupted image.'
    INVALID_EMAIL_ERROR_2 = "Please include an '@' in the email"
    