import datetime
import time

# selenium 4
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
password_all = "secret_sauce"

user_name = driver.find_element(By.XPATH, '//input[@id="user-name"]')
user_name.send_keys(login_standard_user)
print("Input Login")

# time.sleep(3)
# user_name.clear()

password = driver.find_element(By.XPATH, '//input[@id="password"]')
password.send_keys(password_all)
print("Input Password")

button_login = driver.find_element(By.XPATH, '//input[@id="login-button"]')
button_login.click()
print("Click Login Button")

menu = driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']")
menu.click()
print("Click Menu Button")
time.sleep(3)
link_about = driver.find_element(By.XPATH, "//a[@id='about_sidebar_link']")
link_about.click()
print("Click Link Item in Menu Button")
time.sleep(10)

# тут надо теперь проверить что мы перешли на нужный внешний ресурс и сделать скриншот
url = "https://saucelabs.com/"
get_url = driver.current_url
print(get_url)
assert url == get_url
print("OK, get url for new resource done")

now_date = datetime.datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S")
name_screenshot = 'screenshot ' + now_date + '.png'
# time.sleep(3)
driver.save_screenshot('./screenshots/' + name_screenshot)
print("OK, screenshot done")

driver.back()
print("Go Back")
time.sleep(5)

driver.forward()
print("Go Forward")