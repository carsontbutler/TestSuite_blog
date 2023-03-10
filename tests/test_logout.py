import pytest
from TestSuite.tests.test_base import BaseTest
from TestSuite.test_data import base_url

@pytest.mark.order("last")
class TestLogout(BaseTest):


    def test_logout(self, go_home): 
        """Attempts to log out and verifies logout was successful"""
        
        home_pg = self.pages['home_page']
        logout_pg = self.pages['logout_page']
        
        home_pg.click(home_pg.LOGOUT_LINK)
        
        assert logout_pg.get_element(logout_pg.LOGOUT_MESSAGE).text == logout_pg.LOGGED_OUT_TEXT
        assert logout_pg._driver.current_url == f'{base_url}/{logout_pg.slug}/'