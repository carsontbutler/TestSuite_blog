import pytest
from TestSuite.tests.test_base import BaseTest
from TestSuite.test_data import data, base_url


@pytest.mark.order(2)
class TestLogin(BaseTest):


    def test_go_to_login_page(self, go_home):
        """Goes to the login page and verifies the page title and current url match the expected results."""

        home_pg = self.pages['home_page']
        login_pg = self.pages['login_page']

        home_pg.click(home_pg.LOGIN_LINK)
        
        assert login_pg._driver.title == login_pg.page_title
        assert login_pg._driver.current_url == f'{base_url}/{login_pg.slug}/'


    def test_login_with_blank_password(self, go_home):
        """Attempts to login with an empty password and verifies the login attempt fails."""

        home_pg = self.pages['home_page']
        login_pg = self.pages['login_page']

        home_pg.click(home_pg.LOGIN_LINK)
        login_pg.send_keys(login_pg.USERNAME_FIELD, data['profile']['username'])
        login_pg.click(login_pg.LOGIN_BTN)

        assert login_pg.get_element(login_pg.PASSWORD_FIELD).get_attribute(
            'validationMessage') == login_pg.BLANK_INPUT_ERROR


    def test_login_with_blank_username(self, go_home):
        """Attempts to login with an empty username and verifies the login attempt fails."""

        home_pg = self.pages['home_page']
        login_pg = self.pages['login_page']

        home_pg.click(home_pg.LOGIN_LINK)
        login_pg.send_keys(login_pg.PASSWORD_FIELD, data['profile']['password'])
        login_pg.click(login_pg.LOGIN_BTN)

        assert login_pg.get_element(login_pg.USERNAME_FIELD).get_attribute(
            'validationMessage') == login_pg.BLANK_INPUT_ERROR


    def test_login_with_all_fields_blank(self, go_home):
        """Attempts to login with all fields empty and verifies login fails."""
        
        home_pg = self.pages['home_page']
        login_pg = self.pages['login_page']

        home_pg.click(home_pg.LOGIN_LINK)
        login_pg.click(login_pg.LOGIN_BTN)

        assert login_pg.get_element(login_pg.USERNAME_FIELD).get_attribute(
            'validationMessage') == login_pg.BLANK_INPUT_ERROR


    def test_login_with_valid_credentials(self, go_home):
        """Attempts to login with valid credentials and verifies login attempt is successful."""

        home_pg = self.pages['home_page']
        login_pg = self.pages['login_page']

        home_pg.click(home_pg.LOGIN_LINK)
        login_pg.send_keys(login_pg.USERNAME_FIELD, data['profile']['username'])
        login_pg.send_keys(login_pg.PASSWORD_FIELD, data['profile']['password'])
        login_pg.click(login_pg.LOGIN_BTN)

        assert home_pg.get_element(home_pg.LOGOUT_LINK).text == 'Logout'

