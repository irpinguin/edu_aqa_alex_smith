# selenium 4
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from base.base_class import Base


class ClientInfoPage(Base):

    timeout = 5
    first_name = "Имя"
    last_name = "Фамилия"
    zip_code = "664002"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    first_name_fld_loc = '//input[@id="first-name"]'
    last_name_fld_loc = '//input[@id="last-name"]'
    zip_code_fld_loc = '//input[@id="postal-code"]'
    continue_btn_loc = '//input[@id="continue"]'

    # Getters
    def get_first_name_fld(self):
        return WebDriverWait(self.driver, self.timeout).until\
                (EC.element_to_be_clickable((By.XPATH, self.first_name_fld_loc)))

    def get_last_name_fld(self):
        return WebDriverWait(self.driver, self.timeout).until\
                (EC.element_to_be_clickable((By.XPATH, self.last_name_fld_loc)))

    def get_zip_code_fld(self):
        return WebDriverWait(self.driver, self.timeout).until\
                (EC.element_to_be_clickable((By.XPATH, self.zip_code_fld_loc)))

    def get_continue_btn(self):
        return WebDriverWait(self.driver, self.timeout).until\
                (EC.element_to_be_clickable((By.XPATH, self.continue_btn_loc)))

    # Actions
    def input_first_name(self, first_name):
        self.get_first_name_fld().send_keys(first_name)
        print("Input first name")

    def input_last_name(self, last_name):
        self.get_last_name_fld().send_keys(last_name)
        print("Input last name")

    def input_zip_code(self, zip_code):
        self.get_zip_code_fld().send_keys(zip_code)
        print("Input postal code")

    def click_continue_btn(self):
        self.get_continue_btn().click()
        print("Click continue button")

    # Methods
    def input_info(self):
        self.get_current_url()
        self.input_first_name(self.first_name)
        self.input_last_name(self.last_name)
        self.input_zip_code(self.zip_code)
        self.click_continue_btn()

