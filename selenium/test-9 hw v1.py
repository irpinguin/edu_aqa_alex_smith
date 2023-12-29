# selenium 4
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from colorama import init, Fore
from colorama import Style

# Инициализируем colorama для вывода в win10
init(autoreset=True)

def print_err_msg(text):
    # Выводит сообщение шрифтом красного цвета
    print(f"\t{Fore.RED} {Style.BRIGHT}{text}{Style.RESET_ALL}")

def login(driver, username, password):
    # Проходим авторизацию

    user_name_loc = '//input[@id="user-name"]'
    password_loc = '//input[@id="password"]'
    login_btn_loc = '//input[@id="login-button"]'
    login_err_msg_loc = '//div[@class="error-message-container error"]/h3'
    err_invalid_user = 'Username and password'
    err_empty_user = 'Username is required'
    err_empty_password = 'Password is required'

    print("Проходим авторизацию")

    # Заполняем поле Username
    try:
        user_name = driver.find_element(By.XPATH, user_name_loc)
        user_name.send_keys(username)
        print(f"\tLogin: {username}")
    except NoSuchElementException:
        print_err_msg(f"Элемент '{user_name_loc}' не найден на странице.")

    # Заполняем поле Password
    try:
        password_field = driver.find_element(By.XPATH, password_loc)
        password_field.send_keys(password)
        print(f"\tPassword: {password}")
    except NoSuchElementException:
        print_err_msg(f"Элемент '{password}' не найден на странице.")

    # Нажимаем кнопку Login
    try:
        login_btn = driver.find_element(By.XPATH, login_btn_loc)
        login_btn.click()
        print("\tНажимаем кнопку Login")
    except NoSuchElementException:
        print(f"Элемент '{login_btn_loc}' не найден на странице.")

    # Проверяем корректность заполнения полей Username и Password
    try:
        err_msg = driver.find_element(By.XPATH, login_err_msg_loc).text
        if err_invalid_user in err_msg:
            print_err_msg("Имя пользователя или пароль введены неверно.")
        elif err_empty_user in err_msg:
            print_err_msg("Имя пользователя не введено.")
        elif err_empty_password in err_msg:
            print_err_msg("Пароль не введен.")
        else:
            print_err_msg("Неизвестная ошибка на странице авторизации.")
    except NoSuchElementException:
        # Если на странице нет сообщения об ошибках, то все хорошо
        print("\tАвторизация прошла успешно")

def get_products(driver, inventory):
    # Получаем список товаров, которые есть на странице
    # inventory: если True - то страница товаров, если False - то страница корзины
    # Возвращаем список словарей с названием товара, ценой и элементом локатора кнопки добавления в корзину

    inventory_item_loc = 'inventory_item'
    cart_items_loc = 'cart_item'
    inventory_item_name_loc = 'inventory_item_name'
    inventory_item_price_loc = 'inventory_item_price'
    add_to_cart_btn_loc = 'button'


    # Создаем пустой список для хранения информации о товарах
    products = []

    # выбираем все товары на странице
    if inventory:
        try:
            product_elements = driver.find_elements(By.CLASS_NAME, inventory_item_loc)
        except NoSuchElementException:
            print_err_msg("Элемент {inventory_item_loc} не найден на странице.")
    else:
        try:
            product_elements = driver.find_elements(By.CLASS_NAME, cart_items_loc)
        except NoSuchElementException:
            print_err_msg(f"Элемент {cart_items_loc} не найден на странице.")

    # проходим по каждому товару на странице
    for product_element in product_elements:

        # получаем у текущего товара название
        try:
            product_name = product_element.find_element(By.CLASS_NAME, inventory_item_name_loc).text
        except NoSuchElementException:
            print_err_msg(f"Элемент {inventory_item_name_loc} не найден на странице.")

        # получаем у текущего товара строку с ценой и преобразуем ее в вещественное число
        try:
            product_price = float(product_element.find_element(By.CLASS_NAME, inventory_item_price_loc).text.strip('$'))
        except NoSuchElementException:
            print_err_msg(f"Элемент {inventory_item_price_loc} не найден на странице.")

        # получаем для текущего товара ИД локатора для кнопки добавления в корзину
        if inventory:
            try:
                add_to_cart_btn = product_element.find_element(By.TAG_NAME, add_to_cart_btn_loc).get_attribute('id')
            except NoSuchElementException:
                print_err_msg(f"Элемент {add_to_cart_btn_loc} не найден на странице.")

        if inventory:
            product_info = {
                'name': product_name,
                'price': product_price,
                'btn_id': add_to_cart_btn
            }
        else:
            product_info = {
                'name': product_name,
                'price': product_price
            }

        products.append(product_info)
    return products



base_url = 'https://www.saucedemo.com/'
login_standard_user = "standard_user"
password_all = "secret_sauce"
first_name = 'Igor'
last_name = 'Andreev'
zip_code = '664002'

# Открываем браузер
service = Service(executable_path='../chromedriver.exe')
options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(service=service, options=options)
driver = webdriver.Chrome(service=service)
driver.get(base_url)
driver.minimize_window()

# Авторизуемся
login(driver, login_standard_user, password_all)

# Получаем данные о товарах, которые есть на странице
print("Введите номер товара для тестирования бизнес-пути или Q для выхода:")
products = get_products(driver, True)
for i, product in enumerate(products, start=1):
    print(f"\t{i}. {product['name']}")

# Выбираем товар для добавления в корзину
while True:
    choice = input('> ')
    if choice.isnumeric() and 1 <= int(choice) <= len(products):
        selected_product = products[int(choice) - 1]
        print(f"\tВыбран товар: {selected_product['name']}")
        break
        # Здесь вы можете выполнить действия с выбранным товаром
    elif choice.lower() == 'q':
        print(choice)
        break
    else:
        print("\tНекорректный ввод. Введите номер товара или Q для выхода.")

