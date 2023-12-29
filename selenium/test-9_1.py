import datetime
import time

# selenium 4
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# base_url = 'https://demoqa.com/checkbox'
# base_url = 'https://demoqa.com/buttons'
# base_url = 'https://demoqa.com/date-picker'
base_url = 'https://demoqa.com/dynamic-properties'
# base_url = 'https://demoqa.com/radio-button'

service = Service(executable_path='../chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)
driver.get(base_url)
# driver.maximize_window()
# driver.implicitly_wait(5)

# print("Start test")
# visible_btn = driver.find_element(By.XPATH, '//button[@id="visibleAfter"]')
# visible_btn.click()
# print("Finish test")

print("Start test")
visible_btn = WebDriverWait(driver, 6).until(EC.element_to_be_clickable((By.XPATH, '//button[@id="visibleAfter"]')))
visible_btn.click()
print("Finish test")