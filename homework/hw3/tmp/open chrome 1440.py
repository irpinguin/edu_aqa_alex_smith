from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

MAIN_PAGE = 'https://bgb-test.tw1.ru/'

# main
options = webdriver.ChromeOptions()
options.add_argument("--window-size=1441,1080")
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get(MAIN_PAGE)
