import datetime
from colorama import init, Fore, Style
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


class Base:
    TIMEOUT = 10

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10, poll_frequency=1)
        # Инициализируем colorama для правильного вывода в win10
        init(autoreset=True)

    # Method get current url
    def get_current_url(self):
        get_url = self.driver.current_url
        print(f"\tCurrent url {get_url}.")

    # Method assert page sign
    def assert_sign(self, sign, result):
        value_sign = sign.text
        assert result in value_sign
        print(f"\tThe specified sign '{sign.text}' is found on the page.")

    # Method get screenshot
    def get_screenshot(self):
        # возвращает имя скриншота
        now_date = datetime.datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S")
        name_screenshot = 'screenshot ' + now_date + '.png'
        self.driver.save_screenshot('./screen/' + name_screenshot)
        return name_screenshot

    # Method assert url
    def assert_url(self, url):
        get_url = self.driver.current_url
        assert get_url == url
        print(f"\tThe specified url '{url}' corresponds to the current one '{get_url}'.")

    # Method measure time
    def get_load_time(self, start_time_sec:float, end_time_sec:float, timeout_sec:int = 3):
        # Выводит разницу во времени в секундах и если она меньше таймаута, то выводит ее красным шрифтом
        elapsed_time = end_time_sec - start_time_sec
        if elapsed_time < timeout_sec:
            print(f'\tThe load time: {end_time_sec - start_time_sec:.2f} sec.')
        else:
            print(f'\t{Fore.RED}The load time: {end_time_sec - start_time_sec:.2f} sec '
                  f'is longer than the expected timeout {timeout_sec} sec{Style.RESET_ALL}.')
        return elapsed_time
