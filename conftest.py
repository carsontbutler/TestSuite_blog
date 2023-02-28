import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from .config import url


# Setup
#The driver and wait are set to autouse=True, so they will be used for every test
#Can always change this later if specific tests are needed with different drivers/tests
@pytest.fixture(autouse=True)
def driver():
    _driver = webdriver.Chrome()
    yield _driver
    _driver.close()

@pytest.fixture(autouse=True)
def wait(driver):
    _wait = WebDriverWait(driver, 4)
    yield _wait