# Находим товар на странице по его названию
product_loc = f"//div[@class='inventory_item_name' and text()='{selected_product['name']}']"
add_to_cart_btn_loc = f"//button[@id='{selected_product['btn_id']}']"

try:
    item_element = driver.find_element(By.XPATH, product_loc)
    # print(f'\tНайден товар: {item_element.text}')
except NoSuchElementException:
    print_err_msg(f"Элемент {product_loc} не найден на странице.")

# Добавляем товар в корзину
try:
    add_to_cart_btn = item_element.find_element(By.XPATH, add_to_cart_btn_loc)
    add_to_cart_btn.click()
    print(f"\tДобавлен в корзину товар: {selected_product['name']} по цене {selected_product['price']:.2f}")
except NoSuchElementException:
    print_err_msg(f"Элемент {add_to_cart_btn_loc} не найден на странице.")

# Переходим в корзину
cart_btn_loc = '//span[@class="shopping_cart_badge"]'

try:
    cart_btn = driver.find_element(By.XPATH,cart_btn_loc)
    cart_btn.click()
    print("Переходим в корзину")
except NoSuchElementException:
       print_err_msg(f"Элемент {cart_btn_loc} не найден на странице.")

# Проверяем, что в корзине находится выбранный товар по верной цене
cart = get_products(driver, False)

if len(cart) == 1:
    print(f"\tВ корзине находится: {cart[0]['name']} по цене {cart[0]['price']:.2f}")
elif len(cart) == 0:
    print_err_msg("В корзине нет товаров")
else:
    print_err_msg("В корзине находится больше товаров, чем добавлено")

# Проверяем идентичность имен и цен в выбранных товарах и товарах в корзине
if selected_product['name'] == cart[0]['name'] and selected_product['price'] == cart[0]['price']:
    print("\tИмена и цены у выбранного товара и товара в корзине идентичны.")
else:
    print_err_msg("Имена и/или цены в выбранных товарах и товарах в корзине не идентичны.")

# Переходим к заполнению счета
checkout_btn_loc = '//button[@id="checkout"]'

try:
    checkout_btn = driver.find_element(By.XPATH, checkout_btn_loc)
    checkout_btn.click()
    print("Нажимаем кнопку Checkout")
except NoSuchElementException:
    print_err_msg(f"Элемент {checkout_btn_loc} не найден на странице.")

# Заполняем поля формы счета
print("Заполняем поля формы")

first_name_field_loc = '//input[@id="first-name"]'
last_name_field_loc = '//input[@id="last-name"]'
zip_code_field_loc = '//input[@id="postal-code"]'
try:
    first_name_field = driver.find_element(By.XPATH, first_name_field_loc)
    first_name_field.send_keys(first_name)
    print(f"\tFirst Name: {first_name}")
except NoSuchElementException:
    print_err_msg(f"Элемент {first_name_field_loc} не найден на странице")

try:
    last_name_field = driver.find_element(By.XPATH, last_name_field_loc)
    last_name_field.send_keys(last_name)
    print(f"\tLast Name: {last_name}")
except NoSuchElementException:
    print_err_msg(f"Элемент {last_name_field_loc} не найден на странице.")

try:
    zip_code_field = driver.find_element(By.XPATH, zip_code_field_loc)
    zip_code_field.send_keys(zip_code)
    print(f"\tZip Code: {zip_code}")
except NoSuchElementException:
    print_err_msg(f"Элемент {zip_code_field_loc} не найден на странице.")

# Переходим к финишной странице
continue_btn_loc = '//input[@id="continue"]'

try:
    continue_btn = driver.find_element(By.XPATH, continue_btn_loc)
    continue_btn.click()
    print("Нажимаем кнопку Continue")
except NoSuchElementException:
    print_err_msg(f"Элемент {continue_btn_loc} не найден на странице.")

# Проверяем, что в счете находится выбранный товар по верной цене
checkout = get_products(driver, False)

if len(checkout) == 1:
    print(f"\tВ счете находится: {checkout[0]['name']} по цене {checkout[0]['price']:.2f}")
    print(f"\tВыбран товар: {selected_product['name']}")
elif len(cart) == 0:
    print_err_msg("В счете нет товаров")
else:
    print_err_msg("В счете находится больше товаров, чем добавлено")

# Проверяем идентичность имен и цен в выбранных товарах и товарах в счете
if selected_product['name'] == checkout[0]['name'] and selected_product['price'] == checkout[0]['price']:
    print("\tИмя и цена у выбранного товара и товара в счете идентичны.")
else:
    print_err_msg("Имя и/или цена у выбранного товара и товара в счете не идентичны.")

# Проверяем верность подсчета суммы счета
checkout_total_price_loc = '//div[@class="summary_subtotal_label"]'

try:
    checkout_total_price = driver.find_element(By.XPATH, checkout_total_price_loc)
    value_checkout_total_price = float(checkout_total_price.text.split('$')[1])
except NoSuchElementException:
    print_err_msg(f"Элемент {checkout_total_price_loc} не найден на странице.")

if selected_product['price'] == value_checkout_total_price:
    print("\tСумма стоимости выбранных товаров подсчитана верно.")
else:
    print_err_msg("Общая сумма счета подсчитана неверно.")

# Завершение
finish_btn_loc = '//button[@id="finish"]'
try:
    finish_btn = driver.find_element(By.XPATH, finish_btn_loc)
    finish_btn.click()
    print("Нажимаем кнопку Finish")
except NoSuchElementException:
    print_err_msg(f"Элемент {finish_btn_loc} не найден на странице.")

input("Нажмите Enter для завершения программы и закрытия браузера")
driver.close()