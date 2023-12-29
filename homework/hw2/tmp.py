import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    HOST = "https://opensource-demo.orangehrmlive.com/web/index.php"
    LOGIN_PAGE = f"{HOST}/auth/login"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10, poll_frequency=1)

    def open(self):
        self.driver.get(self.LOGIN_PAGE)


def driver(request):
    service = Service(executable_path='../project_hw/chromedriver-116.0.5845.96.exe')
    options = Options()
    # options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1400,1050")
    options.add_experimental_option("detach", True)
    # options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # driver = webdriver.Chrome(service=service, options=options)
    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver
