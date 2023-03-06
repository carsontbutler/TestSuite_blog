import pytest
from TestSuite.tests.test_base import BaseTest
from TestSuite.test_data import data, base_url


@pytest.mark.order(4)
class TestNewPost(BaseTest):

    def test_go_to_new_post_page(self, go_home):
        """Goes to the new post page and verifies the page header and current url match expected results."""

        home_pg = self.pages['home_page']
        new_post_pg = self.pages['new_post_page']

        home_pg.click(home_pg.NEW_POST_LINK)

        assert new_post_pg.get_element(
            new_post_pg.PAGE_HEADER).text == new_post_pg.PAGE_HEADER_TEXT
        assert new_post_pg._driver.current_url == f'{base_url}/{new_post_pg.slug}/' 

    def test_create_new_post_with_blank_title(self, go_home):
        """Attempts to create a new post with an empty title and verifies the attempt fails."""
        
        home_pg = self.pages['home_page']
        new_post_pg = self.pages['new_post_page']

        home_pg.click(home_pg.NEW_POST_LINK)
        new_post_pg.send_keys(new_post_pg.CONTENT_FIELD,
                              data['blog']['content'])
        new_post_pg.click(new_post_pg.POST_BTN)
        
        assert new_post_pg.get_element(new_post_pg.TITLE_FIELD).get_attribute(
            'validationMessage') == new_post_pg.BLANK_INPUT_ERROR

    def test_create_new_post_with_blank_content(self, go_home):
        """Attempts to create a new post with empty content and verifies the attempt fails."""

        home_pg = self.pages['home_page']
        new_post_pg = self.pages['new_post_page']

        home_pg.click(home_pg.NEW_POST_LINK)
        new_post_pg.send_keys(new_post_pg.TITLE_FIELD, data['blog']['title'])
        new_post_pg.click(new_post_pg.POST_BTN)

        assert new_post_pg.get_element(new_post_pg.CONTENT_FIELD).get_attribute(
            'validationMessage') == new_post_pg.BLANK_INPUT_ERROR

    def test_create_new_post_with_valid_input(self, go_home):
        """Creates a new post with valid inputs and verifies the post is created successfully."""


        home_pg = self.pages['home_page']
        new_post_pg = self.pages['new_post_page']
        view_post_pg = self.pages['view_post_page']

        home_pg.click(home_pg.NEW_POST_LINK)
        new_post_pg.send_keys(new_post_pg.TITLE_FIELD, data['blog']['title'])
        new_post_pg.send_keys(new_post_pg.CONTENT_FIELD,
                              data['blog']['content'])
        new_post_pg.click(new_post_pg.POST_BTN)

        assert view_post_pg.get_element(
            view_post_pg.POST_TITLE).text == data['blog']['title']
        assert view_post_pg.get_element(
            view_post_pg.POST_CONTENT).text == data['blog']['content']