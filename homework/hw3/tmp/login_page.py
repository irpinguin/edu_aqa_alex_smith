# selenium 4
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from pages.main_page import MainPage


class LoginPage(MainPage):

    url_login_page = "https://profile.irmag.ru/login/"
    username = "testusr_230928"
    password = "230928"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    mp_login_link_loc = '//span[@class="hidden-sm"]'
    mp_login_btn_loc = '//i[@class="fa fa-sign-in fa-fw"]'
    login_page_sign_loc = '//h2[@class="text-center"]'
    login_page_sign_val = "Аутентификация"
    username_fld_loc = '//input[@id="username"]'
    password_fld_loc = '//input[@id="password"]'
    login_btn_loc = '//button[@class="btn btn-success text-uppercase"]'
    logged_user_sign = '//span[@class="hidden-sm username"]'


    # Getters
    def get_mp_login_page_btn(self):
        return WebDriverWait(self.driver, self.timeout).until\
            (EC.element_to_be_clickable((By.XPATH, self.mp_login_btn_loc)))

    def get_mp_login_page_link(self):
        return WebDriverWait(self.driver, self.timeout).until\
            (EC.element_to_be_clickable((By.XPATH, self.mp_login_link_loc)))

    def get_login_page_sign(self):
        return WebDriverWait(self.driver, self.timeout).until\
            (EC.element_to_be_clickable((By.XPATH, self.login_page_sign_loc)))

    def get_user_name_fld(self):
        return WebDriverWait(self.driver, self.timeout).until\
            (EC.element_to_be_clickable((By.XPATH, self.username_fld_loc)))

    def get_password_fld(self):
        return WebDriverWait(self.driver, self.timeout).until \
            (EC.element_to_be_clickable((By.XPATH, self.password_fld_loc)))

    def get_login_btn(self):
        return WebDriverWait(self.driver, self.timeout).until\
            (EC.element_to_be_clickable((By.XPATH, self.login_btn_loc)))

    def get_logged_user_sign(self):
        return WebDriverWait(self.driver, self.timeout).until \
            (EC.element_to_be_clickable((By.XPATH, self.logged_user_sign)))

    # Actions
    def open_mp_login_page_btn(self):
        self.get_mp_login_page_btn().click()
        print("\tThe button on the Main page to go to the login page is clicked")

    def open_mp_login_page_link(self):
        self.get_mp_login_page_link().click()
        print("\tThe link on the Main page to go to the login page is clicked")

    def input_user_name_fld(self, user_name):
        self.get_user_name_fld().send_keys(user_name)
        print("\tInput user name")

    def input_password_fld(self, password):
        self.get_password_fld().send_keys(password)
        print("\tInput password")

    def click_login_do_btn(self):
        self.get_login_btn().click()
        print("\tThe Login button on the login page is clicked")

    # Methods
    def mp_login_page_load_btn(self):
        # переходим на страницу авторизации через кнопку
        print("Open the Login page via button:")
        start_time = time.time()
        self.open_mp_login_page_btn()
        end_time = time.time()
        self.get_load_time(start_time, end_time, self.timeout)
        self.assert_url(self.url_login_page)
        self.assert_sign(self.get_login_page_sign(), self.login_page_sign_val)
        print("\tOK")

    def mp_login_page_load_link(self):
        # переходим на страницу авторизации через ссылку
        print("Open the Login page via link:")
        start_time = time.time()
        self.open_mp_login_page_link()
        end_time = time.time()
        self.get_load_time(start_time, end_time, self.timeout)
        self.assert_url(self.url_login_page)
        self.assert_sign(self.get_login_page_sign(), self.login_page_sign_val)
        print("\tOK")

    def login_do(self):
        # заполняем поля и нажимаем кнопку Войти
        print(f"Log in with username = {self.username} and password = {self.password}")
        start_time = time.time()
        self.input_user_name_fld(self.username)
        self.input_password_fld(self.password)
        self.click_login_do_btn()
        end_time = time.time()
        self.get_load_time(start_time, end_time, self.timeout)
        self.assert_url(self.url_main_page)
        self.assert_sign(self.get_main_page_sign(), self.main_page_sign_val)
        self.assert_sign(self.get_logged_user_sign(), self.username)
        print("\tOK")


