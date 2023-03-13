from TestSuite.tests.test_base import BaseTest
from TestSuite.test_data import data
import pytest


@pytest.mark.order(5)
class TestViewPost(BaseTest):
    # as of right now this finds the most recently created post

    def test_view_post(self, go_home):
        home_pg = self.pages['home_page']
        view_post_pg = self.pages['view_post_page']

        home_pg.click(home_pg.POST_LINK)

        assert view_post_pg.get_element(
            view_post_pg.POST_TITLE).text == data['blog']['title']
        assert view_post_pg.get_element(
            view_post_pg.POST_CONTENT).text == data['blog']['content']
