from TestSuite.tests.test_base import BaseTest
from TestSuite.test_data import data


class TestLogin(BaseTest):

    def test_login_with_blank_password(self, go_home):
        home_pg = self.pages['home_page']
        login_pg = self.pages['login_page']

        home_pg.click_login_link()
        login_pg.send_keys(login_pg.USERNAME_FIELD, data['username'])
        login_pg.click(login_pg.LOGIN_BTN)

        assert login_pg.get_element(login_pg.PASSWORD_FIELD).get_attribute(
            'validationMessage') == login_pg.BLANK_INPUT_ERROR

    def test_login_with_blank_password(self, go_home):
        home_pg = self.pages['home_page']
        login_pg = self.pages['login_page']

        home_pg.click_login_link()
        login_pg.send_keys(login_pg.PASSWORD_FIELD, data['password'])
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

    def login_with_valid_credentials(self, go_home):
        home_pg = self.pages['home_page']
        login_pg = self.pages['login_page']

        home_pg.click_login_link()
        