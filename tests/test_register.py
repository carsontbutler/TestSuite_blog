import pytest
from TestSuite.tests.test_base import BaseTest

class TestRegister(BaseTest):

    def test_check_page_title(self):
        assert self.pages['register_page']._driver.title == self.pages['register_page'].page_title