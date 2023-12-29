from selenium import webdriver
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
login_invalid_user = "standard_use"
password_all = "secret_sauce"
password_invalid = "secret_sauc"

# Check login with invalid user name and valid password
user_name = driver.find_element(By.XPATH, '//input[@id="user-name"]')
user_name.send_keys(login_invalid_user)
print("Input Login")

password = driver.find_element(By.XPATH, '//input[@id="password"]')
password.send_keys(password_all)
print("Input Password")

button_login = driver.find_element(By.XPATH, '//input[@id="login-button"]')
button_login.click()
print("Click Login Button")

warring_text = driver.find_element(By.XPATH, "//h3[@data-test='error']")
value_warring_text = warring_text.text
assert value_warring_text == "Epic sadface: Username and password do not match any user in this service"
print("OK. Invalid login processed correctly")
driver.refresh()

# Check login with valid user name and invalid password
print()
user_name = driver.find_element(By.XPATH, '//input[@id="user-name"]')
user_name.send_keys(login_standard_user)
print("Input Login")

password = driver.find_element(By.XPATH, '//input[@id="password"]')
password.send_keys(password_invalid)
print("Input Password")

button_login = driver.find_element(By.XPATH, '//input[@id="login-button"]')
button_login.click()
print("Click Login Button")

warring_text = driver.find_element(By.XPATH, "//h3[@data-test='error']")
value_warring_text = warring_text.text
assert value_warring_text == "Epic sadface: Username and password do not match any user in this service"
print("OK. Invalid password processed correctly")
driver.refresh()