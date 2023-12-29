# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# import sys

from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.client_info_page import ClientInfoPage
from pages.finish_page import FinishPage
from pages.payment_page import PaymentPage

# sys.path.append("/")


def test_buy_product():
    service = Service(executable_path='../chromedriver.exe')
    # options = webdriver.ChromeOptions()
    options = Options()
    options.add_experimental_option("detach", True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=service, options=options)

    print("Start test")

    login = LoginPage(driver)
    login.authorization()

    # enter_shopping_cart = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//div[@id="shopping_cart_container"]')))
    # enter_shopping_cart.click()
    # print("Click Enter Shopping Cart")

    mp = MainPage(driver)
    mp.select_product()

    cp = CartPage(driver)
    cp.click_checkout_btn()

    ci = ClientInfoPage(driver)
    ci.input_info()

    p = PaymentPage(driver)
    p.payment()

    f = FinishPage(driver)
    f.finish('https://www.saucedemo.com/checkout-complete.html')

    driver.quit()




