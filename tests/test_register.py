from TestSuite.tests.test_base import BaseTest
from TestSuite.test_data import data, base_url
import pytest


@pytest.mark.order(1)
class TestRegister(BaseTest):

    def test_go_to_register_page(self, go_home):
        home_pg = self.pages['home_page']
        register_pg = self.pages['register_page']
        
        home_pg.click(home_pg.REGISTER_LINK)

        assert register_pg._driver.title == register_pg.page_title
        assert register_pg._driver.current_url == f'{base_url}/{register_pg.slug}/'

    def test_register_with_all_fields_blank(self, go_home):
        register_pg = self.pages['register_page']
        home_pg = self.pages['home_page']

        home_pg.click(home_pg.REGISTER_LINK)
        register_pg.click(register_pg.REGISTER_BTN)

        assert register_pg.get_element(register_pg.USERNAME_FIELD).get_attribute(
            "validationMessage") == register_pg.BLANK_INPUT_ERROR

    def test_register_with_blank_username(self, go_home):
        register_pg = self.pages['register_page']
        home_pg = self.pages['home_page']

        home_pg.click(home_pg.REGISTER_LINK)
        register_pg.send_keys(register_pg.EMAIL_FIELD, data['profile']['email'])
        register_pg.send_keys(register_pg.PASSWORD1_FIELD, data['profile']['password'])
        register_pg.send_keys(register_pg.PASSWORD2_FIELD, data['profile']['password'])
        register_pg.click(register_pg.REGISTER_BTN)

        assert register_pg.get_element(register_pg.USERNAME_FIELD).get_attribute(
            "validationMessage") == register_pg.BLANK_INPUT_ERROR

    def test_register_with_blank_password_1(self, go_home):
        register_pg = self.pages['register_page']
        home_pg = self.pages['home_page']

        home_pg.click(home_pg.REGISTER_LINK)
        register_pg.send_keys(register_pg.USERNAME_FIELD, data['profile']['username'])
        register_pg.send_keys(register_pg.EMAIL_FIELD, data['profile']['email'])
        register_pg.send_keys(register_pg.PASSWORD2_FIELD, data['profile']['password'])
        register_pg.click(register_pg.REGISTER_BTN)

        assert register_pg.get_element(register_pg.PASSWORD1_FIELD).get_attribute(
            "validationMessage") == register_pg.BLANK_INPUT_ERROR

    def test_register_with_blank_password_2(self, go_home):
        register_pg = self.pages['register_page']
        home_pg = self.pages['home_page']

        home_pg.click(home_pg.REGISTER_LINK)
        register_pg.send_keys(register_pg.USERNAME_FIELD, data['profile']['username'])
        register_pg.send_keys(register_pg.EMAIL_FIELD, data['profile']['email'])
        register_pg.send_keys(register_pg.PASSWORD1_FIELD, data['profile']['password'])
        register_pg.click(register_pg.REGISTER_BTN)

        assert register_pg.get_element(register_pg.PASSWORD2_FIELD).get_attribute(
            "validationMessage") == register_pg.BLANK_INPUT_ERROR

    def test_register_with_blank_email(self, go_home):
        register_pg = self.pages['register_page']
        home_pg = self.pages['home_page']

        home_pg.click(home_pg.REGISTER_LINK)
        register_pg.send_keys(register_pg.USERNAME_FIELD, data['profile']['username'])
        register_pg.send_keys(register_pg.PASSWORD1_FIELD, data['profile']['password'])
        register_pg.send_keys(register_pg.PASSWORD2_FIELD, data['profile']['password'])
        register_pg.click(register_pg.REGISTER_BTN)

        assert register_pg.get_element(register_pg.EMAIL_FIELD).get_attribute(
            "validationMessage") == register_pg.BLANK_INPUT_ERROR

    def test_register_with_invalid_email_1(self, go_home):
        register_pg = self.pages['register_page']
        home_pg = self.pages['home_page']

        home_pg.click(home_pg.REGISTER_LINK)
        register_pg.send_keys(register_pg.USERNAME_FIELD, data['profile']['username'])
        register_pg.send_keys(register_pg.EMAIL_FIELD, data['profile']['email_invalid_1'])
        register_pg.send_keys(register_pg.PASSWORD1_FIELD, data['profile']['password'])
        register_pg.send_keys(register_pg.PASSWORD2_FIELD, data['profile']['password'])
        register_pg.click(register_pg.REGISTER_BTN)

        assert register_pg.get_element(
            register_pg.ERROR_LIST).text == register_pg.INVALID_EMAIL_ERROR_1

    def test_register_with_invalid_email_2(self, go_home):
        register_pg = self.pages['register_page']
        home_pg = self.pages['home_page']

        home_pg.click(home_pg.REGISTER_LINK)
        register_pg.send_keys(register_pg.USERNAME_FIELD, data['profile']['username'])
        register_pg.send_keys(register_pg.EMAIL_FIELD, data['profile']['email_invalid_2'])
        register_pg.send_keys(register_pg.PASSWORD1_FIELD, data['profile']['password'])
        register_pg.send_keys(register_pg.PASSWORD2_FIELD, data['profile']['password'])
        register_pg.click(register_pg.REGISTER_BTN)

        assert register_pg.INVALID_EMAIL_ERROR_2 in register_pg.get_element(
            register_pg.EMAIL_FIELD).get_attribute("validationMessage")

    def test_register_with_valid_input(self, go_home):
        register_pg = self.pages['register_page']
        home_pg = self.pages['home_page']

        home_pg.click(home_pg.REGISTER_LINK)
        register_pg.send_keys(register_pg.USERNAME_FIELD, data['profile']['username'])
        register_pg.send_keys(register_pg.EMAIL_FIELD, data['profile']['email'])
        register_pg.send_keys(register_pg.PASSWORD1_FIELD, data['profile']['password'])
        register_pg.send_keys(register_pg.PASSWORD2_FIELD, data['profile']['password'])
        register_pg.click(register_pg.REGISTER_BTN)

        assert home_pg.get_element(
            home_pg.ALERT).text == register_pg.REGISTRATION_SUCCESS_TEXT
