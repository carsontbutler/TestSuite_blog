import pytest
from TestSuite.tests.test_base import BaseTest
from TestSuite.test_data import data, base_url


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
