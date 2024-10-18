from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select


class Screen:

    def __init__(self, driver):
        self.driver = driver

    def switch_to_iframe_case(self, locator):
        my_elem = (WebDriverWait(self.driver, 50).until(ec.presence_of_element_located(locator)))
        WebDriverWait(self.driver, 50).until(ec.frame_to_be_available_and_switch_to_it(my_elem))

    def is_visible(self, locator):
        return bool(WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator)))

    def is_not_visible(self, locator):
        return bool(WebDriverWait(self.driver, 10).until(ec.invisibility_of_element_located(locator)))

    def get_elem(self, locator):
        return WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(locator))

    def get_elements(self, locator):
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_all_elements_located(locator))

    def is_visible_by_argument(self, locator, argument):
        return bool(WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((locator[0], locator[1].format(argument)))))

    def select_drop(self, locator):
        select = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(locator))
        Select(select)
        return select

    def click(self, locator):
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(locator)).click()

    def click1(self, locator):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator)).click()

    def click_by_pasted_data(self, locator, argument):
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((locator[0], locator[1].format(argument)))).click()

    def submit(self, locator):
        WebDriverWait(self.driver, 50).until(ec.visibility_of_element_located(locator)).submit()

    def enter_data(self, locator, text):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator)).send_keys(text)

    def enter_data1(self, locator, text):
        return WebDriverWait(self.driver, 20).until(ec.presence_of_element_located(locator)).send_keys(text)


    def get_element_text(self, locator):
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator)).text

    def scroll_element(self, locator):
        element = WebDriverWait(self.driver, 100).until(ec.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def clear_field(self, locator):
        element = WebDriverWait(self.driver, timeout=50).until(ec.visibility_of_element_located(locator))
        element.clear()

    def click_by_param(self, locator, argument):
        element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((locator[0], locator[1].format(argument))))
        element.click()
