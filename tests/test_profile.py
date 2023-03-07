import pytest
from TestSuite.tests.test_base import BaseTest
from TestSuite.test_data import data, base_url, base_dir
from TestSuite.helpers import *


class TestProfile(BaseTest):


    def test_go_to_profile_page(self, go_home):
        """Goes to the profile page and verifies the current url matches the expected result."""

        home_pg = self.pages['home_page']
        profile_pg = self.pages['profile_page']

        home_pg.click(home_pg.PROFILE_LINK)

        assert profile_pg._driver.current_url == f'{base_url}/{profile_pg.slug}/'


    def test_check_current_profile_info(self, go_home):
        """
        Verifies that the information on the profile page matches the 
        profile created during test_register_with_valid_input test
        """

        home_pg = self.pages['home_page']
        profile_pg = self.pages['profile_page']

        home_pg.click(home_pg.PROFILE_LINK)

        assert profile_pg.get_element(
            profile_pg.PROFILE_NAME).text == data['profile']['username']
        assert profile_pg.get_element(profile_pg.USERNAME_FIELD).get_attribute(
            'value') == data['profile']['username']
        assert profile_pg.get_element(profile_pg.EMAIL_FIELD).get_attribute(
            'value') == data['profile']['email']
        assert profile_pg.get_element(
            profile_pg.IMAGE_TITLE).text == 'default.jpg'


# USERNAME TESTS
    def test_change_username(self, go_home):
        """Changes the username with valid input and verifies it was changed successfully"""

        home_pg = self.pages['home_page']
        profile_pg = self.pages['profile_page']

        home_pg.click(home_pg.PROFILE_LINK)
        profile_pg.send_keys(profile_pg.USERNAME_FIELD,
                             data['profile']['username_changed'])
        profile_pg.click(profile_pg.UPDATE_BTN)

        assert profile_pg.get_element(
            profile_pg.ALERT).text == profile_pg.UPDATE_SUCCESS_TEXT
        assert profile_pg.get_element(profile_pg.USERNAME_FIELD).get_attribute(
            'value') == data['profile']['username_changed']


    def test_change_username_invalid(self, go_home):
        """Attempts to change username to one with invalid characters and verifies the attempt fails."""

        home_pg = self.pages['home_page']
        profile_pg = self.pages['profile_page']

        home_pg.click(home_pg.PROFILE_LINK)
        profile_pg.send_keys(profile_pg.USERNAME_FIELD,
                             generate_invalid_username())
        profile_pg.click(profile_pg.UPDATE_BTN)

        assert profile_pg.get_element(
            profile_pg.USERNAME_ERROR_LOCATOR).text == profile_pg.INVALID_USERNAME_ERROR_1


    def test_change_long_username(self, go_home):
        """
        Attempts to input a username of length > 150 and verifies
          the text in the field stops at length=150
        """

        home_pg = self.pages['home_page']
        profile_pg = self.pages['profile_page']

        home_pg.click(home_pg.PROFILE_LINK)
        profile_pg.send_keys(profile_pg.USERNAME_FIELD,
                             generate_long_username())

        assert len(profile_pg.get_element(
            profile_pg.USERNAME_FIELD).get_attribute('value')) == 150


    def test_change_username_preexisting(self, go_home):
        """
        Attempts to change username to one that is taken by another user
        and verifies that the attempt failed.
        """

        home_pg = self.pages['home_page']
        profile_pg = self.pages['profile_page']

        home_pg.click(home_pg.PROFILE_LINK)
        profile_pg.send_keys(profile_pg.USERNAME_FIELD,
                             data['profile2']['username'])

        profile_pg.click(profile_pg.UPDATE_BTN)
        assert profile_pg.get_element(profile_pg.USERNAME_ERROR_LOCATOR).text == profile_pg.USERNAME_EXISTS_ERROR


# EMAIL TESTS
    def test_change_email(self, go_home):
        """Changes the email to a valid email address and verifies the attempt succeeded."""

        home_pg = self.pages['home_page']
        profile_pg = self.pages['profile_page']

        home_pg.click(home_pg.PROFILE_LINK)
        profile_pg.send_keys(profile_pg.EMAIL_FIELD,
                             data['profile']['email_changed'])
        profile_pg.click(profile_pg.UPDATE_BTN)

        assert profile_pg.get_element(
            profile_pg.ALERT).text == profile_pg.UPDATE_SUCCESS_TEXT
        assert profile_pg.get_element(profile_pg.EMAIL_FIELD).get_attribute(
            'value') == data['profile']['email_changed']


    def test_change_email_invalid_1(self, go_home):
        """
        Attempts to change the email to one that is missing a domain on the end 
        and verifies that it fails.
        """
        home_pg = self.pages['home_page']
        profile_pg = self.pages['profile_page']

        home_pg.click(home_pg.PROFILE_LINK)
        profile_pg.send_keys(profile_pg.EMAIL_FIELD,
                             data['profile']['email_invalid_1'])
        profile_pg.click(profile_pg.UPDATE_BTN)

        assert profile_pg.get_element(profile_pg.EMAIL_ERROR_LOCATOR).text == profile_pg.INVALID_EMAIL_ERROR_1

        
    def test_change_email_invalid_2(self, go_home):
        """Attempts to change the email to one that is missing the '@' sign and verifies that it fails."""

        home_pg = self.pages['home_page']
        profile_pg = self.pages['profile_page']

        home_pg.click(home_pg.PROFILE_LINK)
        profile_pg.send_keys(profile_pg.EMAIL_FIELD,
                             data['profile']['email_invalid_2'])
        profile_pg.click(profile_pg.UPDATE_BTN)

        assert profile_pg.INVALID_EMAIL_ERROR_2 in profile_pg.get_element(profile_pg.EMAIL_FIELD).get_attribute("validationMessage")


# PROFILE PIC TESTS
    def test_change_profile_pic_to_invalid_file(self, go_home):
        """
        Attempts to change the profile pic using a filetype that isn't accepted 
        and verifies that the attempt fails.
        """

        home_pg = self.pages['home_page']
        profile_pg = self.pages['profile_page']
        invalid_file = data['profile']['invalid_file_name']

        home_pg.click(home_pg.PROFILE_LINK)
        profile_pg.send_keys(profile_pg.IMAGE_FIELD,
                             f'{base_dir}/media/{invalid_file}')
        profile_pg.click(profile_pg.UPDATE_BTN)

        assert profile_pg.get_element(profile_pg.FILE_ERROR_LOCATOR).text == profile_pg.INVALID_FILE_ERROR_1

    
    def test_change_profile_pic(self, go_home):
        """Changes the profile pic and verifies the attempt was successful."""

        home_pg = self.pages['home_page']
        profile_pg = self.pages['profile_page']
        profile_pic = data['profile']['new_profile_image_name']

        home_pg.click(home_pg.PROFILE_LINK)
        profile_pg.send_keys(profile_pg.IMAGE_FIELD,
                             f'{base_dir}/media/{profile_pic}')
        profile_pg.click(profile_pg.UPDATE_BTN)

        assert profile_pg.get_element(
            profile_pg.ALERT).text == profile_pg.UPDATE_SUCCESS_TEXT
        assert profile_pg.get_element(
            profile_pg.IMAGE_TITLE).text != 'default.jpg'
        assert data['profile']['new_profile_image_name'].split('.')[0] in profile_pg.get_element(
            profile_pg.IMAGE_TITLE).text
