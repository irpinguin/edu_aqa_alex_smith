# selenium 4
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# from base.base_class import Base
from base.base_page import BasePage


class MainPage(BasePage):

    PAGE_URL = "https://irmag.ru/"
    TIMEOUT = 10
    # url_catalog_page = "https://irmag.ru/cat/"
    # url_catalog_subcategory_page = "https://irmag.ru/cat/1249639/"
    #
    # def __init__(self, browser):
    #     # super().__init__(driver)
    #     self.browser = browser

    # Locators
    # main_page_load_widget_loc = '//iframe[@title="chat widget"]'                        # with chat widget
    # main_page_sign_loc = '//div[@class="pl-10"]'
    # main_page_sign_val = "ИРМАГ"
    main_page_sign_loc = '//div[@id="index-last-blog-posts"]/h2'
    main_page_sign_val = 'Новые обзоры в блоге'
    # hamburger_btn_loc = '//span[@class="hamburger hidden-xs"]'
    # hamburger_category_loc = '//nav[@id="catalog-menu"]/ul/li[2]/a'                     # Бытовая химия
    # hamburger_subcategory_loc = '//nav[@id="catalog-menu"]/ul/li[2]/div/dl[3]/dd[4]/a'  # От тараканов и муравьев
    # catalog_sign_loc = '//section[@class="catalog container"]/h1'
    # catalog_sign_val = "Каталог"
    # catalog_subcategory_sign_val = "От тараканов и муравьев"
    # catalog_loc = '//span[@class="hidden-sm btn-text"]'

    # Getters
    def get_main_page(self):
        return WebDriverWait(self.browser, self.TIMEOUT * 10).until \
            (lambda driver: driver.execute_script('return document.readyState') == 'complete')
            # EC.element_to_be_clickable((By.XPATH, self.main_page_load_widget_loc)))

    def get_main_page_sign(self):
        return WebDriverWait(self.browser, self.TIMEOUT).until \
            (EC.visibility_of_element_located((By.XPATH, self.main_page_sign_loc)))

    # def get_hamburger_menu(self):
    #     return WebDriverWait(self.driver, self.timeout).until \
    #         (EC.element_to_be_clickable((By.XPATH, self.hamburger_btn_loc)))
    #
    # def get_hamburger_category(self):
    #     return WebDriverWait(self.driver, self.timeout).until\
    #             (EC.element_to_be_clickable((By.XPATH, self.hamburger_category_loc)))
    #
    # def get_hamburger_subcategory(self):
    #     return WebDriverWait(self.driver, self.timeout).until\
    #             (EC.element_to_be_clickable((By.XPATH, self.hamburger_subcategory_loc)))
    #
    # def get_catalog_sign(self):
    #     return WebDriverWait(self.driver, self.timeout).until\
    #             (EC.element_to_be_clickable((By.XPATH, self.catalog_sign_loc)))
    #
    # def get_catalog_page(self):
    #     return WebDriverWait(self.driver, self.timeout).until \
    #         (EC.element_to_be_clickable((By.XPATH, self.catalog_loc)))

    # Actions
    # def open_hamburger_menu(self):
    #     action = ActionChains(self.driver)
    #     hamburger = self.get_hamburger_menu()
    #     action.move_to_element(hamburger).perform()
    #     print("The hamburger menu is open")
    #
    # def select_hamburger_category(self):
    #     action = ActionChains(self.driver)
    #     hamburger_category = self.get_hamburger_category()
    #     action.move_to_element(hamburger_category).perform()
    #     print("The category in hamburger menu selected")
    #
    # def select_hamburger_subcategory(self):
    #     action = ActionChains(self.driver)
    #     hamburger_subcategory = self.get_hamburger_subcategory()
    #     action.move_to_element(hamburger_subcategory).perform()
    #     print("The subcategory in hamburger menu selected")
    #
    # def open_hamburger_subcategory(self):
    #     self.get_hamburger_subcategory().click()
    #     print("\tThe link to the Catalog subcategory page in hamburger menu is clicked")
    #
    # def open_catalog_page(self):
    #     self.get_catalog_page().click()
    #     print("\tThe link to the Catalog page is clicked")

    # Methods
    def open_main_page(self):
        print("Open the Main page:")
        # ждем когда страница прогрузится целиком, долго грузится виджет чата
        start_time = time.time()
        self.browser.get(self.PAGE_URL)
        self.get_main_page()
        end_time = time.time()
        # self.get_load_time(start_time, end_time, self.TIMEOUT)
        # self.assert_url(self.PAGE_URL)
        # self.assert_sign(self.get_main_page_sign(), self.main_page_sign_val)
        print("\tOK")

    # def open_hamburger_catalog(self):
    #     # открываем гамбургер меню, выбираем категорию и подкатегорию
    #     self.open_hamburger_menu()
    #     self.select_hamburger_category()
    #     self.select_hamburger_subcategory()
    #
    #     # открываем каталог подкатегории
    #     print("Open the Catalog subcategory page from hamburger menu:")
    #     start_time = time.time()
    #     self.open_hamburger_subcategory()
    #     end_time = time.time()
    #     self.get_load_time(start_time, end_time, self.timeout)
    #     self.assert_url(self.url_catalog_subcategory_page)
    #     self.assert_sign(self.get_catalog_sign(), self.catalog_subcategory_sign_val)
    #     print("\tOK")

    def main_page_return(self):
        # переходим на главную страницу
        print("Return to the Main page:")
        start_time = time.time()
        # self.driver.back()
        self.browser.get(self.PAGE_URL)
        end_time = time.time()
        # self.get_load_time(start_time, end_time, self.TIMEOUT)
        # self.assert_url(self.PAGE_URL)
        print("\tOK")

    # def open_link_catalog(self):
    #     # открываем каталог через ссылку
    #     print("Open the Catalog page from link:")
    #     start_time = time.time()
    #     self.driver.get(self.url_catalog_page)
    #     self.get_catalog_page()
    #     end_time = time.time()
    #     self.get_load_time(start_time, end_time, self.timeout)
    #     self.assert_url(self.url_catalog_page)
    #     self.assert_sign(self.get_catalog_sign(), self.catalog_sign_val)
    #     print("\tOK")



