import datetime
import time

# selenium 4
from selenium import webdriver
from selenium.webdriver import ActionChains
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

password = driver.find_element(By.XPATH, '//input[@id="password"]')
password.send_keys(password_all)
print("Input Password")

button_login = driver.find_element(By.XPATH, '//input[@id="login-button"]')
button_login.click()
print("Click Login Button")

# driver.execute_script("window.scrollTo(0, 500)")      # X, Y in pixels
action = ActionChains(driver)
red_t_shirt = driver.find_element(By.XPATH, "//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']")
action.move_to_element(red_t_shirt).perform()
time.sleep(2)

now_date = datetime.datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S")
name_screenshot = 'screenshot ' + now_date + '.png'
time.sleep(3)
driver.save_screenshot('./screenshots/' + name_screenshot)
print("OK, screenshot done")