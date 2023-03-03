import pytest
import time
from TestSuite.tests.test_base import BaseTest
from TestSuite.test_data import data

class TestRegister(BaseTest):

    def test_go_to_register_page(self, go_home):
        home_pg = self.pages['home_page']
        register_pg = self.pages['register_page']

        home_pg.click_register_link()
        assert register_pg._driver.title == register_pg.page_title

    def test_register_with_blank_username(self, go_home):
        register_pg = self.pages['register_page']
        home_pg = self.pages['home_page']

        home_pg.click_register_link()
        register_pg.send_keys(register_pg.EMAIL_FIELD, data['email'])
        register_pg.send_keys(register_pg.PASSWORD1_FIELD, data['password'])
        register_pg.send_keys(register_pg.PASSWORD2_FIELD, data['password'])
        register_pg.click(register_pg.REGISTER_BTN)
        assert register_pg.get_element(register_pg.USERNAME_FIELD).get_attribute("validationMessage") == register_pg.BLANK_INPUT_ERROR
    
    def test_register_with_blank_password_1(self, go_home):
        register_pg = self.pages['register_page']
        home_pg = self.pages['home_page']

        home_pg.click_register_link()
        register_pg.send_keys(register_pg.USERNAME_FIELD, data['username'])
        register_pg.send_keys(register_pg.EMAIL_FIELD, data['email'])
        register_pg.send_keys(register_pg.PASSWORD2_FIELD, data['password'])
        register_pg.click(register_pg.REGISTER_BTN)
        assert register_pg.get_element(register_pg.PASSWORD1_FIELD).get_attribute("validationMessage") == register_pg.BLANK_INPUT_ERROR

    
    def test_register_with_blank_password_2(self, go_home):
        register_pg = self.pages['register_page']
        home_pg = self.pages['home_page']

        home_pg.click_register_link()
        register_pg.send_keys(register_pg.USERNAME_FIELD, data['username'])
        register_pg.send_keys(register_pg.EMAIL_FIELD, data['email'])
        register_pg.send_keys(register_pg.PASSWORD1_FIELD, data['password'])
        register_pg.click(register_pg.REGISTER_BTN)
        assert register_pg.get_element(register_pg.PASSWORD2_FIELD).get_attribute("validationMessage") == register_pg.BLANK_INPUT_ERROR

    def test_register_with_blank_email(self, go_home):
            register_pg = self.pages['register_page']
            home_pg = self.pages['home_page']

            home_pg.click_register_link()
            register_pg.send_keys(register_pg.USERNAME_FIELD, data['username'])
            register_pg.send_keys(register_pg.PASSWORD1_FIELD, data['password'])
            register_pg.send_keys(register_pg.PASSWORD2_FIELD, data['password'])
            register_pg.click(register_pg.REGISTER_BTN)
            assert register_pg.get_element(register_pg.EMAIL_FIELD).get_attribute("validationMessage") == register_pg.BLANK_INPUT_ERROR

    def test_register_with_invalid_email_1(self, go_home):
        register_pg = self.pages['register_page']
        home_pg = self.pages['home_page']

        home_pg.click_register_link()
        register_pg.send_keys(register_pg.USERNAME_FIELD, data['username'])
        register_pg.send_keys(register_pg.EMAIL_FIELD, data['email_invalid_1'])
        register_pg.send_keys(register_pg.PASSWORD1_FIELD, data['password'])
        register_pg.send_keys(register_pg.PASSWORD2_FIELD, data['password'])
        register_pg.click(register_pg.REGISTER_BTN)
        assert register_pg.get_element(register_pg.ERROR_LIST).text == register_pg.INVALID_EMAIL_ERROR_1

    def test_register_with_invalid_email_2(self, go_home):
        register_pg = self.pages['register_page']
        home_pg = self.pages['home_page']

        home_pg.click_register_link()
        register_pg.send_keys(register_pg.USERNAME_FIELD, data['username'])
        register_pg.send_keys(register_pg.EMAIL_FIELD, data['email_invalid_2'])
        register_pg.send_keys(register_pg.PASSWORD1_FIELD, data['password'])
        register_pg.send_keys(register_pg.PASSWORD2_FIELD, data['password'])
        register_pg.click(register_pg.REGISTER_BTN)
        assert register_pg.INVALID_EMAIL_ERROR_2 in register_pg.get_element(register_pg.EMAIL_FIELD).get_attribute("validationMessage")

    def test_register_with_valid_input(self, go_home):
        register_pg = self.pages['register_page']
        home_pg = self.pages['home_page']

        home_pg.click_register_link()
        register_pg.send_keys(register_pg.USERNAME_FIELD, data['username'])
        register_pg.send_keys(register_pg.EMAIL_FIELD, data['email'])
        register_pg.send_keys(register_pg.PASSWORD1_FIELD, data['password'])
        register_pg.send_keys(register_pg.PASSWORD2_FIELD, data['password'])
        register_pg.click(register_pg.REGISTER_BTN)
        assert home_pg.get_element(home_pg.ALERT).text == register_pg.REGISTRATION_SUCCESS_TEXT