import pytest
from TestSuite.tests.test_base import BaseTest
from TestSuite.test_data import data, base_url, base_dir
from TestSuite.helpers import *


class TestProfile(BaseTest):

    def test_go_to_profile_page(self, go_home):
        home_pg = self.pages['home_page']
        profile_pg = self.pages['profile_page']

        home_pg.click(home_pg.PROFILE_LINK)

        assert profile_pg._driver.current_url == f'{base_url}/{profile_pg.slug}/'

    def test_check_current_profile_info(self, go_home):
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
        home_pg = self.pages['home_page']
        profile_pg = self.pages['profile_page']

        home_pg.click(home_pg.PROFILE_LINK)
        profile_pg.send_keys(profile_pg.USERNAME_FIELD,
                             generate_invalid_username())
        profile_pg.click(profile_pg.UPDATE_BTN)

        assert profile_pg.get_element(
            profile_pg.USERNAME_ERROR_LOCATOR).text == profile_pg.INVALID_USERNAME_ERROR_1

    def test_change_long_username(self, go_home):
        home_pg = self.pages['home_page']
        profile_pg = self.pages['profile_page']

        home_pg.click(home_pg.PROFILE_LINK)
        profile_pg.send_keys(profile_pg.USERNAME_FIELD,
                             generate_long_username())

        assert len(profile_pg.get_element(
            profile_pg.USERNAME_FIELD).get_attribute('value')) == 150

    def test_change_username_preexisting(self, go_home):
        # enter username that already exists and make sure it is rejected
        pass

    # EMAIL TESTS
    def test_change_email(self, go_home):
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
        # change email to data["profile"]["email_invalid_1"]
        pass

    def test_change_email_invalid_2(self, go_home):
        # change email to data["profile"]["email_invalid_2"]
        pass

    # PROFILE PIC TESTS
    def test_change_profile_pic(self, go_home):
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
