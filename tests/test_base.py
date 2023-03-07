import pytest

class BaseTest:

    @pytest.fixture(autouse=True)
    def injector(self, pages):
        # instantiates pages object, and data readers
        self.pages = pages
