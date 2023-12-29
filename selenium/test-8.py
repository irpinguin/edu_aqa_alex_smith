import datetime
import time

# selenium 4
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path='../chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)
# base_url = 'https://demoqa.com/checkbox'
# base_url = 'https://demoqa.com/buttons'
# base_url = 'https://demoqa.com/date-picker'
# base_url = 'https://demoqa.com/dynamic-properties'
base_url = 'https://demoqa.com/radio-button'
driver.get(base_url)
driver.maximize_window()

# checkbox = driver.find_element(By.XPATH, '//span[@class="rct-checkbox"]')
# checkbox.click()
#
# checkbox_expand = driver.find_element(By.XPATH, '//button[@aria-label="Toggle"]')
# checkbox_expand.click()

# action = ActionChains(driver)
#
# # Double click
# dbl_clk = driver.find_element(By.XPATH, '//button[@id="doubleClickBtn"]')
# action.double_click(dbl_clk).perform()
#
# # Right click
# right_clk = driver.find_element(By.XPATH, '//button[@id="rightClickBtn"]')
# action.context_click(right_clk).perform()
#
# # One click
# # Так не находит XPath
# #one_clk = driver.find_element(By.XPATH, '//button[@id="WNcV0"]')
# # А вот так - находит
# one_clk = driver.find_element(By.XPATH, "//button[text()='Click Me']")
# action.click(one_clk).perform()

# new_date = driver.find_element(By.XPATH, '//input[@id="datePickerMonthYearInput"]')
# # new_date.clear()
# new_date.click()

# new_date.send_keys(Keys.CONTROL + "a")
# new_date.send_keys(Keys.BACKSPACE)
# time.sleep(2)
# new_date.send_keys("09/10/2023")
# time.sleep(2)
# new_date.send_keys(Keys.RETURN)

# time.sleep(5)
# date_17 = driver.find_element(By.XPATH, '//div[@aria-label="Choose Sunday, September 17th, 2023"]')
# time.sleep(5)
# date_17.click()

# time.sleep(5)
# new_date = driver.find_element(By.XPATH, '//input[@id="datePickerMonthYearInput"]')
# new_date.click()
# date_today = driver.find_element(By.XPATH, '//div[contains(@class,"react-datepicker__day--today")]')
# date_today.click()

# time.sleep(5)
# now_date = datetime.datetime.now().strftime("%d")
# print((now_date))
# date = int(now_date) + 4
# locator = f'//div[@aria-label="Choose Sunday, September {str(date)}th, 2023"]'
# print(locator)
# date_17 = driver.find_element(By.XPATH, locator)
# date_17.click()

# try:
#     visible_btn = driver.find_element(By.XPATH, '//button[@id="visibleAfter "]')
#     visible_btn.click()
# except NoSuchElementException as exception:
#     print("!!! NoSuchElementException")
#     time.sleep(5)
#     visible_btn.click()
# print("Click Visible Button")

try:
    yes_radio = driver.find_element(By.XPATH, '//label[@for="yesRadio"]')
    yes_radio.click()
    msg = driver.find_element(By.XPATH, '//span[@class="text-success"]')
    value_msg = msg.text
    print(value_msg)
    assert value_msg == "No"
except AssertionError as exception:
    driver.refresh()
    yes_radio = driver.find_element(By.XPATH, '//label[@for="yesRadio"]')
    yes_radio.click()
    msg = driver.find_element(By.XPATH, '//span[@class="text-success"]')
    value_msg = msg.text
    print(value_msg)
    assert value_msg == "Yes"