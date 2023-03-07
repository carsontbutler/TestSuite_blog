from TestSuite.tests.test_base import BaseTest
from TestSuite.test_data import data, base_url
from TestSuite.helpers import *
import pytest


@pytest.mark.order(1)
class TestRegister(BaseTest):


    def test_go_to_register_page(self, go_home):
        """Goes to the register page and verifies page title and current url match expected results."""

        home_pg = self.pages['home_page']
        register_pg = self.pages['register_page']

        home_pg.click(home_pg.REGISTER_LINK)

        assert register_pg._driver.title == register_pg.page_title
        assert register_pg._driver.current_url == f'{base_url}/{register_pg.slug}/'


    def test_register_with_all_fields_blank(self, go_home):
        """
        Attempts to register a new user while leaving all inputs blank 
        and verifies the attempt fails.
        """

        register_pg = self.pages['register_page']
        home_pg = self.pages['home_page']

        home_pg.click(home_pg.REGISTER_LINK)
        register_pg.click(register_pg.REGISTER_BTN)

        assert register_pg.get_element(register_pg.USERNAME_FIELD).get_attribute(
            "validationMessage") == register_pg.BLANK_INPUT_ERROR


    def test_register_with_blank_username(self, go_home):
        """
        Attempts to register a new user while leaving the username field blank
          and verifies the attempt fails.
        """

        register_pg = self.pages['register_page']
        home_pg = self.pages['home_page']

        home_pg.click(home_pg.REGISTER_LINK)
        register_pg.send_keys(register_pg.EMAIL_FIELD,
                              data['profile']['email'])
        register_pg.send_keys(register_pg.PASSWORD1_FIELD,
                              data['profile']['password'])
        register_pg.send_keys(register_pg.PASSWORD2_FIELD,
                              data['profile']['password'])
        register_pg.click(register_pg.REGISTER_BTN)

        assert register_pg.get_element(register_pg.USERNAME_FIELD).get_attribute(
            "validationMessage") == register_pg.BLANK_INPUT_ERROR


    def test_register_with_invalid_username(self, go_home):
        """
        Attempts to register a new user with invalid characters in the username 
        and verifies the attempt fails.
        """

        register_pg = self.pages['register_page']
        home_pg = self.pages['home_page']

        home_pg.click(home_pg.REGISTER_LINK)
        register_pg.send_keys(register_pg.USERNAME_FIELD,
                              generate_invalid_username())
        register_pg.send_keys(register_pg.EMAIL_FIELD,
                              data['profile']['email'])
        register_pg.send_keys(register_pg.PASSWORD1_FIELD,
                              data['profile']['password'])
        register_pg.send_keys(register_pg.PASSWORD2_FIELD,
                              data['profile']['password'])
        register_pg.click(register_pg.REGISTER_BTN)

        assert register_pg.INVALID_USERNAME_ERROR_1 in register_pg.get_element(
            register_pg.USERNAME_ERROR_LOCATOR).text


    def test_register_with_long_username(self, go_home):
        """
        Attempts to type a username with length > 150 and verifies
        the input length stops at 150
        """
        register_pg = self.pages['register_page']
        home_pg = self.pages['home_page']

        home_pg.click(home_pg.REGISTER_LINK)
        register_pg.send_keys(register_pg.USERNAME_FIELD,
                              generate_long_username())

        assert len(register_pg.get_element(
            register_pg.USERNAME_FIELD).get_attribute('value')) == 150


    def test_register_with_blank_password_1(self, go_home):
        """
        Attempts to register a new user while leaving the first password field blank 
        and verifies that the attempt fails.
        """

        register_pg = self.pages['register_page']
        home_pg = self.pages['home_page']

        home_pg.click(home_pg.REGISTER_LINK)
        register_pg.send_keys(register_pg.USERNAME_FIELD,
                              data['profile']['username'])
        register_pg.send_keys(register_pg.EMAIL_FIELD,
                              data['profile']['email'])
        register_pg.send_keys(register_pg.PASSWORD2_FIELD,
                              data['profile']['password'])
        register_pg.click(register_pg.REGISTER_BTN)

        assert register_pg.get_element(register_pg.PASSWORD1_FIELD).get_attribute(
            "validationMessage") == register_pg.BLANK_INPUT_ERROR


    def test_register_with_blank_password_2(self, go_home):
        """
        Attempts to register a new user while leaving the second password field blank 
        and verifies that the attempt fails.
        """

        register_pg = self.pages['register_page']
        home_pg = self.pages['home_page']

        home_pg.click(home_pg.REGISTER_LINK)
        register_pg.send_keys(register_pg.USERNAME_FIELD,
                              data['profile']['username'])
        register_pg.send_keys(register_pg.EMAIL_FIELD,
                              data['profile']['email'])
        register_pg.send_keys(register_pg.PASSWORD1_FIELD,
                              data['profile']['password'])
        register_pg.click(register_pg.REGISTER_BTN)

        assert register_pg.get_element(register_pg.PASSWORD2_FIELD).get_attribute(
            "validationMessage") == register_pg.BLANK_INPUT_ERROR


    def test_register_with_blank_email(self, go_home):
        """
        Attempts to register a new user while leaving the email field blank 
        and verifies that the attempt fails.
        """

        register_pg = self.pages['register_page']
        home_pg = self.pages['home_page']

        home_pg.click(home_pg.REGISTER_LINK)
        register_pg.send_keys(register_pg.USERNAME_FIELD,
                              data['profile']['username'])
        register_pg.send_keys(register_pg.PASSWORD1_FIELD,
                              data['profile']['password'])
        register_pg.send_keys(register_pg.PASSWORD2_FIELD,
                              data['profile']['password'])
        register_pg.click(register_pg.REGISTER_BTN)

        assert register_pg.get_element(register_pg.EMAIL_FIELD).get_attribute(
            "validationMessage") == register_pg.BLANK_INPUT_ERROR


    def test_register_with_invalid_email_1(self, go_home):
        """
        Attempts to register a new user using an invalid email address (no domain) 
        and verifies that the attempt fails.
        """

        register_pg = self.pages['register_page']
        home_pg = self.pages['home_page']

        home_pg.click(home_pg.REGISTER_LINK)
        register_pg.send_keys(register_pg.USERNAME_FIELD,
                              data['profile']['username'])
        register_pg.send_keys(register_pg.EMAIL_FIELD,
                              data['profile']['email_invalid_1'])
        register_pg.send_keys(register_pg.PASSWORD1_FIELD,
                              data['profile']['password'])
        register_pg.send_keys(register_pg.PASSWORD2_FIELD,
                              data['profile']['password'])
        register_pg.click(register_pg.REGISTER_BTN)

        assert register_pg.get_element(
            register_pg.EMAIL_ERROR_LOCATOR).text == register_pg.INVALID_EMAIL_ERROR_1


    def test_register_with_invalid_email_2(self, go_home):
        """
        Attempts to register a new user using an invalid email address (no @) 
        and verifies that the attempt fails.
        """

        register_pg = self.pages['register_page']
        home_pg = self.pages['home_page']

        home_pg.click(home_pg.REGISTER_LINK)
        register_pg.send_keys(register_pg.USERNAME_FIELD,
                              data['profile']['username'])
        register_pg.send_keys(register_pg.EMAIL_FIELD,
                              data['profile']['email_invalid_2'])
        register_pg.send_keys(register_pg.PASSWORD1_FIELD,
                              data['profile']['password'])
        register_pg.send_keys(register_pg.PASSWORD2_FIELD,
                              data['profile']['password'])
        register_pg.click(register_pg.REGISTER_BTN)

        assert register_pg.INVALID_EMAIL_ERROR_2 in register_pg.get_element(
            register_pg.EMAIL_FIELD).get_attribute("validationMessage")


    def test_register_with_valid_input(self, go_home):
        """Registers a new user with valid input and verifies the attempt was successful."""

        register_pg = self.pages['register_page']
        home_pg = self.pages['home_page']

        home_pg.click(home_pg.REGISTER_LINK)
        register_pg.send_keys(register_pg.USERNAME_FIELD,
                              data['profile']['username'])
        register_pg.send_keys(register_pg.EMAIL_FIELD,
                              data['profile']['email'])
        register_pg.send_keys(register_pg.PASSWORD1_FIELD,
                              data['profile']['password'])
        register_pg.send_keys(register_pg.PASSWORD2_FIELD,
                              data['profile']['password'])
        register_pg.click(register_pg.REGISTER_BTN)

        assert home_pg.get_element(
            home_pg.ALERT).text == register_pg.REGISTRATION_SUCCESS_TEXT
