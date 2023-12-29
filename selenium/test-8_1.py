import time

# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path='../chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)
base_url = 'https://testpages.herokuapp.com/styled/basic-html-form-test.html'
driver.get(base_url)
driver.maximize_window()

# time.sleep(2)
# checkbox = driver.find_element(By.XPATH, '//input[@value="cb1"]')
# checkbox.click()
#
# time.sleep(3)
# checkbox = driver.find_element(By.XPATH, '//input[@value="cb3"]')
# checkbox.click()

time.sleep(2)
radio_btn_1 = driver.find_element(By.XPATH, '//input[@value="rd1"]')
radio_btn_1.click()