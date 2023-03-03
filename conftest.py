import pytest
from selenium import webdriver
from TestSuite.pages.register_page import RegisterPage
from TestSuite.pages.home_page import HomePage
from TestSuite.pages.login_page import LoginPage
from TestSuite.pages.logout_page import LogoutPage

base_url = 'http://localhost:8000'

@pytest.fixture(scope="session")
def pages():
    register_page = RegisterPage(driver)
    home_page = HomePage(driver)
    login_page = LoginPage(driver)
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