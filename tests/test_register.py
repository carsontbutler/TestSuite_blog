import pytest
import time
from TestSuite.tests.test_base import BaseTest

#change to import
data = {
    "username": "C45666",
    "email": "Carson1@t3456.com",
    "password": "Testing123!!"
}

class TestRegister(BaseTest):

    def test_go_to_register_page(self):
        self.pages['home_page'].click_register_link()
        assert self.pages['register_page']._driver.title == self.pages['register_page'].page_title

    def test_register_with_valid_input(self):
        self.pages['register_page'].send_keys(self.pages['register_page'].USERNAME_FIELD, data['username'])
        self.pages['register_page'].send_keys(self.pages['register_page'].EMAIL_FIELD, data['email'])
        self.pages['register_page'].send_keys(self.pages['register_page'].PASSWORD1_FIELD, data['password'])
        self.pages['register_page'].send_keys(self.pages['register_page'].PASSWORD2_FIELD, data['password'])
        self.pages['register_page'].click(self.pages['register_page'].REGISTER_BTN)
        assert self.pages['home_page'].wait_for_text(self.pages['home_page'].ALERT) == self.pages['register_page'].REGISTRATION_SUCCESS_TEXT