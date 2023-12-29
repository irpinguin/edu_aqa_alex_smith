import datetime
import time

# selenium 4
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def get_delta_date(start_date, delta):
    # Возвращаем строку "<Day of week>, <Month> <day_number><suffix>, Year"
    #   start_date: string
    #   delta: int
    # Пример возвращаемого значения: "Sunday, September 17th, 2023"

    new_date = start_date + datetime.timedelta(delta)
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # Получаем название дня недели (например, "Sunday") и месяца (например, "September") для новой даты
    day_of_week = days_of_week[new_date.weekday()]
    month = new_date.strftime("%B")

    # Получаем числовое значение дня с окончанием в виде "st", "nd", "rd" или "th"
    day = new_date.day
    if 10 <= day % 100 <= 20:
        day_str = str(day) + "th"
    else:
        suffixes = {1: "st", 2: "nd", 3: "rd"}
        day_str = str(day) + suffixes.get(day % 10, "th")

    # Форматируем дату и возвращаем её
    formatted_date = f"{day_of_week}, {month} {day_str}, {new_date.year}"
    return formatted_date



# Создаем экземпляр браузера
service = Service(executable_path='../chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)
base_url = 'https://demoqa.com/date-picker'
driver.get(base_url)
driver.maximize_window()

# Выбираем дата-пикер
time.sleep(10)
new_date = driver.find_element(By.XPATH, '//input[@id="datePickerMonthYearInput"]')
new_date.click()

# Очищаем поле ввода даты
time.sleep(5)
new_date.send_keys(Keys.CONTROL + "a")
new_date.send_keys(Keys.BACKSPACE)

# Вычисляем текущую дату +10 дней и выбираем ее в дата-пикере
time.sleep(5)
now_date = datetime.datetime.now()
print(f'Текущая дата: {now_date}')
delta = 10
# Проверка на високосный год
# leap_year_date = datetime.datetime.strptime("2024-02-19", "%Y-%m-%d")
# print(leap_year_date)
# print(get_delta_date(leap_year_date,10))
# exit(0)
locator = f'//div[@aria-label="Choose {get_delta_date(now_date, delta)}"]'
print(locator)
date_future = driver.find_element(By.XPATH, locator)
date_future.click()
