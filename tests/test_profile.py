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
        assert profile_pg.get_element(profile_pg.PROFILE_NAME).text == data['register']['username']
        assert profile_pg.get_element(profile_pg.USERNAME_FIELD).get_attribute('value') == data['register']['username']
        assert profile_pg.get_element(profile_pg.EMAIL_FIELD).get_attribute('value') == data['register']['email']
        assert profile_pg.get_element(profile_pg.IMAGE_TITLE).text == 'default.jpg'

    