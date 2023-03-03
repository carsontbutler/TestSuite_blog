import pytest
from TestSuite.tests.test_base import BaseTest
from TestSuite.test_data import data
from TestSuite.pages.logout_page import LogoutPage


@pytest.mark.order(2)
class TestLogin(BaseTest):

    def test_login_with_blank_password(self, go_home):
        home_pg = self.pages['home_page']
        login_pg = self.pages['login_page']

        home_pg.click_login_link()
        login_pg.send_keys(login_pg.USERNAME_FIELD, data['login']['username'])
        login_pg.click(login_pg.LOGIN_BTN)

        assert login_pg.get_element(login_pg.PASSWORD_FIELD).get_attribute(
            'validationMessage') == login_pg.BLANK_INPUT_ERROR

    def test_login_with_blank_password(self, go_home):
        home_pg = self.pages['home_page']
        login_pg = self.pages['login_page']

        home_pg.click_login_link()
        login_pg.send_keys(login_pg.PASSWORD_FIELD, data['login']['password'])
        login_pg.click(login_pg.LOGIN_BTN)

        assert login_pg.get_element(login_pg.USERNAME_FIELD).get_attribute(
            'validationMessage') == login_pg.BLANK_INPUT_ERROR

    def test_login_with_all_fields_blank(self, go_home):
        home_pg = self.pages['home_page']
        login_pg = self.pages['login_page']

        home_pg.click_login_link()
        login_pg.click(login_pg.LOGIN_BTN)

        assert login_pg.get_element(login_pg.USERNAME_FIELD).get_attribute(
            'validationMessage') == login_pg.BLANK_INPUT_ERROR

    def test_login_with_valid_credentials(self, go_home):
        home_pg = self.pages['home_page']
        login_pg = self.pages['login_page']

        home_pg.click_login_link()
        login_pg.send_keys(login_pg.USERNAME_FIELD, data['login']['username'])
        login_pg.send_keys(login_pg.PASSWORD_FIELD, data['login']['password'])
        login_pg.click(login_pg.LOGIN_BTN)

        assert home_pg.get_element(home_pg.LOGOUT_LINK).text == 'Logout'

    def test_logout(self):
        home_pg = self.pages['home_page']
        logout_pg = self.pages['logout_page']
        
        home_pg.click(home_pg.LOGOUT_LINK)
        assert logout_pg.get_element(logout_pg.LOGOUT_MESSAGE).text == logout_pg.LOGGED_OUT_TEXT
