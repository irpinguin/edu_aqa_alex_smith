# selenium 4
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from base.base_class import Base


class LoginPage(Base):

    url = 'https://www.saucedemo.com/'
    timeout = 5

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    user_name_loc = '//input[@id="user-name"]'
    password_loc = '//input[@id="password"]'
    login_btn_loc = '//input[@id="login-button"]'
    main_page_sign = 'Products'
    main_page_sign_loc = '//span[@class="title"]'

    # Getters
    def get_user_name(self):
        return WebDriverWait(self.driver, self.timeout).until\
                (EC.element_to_be_clickable((By.XPATH, self.user_name_loc)))

    def get_password(self):
        return WebDriverWait(self.driver, self.timeout).until\
                (EC.element_to_be_clickable((By.XPATH, self.password_loc)))

    def get_login_btn(self):
        return WebDriverWait(self.driver, self.timeout).until\
                (EC.element_to_be_clickable((By.XPATH, self.login_btn_loc)))

    def get_main_sign(self):
        return WebDriverWait(self.driver, self.timeout).until\
                (EC.element_to_be_clickable((By.XPATH, self.main_page_sign_loc)))

    # Actions
    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("Input user name")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")

    def click_login_btn(self):
        self.get_login_btn().click()
        print("Click login button")

    # Methods
    def authorization(self):
        self.driver.get(self.url)
        # self.driver.maximize_window()
        self.get_current_url()
        self.input_user_name("standard_user")
        self.input_password("secret_sauce")
        self.click_login_btn()
        self.assert_sign(self.get_main_sign(), self.main_page_sign)

