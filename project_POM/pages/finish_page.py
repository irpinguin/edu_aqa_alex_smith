# selenium 4
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from base.base_class import Base


class FinishPage(Base):

    timeout = 5

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    # Getters

    # Actions

    # Methods
    def finish(self, result):
        self.get_current_url()
        self.assert_url(result)
        self.get_screenshot()
