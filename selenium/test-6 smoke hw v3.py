# selenium 4
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import random
import time
from colorama import init, Fore
from colorama import Back
from colorama import Style

# Инициализируем colorama для вывода в win10
init(autoreset=True)

# Открываем браузер
service = Service(executable_path='../chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

login_standard_user = "standard_user"
password_all = "secret_sauce"
first_name = 'Igor'
last_name = 'Andreev'
zip_code = '664002'
pause_sec = 2

#
# Авторизуемся
#
print("Проходим авторизацию")

try:
    user_name = driver.find_element(By.XPATH, '//input[@id="user-name"]')
    user_name.send_keys(login_standard_user)
    print(f"\tLogin: {login_standard_user}")
except NoSuchElementException:
    print("Элемент 'user-name' не найден на странице. Проверьте локатор.")

try:
    password = driver.find_element(By.XPATH, '//input[@id="password"]')
    password.send_keys(password_all)
    print(f"\tPassword: {password_all}")
except NoSuchElementException:
    print("Элемент 'password' не найден на странице. Проверьте локатор.")

try:
    login_btn = driver.find_element(By.XPATH, '//input[@id="login-button"]')
    login_btn.click()
    print("Нажимаем кнопку Login")
except NoSuchElementException:
    print("Элемент 'login-button' не найден на странице. Проверьте локатор.")

# Даем время на то, чтобы страница прогрузилась
time.sleep(pause_sec)

#
# Выбираем товары
#

# Создаем пустой список для хранения информации о товарах
products = []

# Находим все элементы товаров на странице
try:
    product_elements = driver.find_elements(By.CLASS_NAME, 'inventory_item')
except NoSuchElementException:
    print("Элемент 'inventory_item' не найден на странице. Проверьте локатор.")

# Проходимся по каждому товару и извлекаем информацию
for product_element in product_elements:

    # Название товара
    try:
        product_name = product_element.find_element(By.CLASS_NAME, 'inventory_item_name').text
    except NoSuchElementException:
        print("Элемент 'inventory_item_name' не найден на странице. Проверьте локатор.")

    # Цена товара
    try:
        product_price = float(product_element.find_element(By.CLASS_NAME, 'inventory_item_price').text.strip('$'))
    except NoSuchElementException:
        print("Элемент 'inventory_item_price' не найден на странице. Проверьте локатор.")

    # XPath для кнопки добавления товара
    try:
        add_to_cart_btn = product_element.find_element(By.TAG_NAME, 'button').get_attribute('id')
    except NoSuchElementException:
        print("Элемент 'button' не найден на странице. Проверьте локатор.")

    # Создаем словарь с информацией о товаре и добавляем его в список
    product_info = {
        'name': product_name,
        'price': product_price,
        'btn_id': add_to_cart_btn
    }
    products.append(product_info)

# Выводим список найденных товаров, цену и ИД кнопки добавления в корзину
print("Найдены товары:")
for product in products:
    print(f'\t{product}')

# Выбираем два товара для добавления в корзину
print("Выбраны товары:")
selected_products = random.sample(products, 2)

for selected_product in selected_products:
    product_name = selected_product["name"]
    product_price = selected_product["price"]
    product_btn_id = selected_product["btn_id"]
    print(f'\t{product_name} по цене {product_price:.2f}, id кнопки {product_btn_id}')

# Добавляем выбранные товары в корзину
print("Добавляем товары в корзину:")
for selected_product in selected_products:
    product_name = selected_product["name"]
    product_price = selected_product["price"]
    product_btn_id = selected_product["btn_id"]

    # Находим товар на странице по его названию
    try:
        item_element = driver.find_element(By.XPATH, f"//div[@class='inventory_item_name' and text()='{product_name}']")
        print(f'\tНайден товар: {item_element.text} ...', end='')
        time.sleep(pause_sec)
    except NoSuchElementException:
        print("Элемент 'inventory_item_name' не найден на странице. Проверьте локатор.")

    # Добавляем товар в корзину
    try:
        add_to_cart_button = item_element.find_element(By.XPATH, f"//button[@id='{product_btn_id}']")
        add_to_cart_button.click()
        print(f'\tДобавлен товар: {product_name} по цене {product_price:.2f}')
        time.sleep(pause_sec)
    except NoSuchElementException:
        print("Элемент 'button' не найден на странице. Проверьте локатор.")
#
# Переходим в корзину
#

try:
    cart_btn = driver.find_element(By.XPATH, '//span[@class="shopping_cart_badge"]')
    cart_btn.click()
    print("Переходим в корзину")
    time.sleep(pause_sec)
except NoSuchElementException:
       print("Элемент 'button' не найден на странице. Проверьте локатор.")

# Проверяем, что в корзине находятся именно те товары и с теми же ценами, которые мы добавляли на предыдущей странице

# Создаем пустой список для хранения информации о товарах в корзине
cart_products = []

# Находим все элементы товаров на странице корзины
try:
    cart_elements = driver.find_elements(By.CLASS_NAME, 'cart_item')
except NoSuchElementException:
       print("Элемент 'cart_item' не найден на странице. Проверьте локатор.")

# Извлекаем названия и цены товаров на странице корзины и добавляем их в списки
print("В корзине находятся:")
for cart_product_element in cart_elements:

    # Название товара
    try:
        cart_product_name = cart_product_element.find_element(By.CLASS_NAME, 'inventory_item_name').text
    except NoSuchElementException:
        print("Элемент 'inventory_item_name' не найден на странице. Проверьте локатор.")

    # Цена товара
    try:
        cart_product_price = float(cart_product_element.find_element(By.CLASS_NAME, 'inventory_item_price').text.strip('$'))
    except NoSuchElementException:
        print("Элемент 'inventory_item_price' не найден на странице. Проверьте локатор.")

# Создаем словарь с информацией о товаре в корзине и добавляем его в список
    cart_product_info = {
        'name': cart_product_name,
        'price': cart_product_price
    }
    cart_products.append(cart_product_info)
    print(f'\t{cart_product_name} по цене {cart_product_price:.2f}')

# Проверяем, совпадают ли выбранные товары в корзине
print("Проверяем, что в корзине находятся верные товары по верным ценам:")

if len(selected_products) == len(cart_products):
    print("\tКоличество выбранных товаров совпадает с количеством товаров в корзине")
else:
        print(f"\t{Fore.RED} {Style.BRIGHT}Количество выбранных товаров не совпадает с количеством товаров в корзине.{Style.RESET_ALL}")
        exit()

# Создаем множества для хранения имен и цен в выбранных товарах
selected_names = set(product['name'] for product in selected_products)
selected_prices = set(product['price'] for product in selected_products)

# Создаем множества для хранения имен и цен в товарах в корзине
cart_names = set(product['name'] for product in cart_products)
cart_prices = set(product['price'] for product in cart_products)

# Проверяем идентичность имен и цен в выбранных товарах и товарах в корзине
if selected_names == cart_names and selected_prices == cart_prices:
    print("\tИмена и цены в выбранных товарах и товарах в корзине идентичны.")
else:
    print(f"\t{Fore.RED} {Style.BRIGHT}Имена и/или цены в выбранных товарах и товарах в корзине не идентичны.{Style.RESET_ALL}")

#
# Выписываем счет
#

try:
    checkout_btn = driver.find_element(By.XPATH, '//button[@id="checkout"]')
    checkout_btn.click()
    print("Нажимаем кнопку Checkout")
    time.sleep(pause_sec)
except NoSuchElementException:
    print("Элемент 'button' не найден на странице. Проверьте локатор.")

# Заполняем поля формы
print("Заполняем поля формы")
try:
    first_name_field = driver.find_element(By.XPATH, '//input[@id="first-name"]')
    first_name_field.send_keys(first_name)
    print(f"\tFirst Name: {first_name}")
except NoSuchElementException:
    print("Элемент 'first-name' не найден на странице. Проверьте локатор.")

try:
    last_name_field = driver.find_element(By.XPATH, '//input[@id="last-name"]')
    last_name_field.send_keys(last_name)
    print(f"\tLast Name: {last_name}")
except NoSuchElementException:
    print("Элемент 'last-name' не найден на странице. Проверьте локатор.")

try:
    zip_code_field = driver.find_element(By.XPATH, '//input[@id="postal-code"]')
    zip_code_field.send_keys(zip_code)
    print(f"\tZip Code: {zip_code}")
except NoSuchElementException:
    print("Элемент 'postal-code' не найден на странице. Проверьте локатор.")

#
# Переходим к финишной странице
#

try:
    continue_btn = driver.find_element(By.XPATH, '//input[@id="continue"]')
    continue_btn.click()
    print("Нажимаем кнопку Continue")
    time.sleep(pause_sec)
except NoSuchElementException:
    print("Элемент 'button' не найден на странице. Проверьте локатор.")

# Находим все элементы товаров на странице счета

# Создаем пустой список для хранения информации о товарах в корзине
checkout_products = []

try:
    checkout_elements = driver.find_elements(By.CLASS_NAME, 'cart_item')
except NoSuchElementException:
    print("Элемент 'cart_item' не найден на странице. Проверьте локатор.")

# Извлекаем названия и цены товаров на странице счета и добавляем их в списки
print("В счете находятся:")
for checkout_product_element in checkout_elements:

    # Название товара
    try:
        checkout_product_name = checkout_product_element.find_element(By.CLASS_NAME, 'inventory_item_name').text
    except NoSuchElementException:
        print("Элемент 'inventory_item_name' не найден на странице. Проверьте локатор.")

    # Цена товара
    try:
        checkout_product_price = float(checkout_product_element.find_element(By.CLASS_NAME, 'inventory_item_price').text.strip('$'))
    except NoSuchElementException:
        print("Элемент 'inventory_item_price' не найден на странице. Проверьте локатор.")

# Создаем словарь с информацией о товаре в счете и добавляем его в список
    checkout_product_info = {
        'name': checkout_product_name,
        'price': checkout_product_price
    }
    checkout_products.append(checkout_product_info)
    print(f'\t{checkout_product_name} по цене {checkout_product_price:.2f}')

# Проверяем, совпадают ли выбранные товары в счете
print("Проверяем, что в счете находятся верные товары по верным ценам:")

if len(selected_products) == len(checkout_products):
    print("\tКоличество выбранных товаров совпадает с количеством товаров в счете")
else:
        print(f"\t{Fore.RED} {Style.BRIGHT}Количество выбранных товаров не совпадает с количеством товаров в счете.{Style.RESET_ALL}")
        exit()

# Создаем множества для хранения имен и цен в выбранных товарах
selected_names = set(product['name'] for product in selected_products)
selected_prices = set(product['price'] for product in selected_products)

# Создаем множества для хранения имен и цен в товарах в счете
checkout_names = set(product['name'] for product in checkout_products)
checkout_prices = set(product['price'] for product in checkout_products)

# Проверяем идентичность имен и цен в выбранных товарах и товарах в счете
if selected_names == checkout_names and selected_prices == checkout_prices:
    print("\tИмена и цены в выбранных товарах и товарах в счете идентичны.")
else:
    print(f"\t{Fore.RED} {Style.BRIGHT}Имена и/или цены в выбранных товарах и товарах в счете не идентичны.{Style.RESET_ALL}")

# Проверяем верность подсчета суммы счета
print("Проверяем верность подсчета суммы стоимости товаров")
try:
    checkout_total_price = driver.find_element(By.XPATH, '//div[@class="summary_subtotal_label"]')
    value_checkout_total_price = float(checkout_total_price.text.split('$')[1])
    print(f"\tВ счете указана сумма: {value_checkout_total_price:.2f}")
except NoSuchElementException:
    print("Элемент 'summary_subtotal_label' не найден на странице. Проверьте локатор.")

# Инициализируем переменную для хранения суммы цен
selected_total_price = 0.0

# Перебираем словари в списке и добавляем их цены к общей сумме
for product in selected_products:
    selected_total_price += product['price']

# Выводим общую сумму
print(f"\tОбщая стоимость выбранных товаров: {selected_total_price:.2f}")
assert selected_total_price == value_checkout_total_price
print("\tСумма стоимости выбранных товаров подсчитана верно.")

#
# Завершение
#
try:
    finish_btn = driver.find_element(By.XPATH, '//button[@id="finish"]')
    finish_btn.click()
    print("Нажимаем кнопку Finish")
except NoSuchElementException:
    print("Элемент 'finish' не найден на странице. Проверьте локатор.")

input("Нажмите Enter для завершения программы и закрытия браузера")
driver.close()