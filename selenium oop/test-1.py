# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test_1():
    def test_select_product(self):
        service = Service(executable_path='../chromedriver.exe')
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(service=service, options=options)
        base_url = 'https://www.saucedemo.com/'
        driver.get(base_url)
        # driver.maximize_window()

        print("Start test")

        login_standard_user = "standard_user"
        password_all = "secret_sauce"

        # user_name = driver.find_element(By.XPATH, '//input[@id="user-name"]')
        user_name = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="user-name"]')))
        user_name.send_keys(login_standard_user)
        print("Input Login")

        password = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="password"]')))
        password.send_keys(password_all)
        print("Input Password")

        button_login = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="login-button"]')))
        button_login.click()
        print("Click Login Button")

        select_product = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//button[@id="add-to-cart-sauce-labs-backpack"]')))
        select_product.click()
        print("Click Select Product")

        enter_shopping_cart = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//div[@id="shopping_cart_container"]')))
        enter_shopping_cart.click()
        print("Click Enter Shopping Cart")

        success_test = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//span[@class="title"]')))
        value_success_test = success_test.text
        assert value_success_test == "Your Cart"
        print("Test success")

test = Test_1()
test.test_select_product()





