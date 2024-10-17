from screens.home_page_screen import HomePageScreen
from screens.admin_screen.admin_staffs_screen import StaffPageScreen
from screens.admin_screen.admin_news_screen import NewsPageScreen
from screens.admin_screen.admin_category_screen import CategoryPageScreen
from screens.admin_screen.admin_tag_screen import TagPageScreen
from screens.admin_screen.admin_tarif_screen import TarifPageScreen


class HomePageNavigation(HomePageScreen):

    def home_page_navigation(self, login, password):
        assert self.check_open_home_page(login, password)
