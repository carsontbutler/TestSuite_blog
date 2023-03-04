import pytest
from selenium import webdriver
from TestSuite.pages.register_page import RegisterPage
from TestSuite.pages.home_page import HomePage
from TestSuite.pages.login_page import LoginPage
from TestSuite.pages.logout_page import LogoutPage
from TestSuite.pages.about_page import AboutPage
from TestSuite.pages.new_post_page import NewPostPage
from TestSuite.pages.view_post_page import ViewPostPage
from TestSuite.test_data import base_url


@pytest.fixture(scope="session")
def pages():
    register_page = RegisterPage(driver)
    home_page = HomePage(driver)
    login_page = LoginPage(driver)
    about_page = AboutPage(driver)
    new_post_page = NewPostPage(driver)
    view_post_page = ViewPostPage(driver)
    logout_page = LogoutPage(driver)
    return locals()

@pytest.fixture(autouse=True, scope="session")
def create_driver():
    global driver
    driver = webdriver.Chrome()
    yield driver
    driver.close()
    driver.quit()

@pytest.fixture
def go_home():
    driver.get(base_url)