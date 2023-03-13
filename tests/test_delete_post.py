import pytest
from TestSuite.tests.test_base import BaseTest
from TestSuite.test_data import data, base_url

@pytest.mark.order(7)
class TestDeletePost(BaseTest):

    def test_go_to_delete_post_page(self, go_home):
        """Goes to the delete post page and makes sure the post title is correct"""

        home_pg = self.pages['home_page']
        view_pg = self.pages['view_post_page']
        delete_pg = self.pages['delete_post_page']

        home_pg.click(home_pg.POST_LINK)
        view_pg.click(view_pg.DELETE_BTN)

        assert 'delete' in delete_pg._driver.current_url
        assert data['blog']['title2'] in delete_pg.get_element(delete_pg.CONFIRM_MSG_LOCATOR).text


    def test_cancel_delete_post(self, go_home):
        """Goes to the delete post page, presses cancel, and confirms the post still exists"""

        home_pg = self.pages['home_page']
        delete_pg = self.pages['delete_post_page']
        view_pg = self.pages['view_post_page']

        home_pg.click(home_pg.POST_LINK)
        view_pg.click(view_pg.DELETE_BTN)
        delete_pg.click(delete_pg.CANCEL_BTN)

        assert view_pg.get_element(view_pg.POST_TITLE).text == data['blog']['title2']

    def test_delete_post(self, go_home):
        """Goes to the delete post page, deletes the post, and confirms it was deleted"""

        home_pg = self.pages['home_page']
        delete_pg = self.pages['delete_post_page']
        view_pg = self.pages['view_post_page']

        home_pg.click(home_pg.POST_LINK)
        view_pg.click(view_pg.DELETE_BTN)
        delete_pg.click(delete_pg.DELETE_BTN)

        pass #still need to fix this assertion