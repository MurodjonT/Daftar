import time
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from screens.screen import Screen
from selenium.webdriver.common.by import By


class HomePageScreen(Screen):

    def __init__(self, driver):
        super().__init__(driver)

    login_field = (By.XPATH, '//*[@id="formatted-phone-input"]')
    password_field = (By.XPATH, '//*[@id="password"]')
    login_btn = (By.XPATH, '//*[@type="submit"]')
    success_path = (By.XPATH, "//h1[contains(@class, 'welcome_page_title')]")
    select_lang = (By.XPATH, "//*[@name='lang']//parent::div")
    selected_eng_lang = (By.XPATH, "//div[@id='menu-lang']/div[3]/ul/li[3]/img")
    logo_admin_top = (By.XPATH, '//*[@class="MuiAvatar-root MuiAvatar-circular mui-style-ltr-1u3scve-MuiAvatar-root"]')
    in_logo_balance = (By.XPATH, "//*[contains(text(), 'Balance')]")
    client_balance_option_select = (By.XPATH, '//input[@placeholder="Shops"]')
    selected_client_balance = (By.XPATH, "//li[@id=':r3:-option-0']/div")


    def check_open_home_page(self, login, password, client_balance):
        time.sleep(2)
        self.click(self.login_field)
        time.sleep(1)
        self.enter_data1(self.login_field, login)
        time.sleep(1)
        self.enter_data1(self.password_field, password)
        time.sleep(1)
        self.click(self.login_btn)
        self.click(self.select_lang)
        time.sleep(1)
        self.click(self.selected_eng_lang)
        time.sleep(1)
        self.click(self.logo_admin_top)
        time.sleep(1)
        self.click(self.in_logo_balance)
        self.click(self.client_balance_option_select)
        time.sleep(2)
        self.enter_data1(self.client_balance_option_select, client_balance).send_keys(Keys.RETURN)

        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.success_path)
            )
            return True
        except Exception as e:
            print(f"Error : {e}")
            return False


