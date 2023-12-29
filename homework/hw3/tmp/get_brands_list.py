from selenium import webdriver
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.links import Links
from base.data import Data

FILTER_BTN_LOC = '//section[@class="catalog container"]/div[2]/div[2]/button'
FILTER_BRAND_BTN = '//button[@id="dropdown-filter_manufacturer_and_brands_select"]'
FILTER_BRAND_UL = './following-sibling::div/ul[@class="dropdown-menu inner"]'
FILTER_BRAND_ELEM = '//li[@class="lvl-2"][1]/a'
FILTER_BRAND_ELEM_ITER = '//li[@class="lvl-2"]'
FILTER_BRAND_LI = '//button[@id="dropdown-filter_manufacturer_and_brands_select"]/following-sibling::div/ul[@class="dropdown-menu inner"]/li[@class="lvl-2"]'
BRANDS_SAMPLE_QTY = 10

def get_filter_btn():
    return WebDriverWait(driver, Data.TIMEOUT).until(EC.element_to_be_clickable((By.XPATH, FILTER_BTN_LOC)))


def filter_open():
    btn = get_filter_btn()
    btn_state = btn.get_attribute('aria-pressed')
    print(f'\tFilter state: {btn_state}')
    if btn_state == "false":
        btn.click()
        print("\tOn Catalog page the open filter button is clicked")
    btn_state = btn.get_attribute('aria-pressed')
    print(f'\tFilter state: {btn_state}')


def get_filter_brand_btn():
    return WebDriverWait(driver, Data.TIMEOUT).until(EC.element_to_be_clickable((By.XPATH, FILTER_BRAND_BTN)))


def filter_brand_open():
    get_filter_brand_btn().click()
    print("\tFilter Brand button is clicked.")


# main
driver = webdriver.Chrome()
driver.get(Links.CATALOG_PAGE)
filter_open()
filter_brand_open()

# element = driver.find_element(By.XPATH, FILTER_BRAND_ELEM)
locator = f'{FILTER_BRAND_ELEM_ITER}[{random.randint(1, BRANDS_SAMPLE_QTY+1)}]/a'
element = driver.find_element(By.XPATH, locator)

brand_id = element.get_attribute('data-id')
text = element.text
print(f"ID: {brand_id}, text: {text}\n")

data = []
for i in range(1, BRANDS_SAMPLE_QTY+1):
    locator = f'{FILTER_BRAND_ELEM_ITER}[{i}]/a'
    # print(locator)
    elem = driver.find_element(By.XPATH, f'{locator}')
    brand_id = elem.get_attribute('data-id')
    brand_name = elem.text
    print(f"{i} ID: {brand_id}, text: {brand_name}")
    data.append({'brand_id': brand_id, 'brand_name': brand_name})

# print(f"ID: {brand_id}, text: {brand_name}")
print(data)

found_brand_name = None

# Итерируемся по списку и ищем нужное значение
for item in data:
    if item['brand_name'] == text:
        found_brand_name = item['brand_name']
        break  # Выходим из цикла, когда находим соответствие

# Проверяем, было ли что-то найдено
if found_brand_name is not None:
    print(f"Найден brand_name: {found_brand_name}")
else:
    print("Ничего не найдено")