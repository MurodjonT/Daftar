import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as serv


@pytest.fixture(params=['chrome'], scope='class')
def init_driver(request):
    global web_driver
    s = serv("/Users/murodjonturobov/Downloads/chromedriver-mac-arm64-4/chromedriver")
    web_driver = webdriver.Chrome(service=s)
    web_driver.maximize_window()
    web_driver.get("https://test.daftar.uz/login")
    web_driver.implicitly_wait(10)
    request.cls.driver = web_driver
    yield
    time.sleep(5)
    web_driver.close()

