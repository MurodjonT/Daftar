import time

from navigations.home_page_navigation import HomePageNavigation


class HomePageAction(HomePageNavigation):

    def open_home_page(self):
        self.home_page_navigation("972600106", "password1")
        return True
