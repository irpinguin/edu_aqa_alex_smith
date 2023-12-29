import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path='../chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
# driver.maximize_window()

#user_name = driver.find_element_by_id("user-name")
# user_name = driver.find_element(By.ID, "user-name")     # ID
# user_name = driver.find_element(By.NAME, "user-name")   # NAME
# user_name = driver.find_element(By.XPATH, '//*[@id="user-name"]')         # Full XPath
# user_name = driver.find_element(By.XPATH, '//input[@id="user-name"]')     # ID XPath
user_name = driver.find_element(By.XPATH, '//input[@data-test="username"]') # data-test XPath
user_name.send_keys("standard_user")

password = driver.find_element(By.CSS_SELECTOR, '#password')    # CSS_SELECTOR
password.send_keys("secret_sauce")

button_login = driver.find_element(By.XPATH, '//input[@value="Login"]')
button_login.click()
