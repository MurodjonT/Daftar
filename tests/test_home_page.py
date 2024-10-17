from actions.home_page_action import HomePageAction
from base_test import TestBase
from config import TestDatas

class TestHomePage(TestBase):

    def test_home_page(self):
        self.go_to_sign_in_page = HomePageAction(self.driver)
        assert self.go_to_sign_in_page.open_home_page()
