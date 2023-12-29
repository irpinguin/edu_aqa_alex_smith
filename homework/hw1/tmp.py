from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from pages.catalog_page import CatalogPage
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage


service = Service(executable_path='../chromedriver.exe')
options = Options()
options.add_experimental_option("detach", True)
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=service, options=options)

print("Start test")
print("=" * 30)

print("Start test for Main page")
mp = MainPage(driver)
# mp.main_page_load()
# mp.open_hamburger_catalog()
# mp.main_page_return()
# mp.open_link_catalog()
print("-" * 30)

print("Start test for Login page")
lp = LoginPage(driver)
mp.main_page_load()
lp.mp_login_page_load_btn()
# mp.main_page_return()
# lp.mp_login_page_load_link()
# lp.mp_login_page_load_btn()
lp.login_do()
print("-" * 30)

# print("Start test for Registration page")
# rp = RegistrationPage(driver)
# mp.main_page_load()
# lp.mp_login_page_load_btn()
# rp.open_registration_page()
# rp.input_fields()
# rp.registration_do()
# print("-" * 30)

print("Start test for Catalog page")
cp = CatalogPage(driver)
mp.main_page_load()
cp.open_link_catalog()
cp.main_page_return()
cp.open_hamburger_catalog()
print("-" * 30)