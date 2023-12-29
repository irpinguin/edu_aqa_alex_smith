# selenium 4
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver import ActionChains, Keys

from colorama import init, Fore
from colorama import Style

from login_page import Login_page

username_list_loc = "login_credentials"
password_loc = "login_password"

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

# login_name = "standard_user"
# login_name = "locked_out_user"
# login_name = "problem_user"
login_name = "performance_glitch_user"
login_password = "secret_sauce"
timeout = 3

login = Login_page(driver)
login.authorization(login_name, login_password, timeout)

# input("Нажмите Enter для завершения программы и закрытия браузера")
driver.close()










