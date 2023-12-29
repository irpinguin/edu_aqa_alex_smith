# selenium 4
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from colorama import init, Fore
from colorama import Style

class Login_page():

    def __init__(self, driver):
        self.driver = driver
        # Инициализируем colorama для вывода в win10
        init(autoreset=True)

    def check_time(self, start_time, end_time, timeout_sec):
        # Выводит разницу во времени в секундах и если она меньше таймаута, то выводит ее красным шрифтом
        elapsed_time = end_time - start_time
        if elapsed_time < timeout_sec:
            print(f'\t\tвремя выполнения: {end_time - start_time:.2f} сек.')
        else:
            print(f'\t\t{Fore.RED}время выполнения: {end_time - start_time} сек. при установленном таймауте {timeout_sec}{Style.RESET_ALL}')

    def authorization(self, user_name, password, timeout):

        user_name_loc = '//input[@id="user-name"]'
        password_loc = '//input[@id="password"]'
        login_btn_loc = '//input[@id="login-button"]'
        login_err_msg_loc = '//div[@class="error-message-container error"]/h3'
        err_invalid_user = 'Username and password'
        err_blocked_user = 'Sorry, this user has been locked out'
        err_empty_user = 'Username is required'
        err_empty_password = 'Password is required'
        main_page_url = 'https://www.saucedemo.com/inventory.html'
        main_page_sign = 'Products'
        main_page_sign_loc = '//span[@class="title"]'

        print(f"\tТест авторизации и перехода на главную страницу")

        # Заполняем поле Username
        start_time = time.time()
        try:
            user_name_field = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.XPATH, user_name_loc)))
            user_name_field.send_keys(user_name)
            print(f"\tВ поле Input Login введено: {Style.BRIGHT}{user_name}{Style.RESET_ALL}", sep='')
        except NoSuchElementException:
            print(f"\t{Fore.RED}{Style.BRIGHT}Элемент '{user_name_loc}' не найден на странице.{Style.RESET_ALL}")
        except TimeoutException:
            print(f"\t{Fore.RED}{Style.BRIGHT}Превышено время заполнения поля.{Style.RESET_ALL}")
        end_time = time.time()
        self.check_time(start_time, end_time, timeout)

        # Заполняем поле Password
        start_time = time.time()
        try:
            password_field = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.XPATH, password_loc)))
            password_field.send_keys(password)
            print(f"\tВ поле Input Password введено: {Style.BRIGHT}{password}{Style.RESET_ALL}")
        except NoSuchElementException:
            print(f"\t{Fore.RED}{Style.BRIGHT}Элемент '{password}' не найден на странице.{Style.RESET_ALL}")
        except TimeoutException:
            print(f"\t{Fore.RED}{Style.BRIGHT}Превышено время заполнения поля.{Style.RESET_ALL}")
        end_time = time.time()
        self.check_time(start_time, end_time, timeout)

        # Нажимаем кнопку Login
        start_time = time.time()
        try:
            button_login = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.XPATH, login_btn_loc)))
            button_login.click()
            print("\tНажата кнопка Login")
        except NoSuchElementException:
            print(f"\t{Fore.RED}{Style.BRIGHT}Элемент '{login_btn_loc}' не найден на странице.{Style.RESET_ALL}")
        except TimeoutException:
            print(f"\t{Fore.RED}{Style.BRIGHT}Превышено время нажатия на кнопку.{Style.RESET_ALL}")
        end_time = time.time()
        self.check_time(start_time, end_time, timeout)

        # Проверяем заполнение полей Username и Password
        start_time = time.time()
        try:
            err_msg = self.driver.find_element(By.XPATH, login_err_msg_loc).text
            if err_invalid_user in err_msg:
                print(f"\t{Fore.RED}{Style.BRIGHT}Имя пользователя или пароль введены неверно.{Style.RESET_ALL}")
            elif err_empty_user in err_msg:
                print(f"\t{Fore.RED}{Style.BRIGHT}Имя пользователя не введено.{Style.RESET_ALL}")
            elif err_empty_password in err_msg:
                print(f"\t{Fore.RED}{Style.BRIGHT}Пароль не введен.{Style.RESET_ALL}")
            elif err_blocked_user in err_msg:
                print(f"\t{Fore.RED}{Style.BRIGHT}Пользователь заблокирован{Style.RESET_ALL}")

            else:
                print(f"\t{Fore.RED}{Style.BRIGHT}Неизвестная ошибка на странице авторизации.{Style.RESET_ALL}")
        except NoSuchElementException:
            # Если на странице нет сообщения об ошибках, то все хорошо
            print(f"\tПользователь {user_name} с паролем {password} авторизован.")
        end_time = time.time()
        self.check_time(start_time, end_time, timeout)

        # Проверка перехода на главную страницу
#
# Непонимание
# Не получилось поймать задержку открытия главной страницы для пользователя performance_glitch_user
# Пробовал разные варианты: отлавливать по смене урл и по признаку на странице
# В результате сделал через замеры времени исполнения участков кода
# Что-то я не понимаю на уровне где про такое читать.
# Может WebDriverWait для этой цели не подходит или я не умею его готовить
#
        # start_time = time.time()
        # try:
        #     # Проверка того, что URL изменился на https://www.saucedemo.com/inventory.html
        #     success_url = WebDriverWait(self.driver, timeout).until(EC.url_changes(main_page_url))
        #     # success_url = WebDriverWait(self.driver, timeout).until(EC.url_to_be(main_page_url))
        #     # success_url = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, main_page_sign_loc)))
        #     if success_url:
        #         print(f"\tПереход на {main_page_url} прошел за приемлемое время")
        # except TimeoutException:
        #     print(f"\t{Fore.RED}{Style.BRIGHT}Превышено время перехода на страницу {main_page_url}.{Style.RESET_ALL}")
        # end_time = time.time()
        # self.check_time(start_time, end_time, timeout)

        start_time = time.time()
        try:
            # Проверка того, что по указанному URL находится верная страница
            success_sign = WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element((By.XPATH, main_page_sign_loc), main_page_sign))
            if success_sign:
                print(f"\tПереход на страницу {main_page_url} прошел успешно")
        except NoSuchElementException:
            print(f"\t{Fore.RED}{Style.BRIGHT}Элемент '{main_page_sign_loc}' не найден на странице {main_page_url}.{Style.RESET_ALL}")
        except TimeoutException:
            # print(f"\t{Fore.RED}{Style.BRIGHT}Элемент '{main_page_sign_loc}' не найден за ожидаемое время на странице {main_page_url}.{Style.RESET_ALL}")
            print(f"\t{Fore.RED}{Style.BRIGHT}Верстка страницы {main_page_url} отличается от ожидаемой или страница не найдена.{Style.RESET_ALL}")
        except AssertionError:
            print(f"\t{Fore.RED}{Style.BRIGHT}Переход на {main_page_url} не состоялся{Style.RESET_ALL}")
        end_time = time.time()
        self.check_time(start_time, end_time, timeout)

        print("\tТест на авторизацию и переход на главную страницу завершен.")


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








