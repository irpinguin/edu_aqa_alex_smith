# selenium 4
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from base.base_class import Base


class MainPage(Base):

    timeout = 5

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    select_product_1_loc = '//button[@id="add-to-cart-sauce-labs-backpack"]'
    select_product_2_loc = '//button[@id="add-to-cart-sauce-labs-bike-light"]'
    select_product_3_loc = '//button[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'
    cart_loc = '//div[@id="shopping_cart_container"]'
    hamburger_menu_loc = '//button[@id="react-burger-menu-btn"]'
    link_about_loc = '//a[@id="about_sidebar_link"]'

    # Getters
    def get_select_product_1(self):
        return WebDriverWait(self.driver, self.timeout).until\
                (EC.element_to_be_clickable((By.XPATH, self.select_product_1_loc)))

    def get_select_product_2(self):
        return WebDriverWait(self.driver, self.timeout).until\
                (EC.element_to_be_clickable((By.XPATH, self.select_product_2_loc)))

    def get_select_product_3(self):
        return WebDriverWait(self.driver, self.timeout).until\
                (EC.element_to_be_clickable((By.XPATH, self.select_product_3_loc)))

    def get_cart(self):
        return WebDriverWait(self.driver, self.timeout).until\
                (EC.element_to_be_clickable((By.XPATH, self.cart_loc)))

    def get_hamburger_menu(self):
        return WebDriverWait(self.driver, self.timeout).until\
                (EC.element_to_be_clickable((By.XPATH, self.hamburger_menu_loc)))

    def get_link_about(self):
        return WebDriverWait(self.driver, self.timeout).until\
                (EC.element_to_be_clickable((By.XPATH, self.link_about_loc)))

    # Actions
    def click_select_product_1(self):
        self.get_select_product_1().click()
        print("Click select product 1 button")

    def click_select_product_2(self):
        self.get_select_product_2().click()
        print("Click select product 2 button")

    def click_select_product_3(self):
        self.get_select_product_3().click()
        print("Click select product 3 button")

    def click_cart(self):
        self.get_cart().click()
        print("Click cart button")

    def click_hamburger_menu(self):
        self.get_hamburger_menu().click()
        print("Click hamburger menu button")

    def click_link_about(self):
        self.get_link_about().click()
        print("Click link About")

    # Methods
    def select_product_1(self):
        self.get_current_url()
        self.click_select_product_1()
        self.click_cart()

    def select_product_2(self):
        self.get_current_url()
        self.click_select_product_2()
        self.click_cart()

    def select_product_3(self):
        self.get_current_url()
        self.click_select_product_3()
        self.click_cart()

    def select_hamburger_menu_about(self):
        self.get_current_url()
        self.click_hamburger_menu()
        self.click_link_about()