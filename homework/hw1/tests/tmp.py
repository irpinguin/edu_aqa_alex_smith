import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_page import BasePage
from base.base_test import BaseTest
# from pages.main_page import MainPage


class MainPage(BasePage):

    PAGE_URL = "https://irmag.ru/"
    TIMEOUT = 10

    # Locators

    # Getters
    # def get_main_page(self):
    #     return WebDriverWait(self.browser, self.TIMEOUT * 10).until \
    #         (lambda driver: driver.execute_script('return document.readyState') == 'complete')

    # def get_main_page_sign(self):
    #     return WebDriverWait(self.browser, self.TIMEOUT).until \
    #         (EC.visibility_of_element_located((By.XPATH, self.main_page_sign_loc)))


MainPage.open()

