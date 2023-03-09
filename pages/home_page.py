from TestSuite.pages.base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):

    #Top Navigation
    LOGIN_LINK = (By.XPATH, '//a[text()="Login"]')
    REGISTER_LINK = (By.XPATH, '//a[text()="Register"]')
    ABOUT_LINK = (By.XPATH, '//a[text()="About"]')
    NEW_POST_LINK = (By.XPATH, '//a[text()="New Post"]')
    PROFILE_LINK = (By.XPATH, '//a[text()="Profile"]')
    LOGOUT_LINK = (By.XPATH, '//a[text()="Logout"]')

    #Posts
    POST_LINK = (By.CLASS_NAME, 'article-title') #Selects the first post on the page
    POST_CONTENT = (By.CLASS_NAME, 'article-content')

    #Misc
    ALERT = (By.CLASS_NAME, 'alert')