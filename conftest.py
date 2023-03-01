import pytest
from selenium import webdriver
from TestSuite.pages.register_page import RegisterPage
from TestSuite.pages.home_page import HomePage

base_url = 'http://localhost:8000'

@pytest.fixture(scope="session")
def pages():
    register_page = RegisterPage(driver)
    home_page = HomePage(driver)
    return locals()

@pytest.fixture(autouse=True, scope="session")
def create_driver():
    global driver
    driver = webdriver.Chrome()
    driver.get(base_url)
    yield driver
    driver.close()
    driver.quit()

