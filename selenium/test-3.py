import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path='../chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

login_standard_user = "standard_user"
password_all = "secret_sauce"

user_name = driver.find_element(By.XPATH, '//input[@id="user-name"]')
user_name.send_keys(login_standard_user)
print("Input Login")
time.sleep(1)
user_name.send_keys(Keys.BACKSPACE)
time.sleep(1)
user_name.send_keys(Keys.BACKSPACE)
time.sleep(1)
user_name.send_keys("er")

password = driver.find_element(By.XPATH, '//input[@id="password"]')
password.send_keys(password_all)
print("Input Password")
password.send_keys(Keys.RETURN)

filter = driver.find_element(By.XPATH, "//select[@data-test='product_sort_container']")
filter.click()
print("Click Filter")
time.sleep(1)
filter.send_keys(Keys.DOWN)
time.sleep(3)
filter.send_keys(Keys.RETURN)
