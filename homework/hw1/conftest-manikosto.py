# manikosto
# Pytest-фикстуры на человеческом
# https://habr.com/ru/articles/716248/
# https://github.com/manikosto/LiveCoding
#
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
import time


@pytest.fixture
def connect_to_db():
    connection = "Established"
    return connection

# @pytest.fixture()
# def generate_data():
    # login = f"autotest_{time.time()}@hyper.org"     # Генерирует логин
    # password = "512"                                # Назначает пароль
    # return {"login":login, "password": password}    # Возвращает логин и пароль


# Причина, по которой в pycharm runner не передается фикстура
# https://intellij-support.jetbrains.com/hc/en-us/community/posts/12897247432338-PyCharm-unable-to-find-fixtures-in-conftest-py
@pytest.fixture
def generate_data(request):
    request.cls.login = f"autotest_{time.time()}@hyper.org" # Генерирует логин
    request.cls.password = "512"                            # Назначает пароль


# @pytest.fixture(scope="function", autouse=True)
@pytest.fixture(scope="function")
def get_driver(request):
    service = Service(executable_path='utilities/chromedriver-116.0.5845.96.exe')
    # options = Options()
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    # options.add_argument("--disable-dev-shm-usage")
    # options.add_argument("--window-size=1920,1080")
    options.add_experimental_option("detach", True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=service, options=options)
    request.cls.driver = driver
    yield driver
    # driver.quit()