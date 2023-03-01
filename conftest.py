import pytest
from selenium import webdriver
from TestSuite.pages.register_page import RegisterPage

base_url = 'http://localhost:8000'

@pytest.fixture
def pages():
    register_page = RegisterPage(driver)
    return locals()

@pytest.fixture(autouse=True)
def create_driver():
    global driver
    driver = webdriver.Chrome()
    driver.get(base_url)
    yield driver
    driver.close()
    driver.quit()

