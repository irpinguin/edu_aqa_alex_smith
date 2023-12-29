# selenium 4
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from colorama import init, Fore
from colorama import Style

from login_page import Login_page

username_list_loc = "login_credentials"
password_loc = "login_password"
timeout = 3

# Инициализируем colorama для вывода в win10
init(autoreset=True)

service = Service(executable_path='../chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=service, options=options)
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
# driver.maximize_window()
driver.minimize_window()

print("Получаем список пользователей")
# Находим элемент с именами пользователей
try:
    username_list = driver.find_element(By.ID, username_list_loc).text
except NoSuchElementException:
    print(f"\t{Fore.RED}{Style.BRIGHT}Элемент '{username_list_loc}' не найден на странице.{Style.RESET_ALL}")
    exit(1)

# Разделяем текст на имена пользователей
usernames = username_list.split('\n')[1:]

# Находим элемент с паролями
try:
    password_list = driver.find_element(By.CLASS_NAME, password_loc).text
except NoSuchElementException:
    print(f"\t{Fore.RED}{Style.BRIGHT}Элемент '{password_loc}' не найден на странице.{Style.RESET_ALL}")
    exit(1)

# Разделяем текст на пароли
passwords = password_list.split('\n')[1:]

# Запускаем тест на каждого из пользователей
login = Login_page(driver)

i = 1
for username in usernames:
    print(f"Запуск теста {i}")
    login.authorization(username, passwords[0], timeout)
    driver.get(base_url)
    time.sleep(timeout)
    print("---")
    i += 1

print(f"Выполнено тестов: {i - 1}")
input("Нажмите Enter для завершения программы и закрытия браузера")
driver.close()








