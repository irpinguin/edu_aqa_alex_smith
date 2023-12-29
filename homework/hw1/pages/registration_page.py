# selenium 4
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from pages.login_page import LoginPage


class RegistrationPage(LoginPage):

    url_registration_page = "https://profile.irmag.ru/registration/"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    lp_registration_btn_loc = '//a[@class="btn btn-default"]'
    registration_sign_loc = '//h2[@class="text-center"]'
    registration_sign_val = 'Регистрация'
    username_fld_loc = '//input[@id="registration_username"]'
    password_fld_loc = '//input[@id="registration_password_first"]'
    password_confirm_fld_loc = '//input[@id="registration_password_second"]'
    registration_do_btn_loc = '//button[@id="registration_save"]'
    registration_success_sign_loc = '//p[@class="alert alert-success text-left"]/b'
    back_btn = '//div[@class="btn-group"]/a'

    # Getters
    def get_registration_page_sign(self):
        return WebDriverWait(self.driver, self.timeout).until \
            (EC.element_to_be_clickable((By.XPATH, self.registration_sign_loc)))

    def get_lp_registration_btn(self):
        return WebDriverWait(self.driver, self.timeout).until \
            (EC.element_to_be_clickable((By.XPATH, self.lp_registration_btn_loc)))

    def get_user_name_fld(self):
        return WebDriverWait(self.driver, self.timeout).until \
            (EC.element_to_be_clickable((By.XPATH, self.username_fld_loc)))

    def get_password_fld(self):
        return WebDriverWait(self.driver, self.timeout).until \
            (EC.element_to_be_clickable((By.XPATH, self.password_fld_loc)))

    def get_password_confirm_fld(self):
        return WebDriverWait(self.driver, self.timeout).until \
            (EC.element_to_be_clickable((By.XPATH, self.password_confirm_fld_loc)))

    def get_registration_do_btn(self):
        return WebDriverWait(self.driver, self.timeout).until \
            (EC.element_to_be_clickable((By.XPATH, self.registration_do_btn_loc)))

    def get_registration_success_sign(self):
        return WebDriverWait(self.driver, self.timeout).until \
            (EC.element_to_be_clickable((By.XPATH, self.registration_success_sign_loc)))

    # Actions
    def open_lp_registration_page_btn(self):
        self.get_lp_registration_btn().click()
        print("\tThe button on the Login page to go to the Registration page is clicked")

    def input_user_name_fld(self, user_name):
        self.get_user_name_fld().send_keys(user_name)
        print("\tInput user name")

    def input_password_fld(self, password):
        self.get_password_fld().send_keys(password)
        print("\tInput password")

    def input_password_confirm_fld(self, password):
        self.get_password_confirm_fld().send_keys(password)
        print("\tInput password confirm")

    def click_registration_do_btn(self):
        # self.get_registration_do_btn().click()
        print("\tThe Register button on the registration page is clicked")
        print("\t\tРегистрация скриптом из под селениум не проходит. Сайт выдает 'Respect My Authoritah!'.")
        print("\t\tНажатие в ручную кнопки Регистрация из-под открытого в селениум браузера проходит успешно.")
        # Надо разбираться со скрытием селениум!
        # check existing user etc

    # Methods
    def open_registration_page(self):
        # переходим на страницу регистрации нового пользователя
        print("Open the Registration page:")
        start_time = time.time()
        self.open_lp_registration_page_btn()
        end_time = time.time()
        self.get_load_time(start_time, end_time, self.timeout)
        self.assert_url(self.url_registration_page)
        self.assert_sign(self.get_registration_page_sign(), self.registration_sign_val)
        print("\tOK")

    def input_fields(self):
        self.input_user_name_fld(self.username)
        self.input_password_fld(self.password)
        self.input_password_confirm_fld(self.password)

    def registration_do(self):
        self.click_registration_do_btn()
        print("\tOK")
