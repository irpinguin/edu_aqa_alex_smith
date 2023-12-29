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
base_url = 'https://html5css.ru/howto/howto_js_rangeslider.php'
driver.get(base_url)
driver.maximize_window()

login_standard_user = "standard_user"
password_all = "secret_sauce"

action = ActionChains(driver)

slider_1 = driver.find_element(By.XPATH, '//input[@id="id2"]')
action.click_and_hold(slider_1).move_by_offset(-300, 0).release().perform()


