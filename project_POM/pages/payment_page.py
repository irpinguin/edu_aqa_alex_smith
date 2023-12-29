# selenium 4
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from base.base_class import Base


class PaymentPage(Base):

    timeout = 5

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    finish_btn_loc = '//button[@id="finish"]'

    # Getters
    def get_finish_btn(self):
        return WebDriverWait(self.driver, self.timeout).until\
                (EC.element_to_be_clickable((By.XPATH, self.finish_btn_loc)))

    # Actions
    def click_finish_btn(self):
        self.get_finish_btn().click()
        print("Click finish button")

    # Methods
    def payment(self):
        self.get_current_url()
        self.click_finish_btn()
