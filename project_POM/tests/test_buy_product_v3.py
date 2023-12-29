# selenium 4
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import sys

from pages.cart_page import CartPage
from pages.client_info_page import ClientInfoPage
from pages.finish_page import FinishPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.payment_page import PaymentPage

sys.path.append("/")


# @pytest.mark.order(3)
def test_buy_product_1(set_up):
    service = Service(executable_path='../chromedriver.exe')
    # options = webdriver.ChromeOptions()
    options = Options()
    options.add_experimental_option("detach", True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=service, options=options)

    print("Start test 1")

    login = LoginPage(driver)
    login.authorization()

    mp = MainPage(driver)
    mp.select_product_1()

    cp = CartPage(driver)
    cp.click_checkout_btn()

    ci = ClientInfoPage(driver)
    ci.input_info()

    p = PaymentPage(driver)
    p.payment()

    f = FinishPage(driver)
    f.finish('https://www.saucedemo.com/checkout-complete.html')

    print("Finish test 1")
    driver.quit()


# @pytest.mark.order(1)
def test_buy_product_2(set_group):
    service = Service(executable_path='../chromedriver.exe')
    # service = Service(executable_path='C:\\Users\\ipinguin\\Edu\\Stepik\\Project_POM\\chromedriver.exe')
    # options = webdriver.ChromeOptions()
    options = Options()
    options.add_experimental_option("detach", True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=service, options=options)

    print("Start test 2")

    login = LoginPage(driver)
    login.authorization()

    mp = MainPage(driver)
    mp.select_product_2()

    cp = CartPage(driver)
    cp.click_checkout_btn()

    print("Finish test 2")
    driver.quit()


# @pytest.mark.order(2)
def test_buy_product_3():
    service = Service(executable_path='../chromedriver.exe')
    # options = webdriver.ChromeOptions()
    options = Options()
    options.add_experimental_option("detach", True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=service, options=options)

    print("Start test 3")

    login = LoginPage(driver)
    login.authorization()

    mp = MainPage(driver)
    mp.select_product_3()

    cp = CartPage(driver)
    cp.click_checkout_btn()

    print("Finish test 3")
    driver.quit()


