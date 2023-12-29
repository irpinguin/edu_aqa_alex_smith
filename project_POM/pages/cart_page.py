# selenium 4
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from base.base_class import Base


class CartPage(Base):

    timeout = 5

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    checkout_btn_loc = '//button[@id="checkout"]'


    # Getters
    def get_checkout_btn(self):
        return WebDriverWait(self.driver, self.timeout).until\
                (EC.element_to_be_clickable((By.XPATH, self.checkout_btn_loc)))

    # Actions
    def click_checkout_btn(self):
        self.get_checkout_btn().click()
        print("Click checkout button")

    # Methods
    def product_confirmation(self):
        self.get_current_url()
        self.click_checkout_btn()
