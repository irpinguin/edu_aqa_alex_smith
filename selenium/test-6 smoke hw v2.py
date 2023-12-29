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

### Авторизуемся
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

# Даем время на то, чтобы страница прогрузилась
time.sleep(3)

# Создаем пустой список для хранения информации о товарах
products = []

# Найдем все товары на странице
product_elements = driver.find_elements(By.CLASS_NAME, 'inventory_item')

# Пройдемся по товарам и получим информацию о каждом из них
for product_element in product_elements:
    # Извлекаем название товара
    product_name = product_element.find_element(By.CLASS_NAME, 'inventory_item_name').text

    # Извлекаем цену товара и убираем символ "$" и преобразуем в float
    product_price = float(product_element.find_element(By.CLASS_NAME, 'inventory_item_price').text.replace('$', ''))

    # Добавляем информацию о товаре в список
    products.append({"name": product_name, "price": product_price})

# Выбираем случайно два товара для добавления в корзину
selected_products = random.sample(products, 2)
# print(f'selected products {selected_products}')

# Инициализируем переменные для хранения информации о добавленных товарах
added_product_names = []
added_product_prices = []

### Добавляем выбранные случайные два товара в корзину
for selected_product in selected_products:
    product_name = selected_product["name"]
    product_price = selected_product["price"]
    print(f'\tВыбран товар: {product_name} по цене {product_price}')
    # Находим товар на странице по его названию
    item_element = driver.find_element(By.XPATH, f"//div[@class='inventory_item_name' and text()='{product_name}']")
    print(f'\tНайден товар: {item_element.text}')
    time.sleep(3)
    # Добавляем товар в корзину
    add_to_cart_button = item_element.find_element(By.XPATH, "//button[@id='inventory_container']/div/div[1]/div[2]/div[2]")
    # //*[@id="inventory_container"]/div/div[1]/div[2]/div[2]
    add_to_cart_button.click()
    print(f'\tВ корзину добавлен товар: {product_name} по цене {product_price}')
    time.sleep(3)

    # Добавляем информацию о товаре в переменные
    added_product_names.append(product_name)
    added_product_prices.append(product_price)

# Даем время на то, чтобы страница прогрузилась
time.sleep(3)

# Переходим в корзину
cart_btn = driver.find_element(By.XPATH, '//span[@class="shopping_cart_badge"]')
cart_btn.click()
print("Enter Cart")

# Даем время на то, чтобы страница прогрузилась
time.sleep(2)

### Проверяем, что в корзине находятся именно те товары и с теми же ценами, которые мы добавляли на предыдущей странице

# Инициализируем списки для товаров и их цен на странице корзины
cart_product_names = []
cart_product_prices = []

# Находим элементы с названиями и ценами товаров на странице корзины
product_name_elements = driver.find_elements(By.XPATH, '//div[@class="inventory_item_name"]')
product_price_elements = driver.find_elements(By.XPATH, '//div[@class="inventory_item_price"]')

# Извлекаем названия и цены товаров на странице корзины и добавляем их в списки
for name_element, price_element in zip(product_name_elements, product_price_elements):
    cart_product_names.append(name_element.text)
    cart_product_prices.append(float(price_element.text.replace('$', '')))

# Печатаем информацию о товарах в корзине
print("В корзине находятся:")
for i in range(len(cart_product_names)):
    print(f"\t{cart_product_names[i]} по цене {cart_product_prices[i]:.2f}")

# Проверяем, есть ли добавленные товары в корзине
# for added_product_name, added_product_price in zip(added_product_names, added_product_prices):
#     if added_product_name in cart_product_names:
#         index = cart_product_names.index(added_product_name)
#         cart_price = cart_product_prices[index]
#         if cart_price == added_product_price:
#             print(f"Товар '{added_product_name}' с ценой {added_product_price} найден в корзине.")
#         else:
#             print(f"Цена для товара '{added_product_name}' не соответствует ожидаемой.")
#     else:
#         print(f"Товар '{added_product_name}' не найден в корзине.")

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