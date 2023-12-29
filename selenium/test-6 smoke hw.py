# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import random
import time

# Открываем браузер
service = Service(executable_path='../chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

# Авторизуемся
login_standard_user = "standard_user"
password_all = "secret_sauce"

user_name = driver.find_element(By.XPATH, '//input[@id="user-name"]')
user_name.send_keys(login_standard_user)
print("Input Login")

password = driver.find_element(By.XPATH, '//input[@id="password"]')
password.send_keys(password_all)
print("Input Password")

login_btn = driver.find_element(By.XPATH, '//input[@id="login-button"]')
login_btn.click()
print("Click Login Button")

# Даем время на то, чтобы страница с товарами прогрузилась
time.sleep(2)

# Найти все элементы с информацией о товарах
product_elements = driver.find_elements(By.CSS_SELECTOR, '.inventory_item')

# Случайным образом выбрать два товара и добавить их в корзину
product_list = []
random_products = random.sample(product_elements, 2)

for product in random_products:
    product_name = product.find_element(By.XPATH, ".//div[@class='inventory_item_name']").text
    product_price = product.find_element(By.XPATH, ".//div[@class='inventory_item_price']").text
    product_price = product_price.replace('$', '')  # Удалить символ '$' из цены
    product_dict = {'name': product_name, 'price': product_price}
    product_list.append(product_dict)

    # Добавить товар в корзину
    add_to_cart_button = product.find_element(By.XPATH, ".//button[@class='btn btn_primary btn_small btn_inventory']")
    add_to_cart_button.click()
    # time.sleep(2)  # Пауза для обновления содержимого корзины

# Вывести список товаров и их цен
for product in product_list:
    print(f"Добавлен товар: {product['name']}")
    print(f"Цена товара: {product['price']}")

# product = driver.find_element(By.XPATH, '//div[@class="inventory_container"]')
# //div[@class="inventory_container"]/div/div[1]/div[2]/div[1]
# //div[@class="inventory_container"]/div/div[2]/div[2]/div[1]
# value_product = product.text
# print(value_product)

# product_1 = driver.find_element(By.XPATH, '//a[@id="item_4_title_link"]')
# value_product_1 = product_1.text
# print(value_product_1)
#
# price_product_1 = driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[1]/div[2]/div[2]/div')
# value_price_product_1 = price_product_1.text
# print(value_price_product_1)
#
# select_product_1 = driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-backpack"]')
# select_product_1.click()
# print("Select Product 1")
#
cart_btn = driver.find_element(By.XPATH, '//span[@class="shopping_cart_badge"]')
cart_btn.click()
print("Enter Cart")
#
# '''
# Info Cart Product 1
# '''
# finish_product_1 = driver.find_element(By.XPATH, '//a[@id="item_4_title_link"]')
# value_cart_product_1 = finish_product_1.text
# print(value_cart_product_1)
# assert value_product_1 == value_cart_product_1
# print("Info Cart Product 1 OK")
#
# price_cart_product_1 = driver.find_element(By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]/div[3]/div[2]/div[2]/div')
# value_price_cart_product_1 = price_cart_product_1.text
# print(value_price_cart_product_1)
# assert value_price_product_1 == value_price_cart_product_1
# print("Info Cart Price Product 1 OK")
#
# checkout_btn = driver.find_element(By.XPATH, '//button[@id="checkout"]')
# checkout_btn.click()
# print("Click Checkout Button")
#
# '''
# Select User Info
# '''
# first_name = driver.find_element(By.XPATH, '//input[@id="first-name"]')
# first_name.send_keys("Igor")
# print("Input First Name")
#
# last_name = driver.find_element(By.XPATH, '//input[@id="last-name"]')
# last_name.send_keys("Andreev")
# print("Input Last Name")
#
# zip_code = driver.find_element(By.XPATH, '//input[@id="postal-code"]')
# zip_code.send_keys("664001")
# print("Input Zip Code")
#
# continue_btn = driver.find_element(By.XPATH, '//input[@id="continue"]')
# continue_btn.click()
# print("Click Continue Button")
#
# '''
# Info Finish Product 1
# '''
# finish_product_1 = driver.find_element(By.XPATH, '//a[@id="item_4_title_link"]')
# value_finish_product_1 = finish_product_1.text
# print(value_finish_product_1)
# assert value_product_1 == value_finish_product_1
# print("Info Finish Product 1 OK")
#
# price_finish_product_1 = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[1]/div[3]/div[2]/div[2]/div')
# value_price_finish_product_1 = price_finish_product_1.text
# print(value_price_finish_product_1)
# assert value_price_product_1 == value_price_finish_product_1
# print("Info Finish Price Product 1 OK")
#
# summary_price = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[6]')
# value_summary_price = summary_price.text
# print(value_summary_price)
# item_total = "Item total: " + value_price_finish_product_1
# print(item_total)
# assert value_summary_price == item_total
# print("Total summary price OK")
#
# finish_btn = driver.find_element(By.XPATH, '//button[@id="finish"]')
# finish_btn.click()
# print("Click Finish Button")