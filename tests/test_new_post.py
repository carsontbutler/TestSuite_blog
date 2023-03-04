import pytest
from TestSuite.tests.test_base import BaseTest
from TestSuite.test_data import data

@pytest.mark.order(4)
class TestNewPost(BaseTest):

    def test_go_to_new_post_page(self, go_home):
        home_pg = self.pages['home_page']
        new_post_pg = self.pages['new_post_page']

        home_pg.click(home_pg.NEW_POST_LINK)

        assert new_post_pg.get_element(
            new_post_pg.PAGE_HEADER).text == new_post_pg.PAGE_HEADER_TEXT
