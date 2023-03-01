import pytest
from os.path import join
from selenium import webdriver
from TestSuite.pages.application import Application
from TestSuite.test_data.utils import get_yaml


# Setup
@pytest.fixture(scope='session')
def driver():
    _driver = webdriver.Chrome()
    yield _driver
    _driver.close()

@pytest.fixture(scope="session")
def data():
    relative_path_from_here_to_yaml = join("test_data", 'data.yaml')
    data = get_yaml(__file__, relative_path_from_here_to_yaml)
    return data

@pytest.fixture(scope="session")
def app(driver: webdriver, data):
    app_data = {"driver": driver, "data": data}
    return Application(app_data)
