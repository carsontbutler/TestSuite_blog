from TestSuite.tests.test_base import BaseTest
from TestSuite.test_data import data
import pytest


@pytest.mark.order(6)
class TestUpdatePost(BaseTest):

    def test_update_post_with_blank_title(self):
        """
        This test will attempt to update the post while leaving the title blank.
        Since the test immediately before this stops on the View Post page, we will
        start the test there (do not need to pass go_home into the method.)
        """

        view_post_pg = self.pages['view_post_page']
        update_post_pg = self.pages['update_post_page']

        view_post_pg.click(view_post_pg.UPDATE_BTN)
        update_post_pg.clear(update_post_pg.TITLE_FIELD)
        update_post_pg.click(update_post_pg.POST_BTN)

        assert update_post_pg.get_element(update_post_pg.TITLE_FIELD).get_attribute(
            "validationMessage") == update_post_pg.BLANK_INPUT_ERROR
        

    def test_update_post_with_blank_content(self):
        """
        This test will attempt to update the post while leaving the content blank.
        Since the test immediately before this cleared the title field, this test starts by
        adding text back to the title field. Then the content field is cleared, and the
        post button is clicked.
        """

        view_post_pg = self.pages['view_post_page']
        update_post_pg = self.pages['update_post_page']

        update_post_pg.send_keys(update_post_pg.TITLE_FIELD, 'My Title')
        update_post_pg.clear(update_post_pg.CONTENT_FIELD)
        update_post_pg.click(update_post_pg.POST_BTN)

        assert update_post_pg.get_element(update_post_pg.CONTENT_FIELD).get_attribute(
            "validationMessage") == update_post_pg.BLANK_INPUT_ERROR
        

    def test_update_post_title_and_content(self):
        """
        This test enters valid input for the title and content, clicks post button,
        and verifies the changes were made successfully
        """

        update_post_pg = self.pages['update_post_page']
        home_pg = self.pages['home_page']

        update_post_pg.send_keys(update_post_pg.TITLE_FIELD, data['blog']['title2'])
        update_post_pg.send_keys(update_post_pg.CONTENT_FIELD, data['blog']['content2'])
        update_post_pg.click(update_post_pg.POST_BTN)
        assert home_pg.get_element(home_pg.POST_LINK).text == data['blog']['title2']
        assert home_pg.get_element(home_pg.POST_CONTENT).text == data['blog']['content2']