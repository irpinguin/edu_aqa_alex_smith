# selenium 4
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

login_standard_user = "standard_user"
password_all = "secret_sauce"

# Открываем браузер
service = Service(executable_path='./chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)

print("Получаем список пользователей")
# Находим элемент с именами пользователей
username_list = driver.find_element(By.ID, "login_credentials").text
# print(usernames)
# Разделяем текст на имена пользователей
usernames = username_list.split('\n')[1:]

# Выводим имена пользователей на экран
print(usernames)
# for username in usernames:
# #
password = driver.find_element(By.CLASS_NAME, "login_password").text
print(password)